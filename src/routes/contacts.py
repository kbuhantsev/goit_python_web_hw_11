from typing import List

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_session
from src.schemas.schemas import ContactSchema, ContactSchemaResponse
from src.repository import contacts as contacts_repo

router = APIRouter(prefix='/contacts', tags=["contacts"])


@router.get("/", response_model=List[ContactSchemaResponse])
async def get_contacts(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_session)):
    tags = await contacts_repo.get_contacts(skip, limit, db)
    return tags


@router.get("/{contact_id}", response_model=ContactSchemaResponse)
async def get_contact_by_id(contact_id: int, db: AsyncSession = Depends(get_session)):
    tag = await contacts_repo.get_contact(contact_id, db)
    if tag is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tag not found")
    return tag


# @router.post("/", response_model=ContactSchemaResponse)
# async def create_tag(body: TagModel, db: Session = Depends(get_db)):
#     return await repository_tags.create_tag(body, db)
#
#
# @router.put("/{tag_id}", response_model=ContactSchemaResponse)
# async def update_tag(body: TagModel, tag_id: int, db: Session = Depends(get_db)):
#     tag = await repository_tags.update_tag(tag_id, body, db)
#     if tag is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tag not found")
#     return tag
#
#
# @router.delete("/{tag_id}", response_model=ContactSchemaResponse)
# async def remove_tag(tag_id: int, db: Session = Depends(get_db)):
#     tag = await repository_tags.remove_tag(tag_id, db)
#     if tag is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tag not found")
#     return tag