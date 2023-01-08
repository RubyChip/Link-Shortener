from app.db.base import db_session


async def get_db_session():
    session = db_session()
    try:
        yield session
    finally:
        await session.close()
