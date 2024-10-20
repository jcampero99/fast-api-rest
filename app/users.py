from app.db import models 
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select 
from app import schemas 
from app.db.database import get_db

router = APIRouter(
    prefix="/api/v1",
    tags=["users"]
)


# endpoint para crear un usuario 
@router.post("/post-users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

# Endpoint para obtener todos los usuarios 
@router.get("/get-users/", response_model=list[schemas.User])
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.User))
    users = result.scalars().all()
    return users 

