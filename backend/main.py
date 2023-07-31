import crud
import crud, models
from models import Question
from fastapi import FastAPI
from sqlalchemy.orm import Session
from responses import getResponses
from fastapi import Depends, FastAPI
from database import SessionLocal, engine
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# These core origins are enabled by default.
origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "http://localhost:3000",
]

# Initialize the fast api object.
app = FastAPI()

# Add middle wares to the origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def getResponse(query:Question,db: Session = Depends(get_db)):
    try:
        res=await getResponses(query.question, query)
        query.answer=res
        crud.create_user(db, query)
        print(res)
        return {"response": res}
    except Exception as e:
        return JSONResponse(content={"error": str(e)})

# Post request of the API to make POST requests. 
@app.post("/postquestion")
async def postquestion(query: Question,db: Session = Depends(get_db)):
    print(query)
    print(query.username)
    print(query.question)
    # Await fro the response to be handled.
    result=await getResponse(query,db=db)
    print("************************************ ")
    print(result)
    # Return the message object in the form of dictionary. FastAPI will convert into JSON.
    return {"result":result}


# Driver code of the program
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)