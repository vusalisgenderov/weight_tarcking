from fastapi import FastAPI
from fastapi import FastAPI,Depends
from db import get_db
from sqlalchemy.orm import Session
from service import *
from scheme import *


app = FastAPI()

@app.get("/")
def healthy_check():
    return {"msg":"this is my site"}


@app.get("/weight")
def your_current_weight(username:str,db:Session=Depends(get_db)):
    msg=get_current_weight(username=username,db=db)
    return msg


@app.get("/weight/difference")
def difference_of_weight(username:str,db:Session=Depends(get_db)):
    msg=get_difference_weight(username=username,db=db)
    return msg

@app.get("/weight/bmi")
def get_bmi_of_weight(username:str,db:Session=Depends(get_db)):
    msg=calculate_bmi(username=username,db=db)
    return msg


@app.post("/user")
def create_user(item:UserCreateSchema,db:Session=Depends(get_db)):
    msg=create_user_in_db(data=item,db=db)
    return msg


@app.post("/weight")
def add_weight_to_your_profile(item:UserCreateWeightschema,db:Session=Depends(get_db)):
    msg=add_your_weight(data=item,db=db)
    return msg
