from models import *
from sqlalchemy.orm import Session
from exceptions import *
from setting import DATABASE_URL
from scheme import *
import bcrypt
from datetime import date

def get_current_weight(*,username:str,db:Session):
    user=db.query(Weight).filter_by(username=username).all()

    if not user:
        raise UserNotWeight()
    ls=[]
    for i in user:
        ls.append(i.date)
    max_date=max(ls)
    for i in user:
        if i.date==max_date:
            result=user[user.index(i)].weight
    return {"current_weight":result}

def create_user_in_db(*,data:UserCreateSchema,db:Session):
    hashed_password=bcrypt.hashpw(data.password.encode("utf-8"),bcrypt.gensalt())
    user=db.query(User).filter_by(username=data.username).first()
    if user:
        raise UserIsExists()
    new_user=User(username=data.username,password=hashed_password.decode("utf-8"),height=data.height)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg":"user is created"}

def add_your_weight(*,data:UserCreateWeightschema,db:Session):
    user=db.query(User).filter_by(username=data.username).first()
    user_weight=db.query(Weight).filter_by(username=data.username,date=data.date).first()
    new_weight_of_user=Weight(username=data.username,weight=data.weight,date=data.date)
    if not user:
        raise UserNottFoundException()
    if user_weight:
        db.query(Weight).filter_by(username=data.username,date=data.date).update({"weight":data.weight})
        db.commit()
        return {"msg":"weight is added"}
    db.add(new_weight_of_user)
    db.commit()
    db.refresh(new_weight_of_user)
    return {"msg":"weight is added"}

def get_difference_weight(*,username:str,db:Session):
    user_weight=db.query(Weight).filter_by(username=username).all()
    if not user_weight:
        raise UserNottFoundException()
    ls=[]
    for i in user_weight:
        ls.append(i.date)
    max_date=max(ls)
    min_date=min(ls)
    for i in user_weight:
        if i.date==max_date:
            last_wieght=user_weight[user_weight.index(i)].weight
        if i.date==min_date:
            first_wieght=user_weight[user_weight.index(i)].weight 
    if last_wieght>first_wieght:
        result=last_wieght-first_wieght
        return {"your_weight_difference (weight gain) ":result}
    elif last_wieght<first_wieght:
        result=first_wieght-last_wieght
        return {"your_weight_difference (weight lose) ":result}
    else:
        return {"your weight has not changed"}
    

def calculate_bmi(*,username:str,db:Session):
    user = db.query(User).filter_by(username=username).first()
    user_weight = db.query(Weight).filter_by(username=username).all()
    ls=[]
    if not user_weight:
        raise UserNottFoundException()
    for i in user_weight:
        ls.append(i.date)
    max_date=max(ls)
    for i in user_weight:
        if i.date==max_date:
            last_wieght=user_weight[user_weight.index(i)].weight
    your_bmi=(last_wieght/(user.height**2))*10000
    return {"your bmi":round(your_bmi,2)}
