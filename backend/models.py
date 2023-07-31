from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from database import Base


class UserItems(Base):

    # We have used only one table and then we have kept the user data there.
    __tablename__ = 'useritems'

    id=Column(Integer, primary_key=True, index=True)
    
    # We need the username, question and the answer to store in the database.
    username= Column(String, unique=False, index=False)

    question= Column(String, unique=False, index=False)

    answer=Column(String, unique=False, index=True)


# The following is the base model for Pydantic to validate that we want to have the data in the format. 

class Question(BaseModel):
    username: str | None= None
    question: str | None = None
    answer: str | None = None