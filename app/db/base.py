from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.configs.base import settings
from app.configs.db import DATABASE_URL

Base = declarative_base()

db_engine = create_async_engine(DATABASE_URL, future=True, echo=settings.DATABASE_LOGS)

db_session = sessionmaker(class_=AsyncSession)
db_session.configure(bind=db_engine)
