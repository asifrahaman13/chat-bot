from pydantic import BaseModel

# Pydantic base model - the format on which we want  our JSON input. 
class UserSchema(BaseModel):
    # Here we need the username, question and the answer field to dispaly.
    username: str | None =None
    question: str | None= None
    answer: str | None= None
    
    # We kept the object relationship to be true 
    class Config:
        orm_mode = True