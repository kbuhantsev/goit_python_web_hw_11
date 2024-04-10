
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.database.models import Contact
# from src.schemas.schemas import ContactSchema


async def get_contacts(skip: int, limit: int, db: AsyncSession) -> [Contact]:
    query = select(Contact).offset(skip).limit(limit)
    res = await db.execute(query)
    return res.scalars().all()


# async def get_tags(skip: int, limit: int, db: Session) -> List[Tag]:
#     return db.query(Tag).offset(skip).limit(limit).all()
#
#
# async def get_tag(tag_id: int, db: Session) -> Tag:
#     return db.query(Tag).filter(Tag.id == tag_id).first()
#
#
# async def create_tag(body: TagModel, db: Session) -> Tag:
#     tag = Tag(name=body.name)
#     db.add(tag)
#     db.commit()
#     db.refresh(tag)
#     return tag
#
#
# async def update_tag(tag_id: int, body: TagModel, db: Session) -> Tag | None:
#     tag = db.query(Tag).filter(Tag.id == tag_id).first()
#     if tag:
#         tag .name = body.name
#         db.commit()
#     return tag
#
#
# async def remove_tag(tag_id: int, db: Session)  -> Tag | None:
#     tag = db.query(Tag).filter(Tag.id == tag_id).first()
#     if tag:
#         db.delete(tag)
#         db.commit()
#     return tag
