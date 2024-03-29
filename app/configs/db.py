from app.configs.base import settings

DATABASE_HOST, DATABASE_PORT, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME = (
    settings.DATABASE_HOST,
    settings.DATABASE_PORT,
    settings.DATABASE_USER,
    settings.DATABASE_PASSWORD,
    settings.DATABASE_NAME,
)

DATABASE_URL = (
    f"postgresql+asyncpg://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
)
