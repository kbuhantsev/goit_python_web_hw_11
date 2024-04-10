from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:masterkey@localhost:5432/contacts"
engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, echo=True)


# Dependency
def get_db():
    async with SessionLocal() as session:
        yield session
