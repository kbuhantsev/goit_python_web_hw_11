
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from src.database.models import Contact
from src.schemas.schemas import ContactSchema


async def get_contacts(skip: int, limit: int, db: AsyncSession) -> [Contact]:
    query = select(Contact).offset(skip).limit(limit)
    res = await db.execute(query)
    return res.scalars().all()


async def get_contact(contact_id: int, db: AsyncSession) -> Contact:
    query = select(Contact).where(Contact.id == contact_id)
    res = await db.execute(query)
    return res.scalars().first()


async def create_contact(contact: ContactSchema, db: AsyncSession) -> Contact:
    contact = Contact(**contact.dict())
    db.add(contact)
    await db.flush()
    await db.commit()

    return contact


async def update_contact(contact_id: int, contact: ContactSchema, db: AsyncSession) -> Contact:
    pass


async def delete_contact(contact_id: int, db: AsyncSession) -> Contact | None:
    contact = await db.get(Contact, contact_id)
    if contact:
        await db.delete(contact)
        await db.flush()
        await db.commit()

    return contact



# async def get_tags(skip: int, limit: int, db: Session) -> List[Tag]:
#     return db.query(Tag).offset(skip).limit(limit).all()
#
#
# async def get_contact(tag_id: int, db: Session) -> Tag:
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
