from Database import users,database
from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from Schema import schema
from Authentication import role_based_access

access = role_based_access.role_required

router = APIRouter(
    tags=["Users"],
    prefix="/user"
)

@router.get("/")
def show_all_user(db:Session=Depends(database.get_db),current_user : schema.Users = Depends(access(role_based_access.level_1))):
    """This function is called when we need to see all the available users."""
    print(current_user.user_role)
    print(role_based_access.level_2)
    if current_user.user_role not in role_based_access.level_2:
        return "Not Authorised User"
    else:
        result = users.get_all_users(db)
        print(result)
        return result

@router.get("/show_by_id")
def show_user_by_id(user_id:int,db:Session=Depends(database.get_db)):
    """This tool is used when we need to get access of only a particular user id's data"""
    user=users.get_user_by_id(db,user_id)
    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Not Found")
    return user

@router.post("/add_user")
def add_new_user(details:schema.Users,db:Session=Depends(database.get_db)):
    """To add a new user to the database we will use this tool."""
    return users.add_user(db,details=details)

@router.put("/update_user")
def update(user_id:int,details:schema.UpdateUser,db:Session=Depends(database.get_db)):
    """To update any details (complete or partial details) of the user, we will use this tool."""
    return users.update_user(details=details,db=db,user_id=user_id)

@router.delete("/delete_user")
def delete(user_id: int,db:Session=Depends(database.get_db)):
    """To delete any user from the database we will use this tool."""
    result=users.delete_user(user_id=user_id,db=db)
    if result:
        return result
    return "User Not Found"