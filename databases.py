import pymysql
from config.config import Settings as settings


def create_connection():
    return pymysql.connect(
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        database=settings.DB_NAME,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=False
    )


def get_connection():
    connection = create_connection()
    try:
        yield connection
    finally:
        connection.close()