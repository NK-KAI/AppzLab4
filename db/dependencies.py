from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from db.models import TokenData
from db.models import User
from auth.utils import verify_password, SECRET_KEY, ALGORITHM
from db.database import get_db
from db.repositories.user import UserRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


# def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#     except JWTError:
#         raise credentials_exception
#     repo = UserRepository(db)
#     user = repo.get_by_name(token_data.username)
#     if user is None:
#         raise credentials_exception
#     return user
