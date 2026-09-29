from fastapi import FastAPI
app = FastAPI()

@app.get('/home')
def home():
    return {"message":"welcome to fastApi"}

@app.get('/')
def home2():
    return {"message":"welcome to fastApi lesson"}

@app.get('/sct')
def func2():
    return{"message":'welcome to sct'}