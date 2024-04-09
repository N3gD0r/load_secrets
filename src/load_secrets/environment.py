import os


def get_env() -> dict:
    secrets = {
        "username": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "db_host": os.getenv("DB_HOST"),
        "db_port": os.getenv("DB_PORT"),
        "db_name": os.getenv("DB_NAME"),
        "jwt_key": os.getenv("JWT_SECRET")
    }
    return secrets

