import models, schemas
from sqlalchemy.orm import Session

# Function to get the user information from the database.

def get_user(db: Session, user_id: int):
    # Get the uer where the id matches with the user. 
    return db.query(models.UserItems).filter(models.UserItems.id == user_id).first()


# Function to create the user information from the database.

def create_user(db: Session, user: schemas.UserSchema):
    db_user = models.UserItems(username=user.username, question=user.question, answer=user.answer)

    # Add the user data.
    db.add(db_user)

    # Commit your changes in the database.
    db.commit()

    # Refresh all the changes that took place.
    db.refresh(db_user)

    # Return the user information
    return db_user