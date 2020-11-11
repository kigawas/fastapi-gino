from fastapi import APIRouter

from ..models import User as UserModel
from ..schemas.user import User
from ..schemas.user import UserCreate

router = APIRouter()


@router.get("/")
async def get_users():
    users = await UserModel.query.gino.all()
    return [User.from_orm(u) for u in users]


@router.get("/{pk}")
async def get_user(pk: int):
    user = await UserModel.get(pk)
    return User.from_orm(user)


@router.get("/{pk}/bake")
async def get_user_bake(pk: int):
    user = await UserModel.get_bake(pk)
    return User.from_orm(user)


@router.get("/{pk}/raw")
async def get_user_raw(pk: int):
    user = await UserModel.get_raw(pk)
    # do not use from_orm to speed up
    return dict(name=user.name, id=user.id)


@router.post("/")
async def create_user(user: UserCreate):
    created = await UserModel.create(name=user.name)
    return User.from_orm(created)
