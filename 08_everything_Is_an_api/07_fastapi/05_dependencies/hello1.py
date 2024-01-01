from fastapi import FastAPI, Depends 
def depfunc1():
    pass
def depfunc2(): 
    pass
app = FastAPI(dependencies=[Depends(depfunc1), Depends(depfunc2)])

@app.get("/main") 
def get_main():
    pass
