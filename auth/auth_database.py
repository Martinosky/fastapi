from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# Variables de entorno obtenidas desde docker-compose.yml
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "123456")
MYSQL_HOST = os.getenv("MYSQL_HOST", "db")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "fastapi_db")

# URL de conexión
DATABASE_URL = (
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}"
    f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
)

# Debug temporal
print("MYSQL_HOST:", MYSQL_HOST)
print("MYSQL_PORT:", MYSQL_PORT)
print("DATABASE_URL:", DATABASE_URL)

# Engine de SQLAlchemy
engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)

# Sesiones
SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)

# Dependency para FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Base para modelos ORM
Base = declarative_base()