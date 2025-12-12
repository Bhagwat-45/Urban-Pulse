import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    dbname: str = os.getenv("Database_Name")
    user: str = os.getenv("User", default="postgres")
    password: str = os.getenv("Password")
    host: str = os.getenv("Host", default="localhost")
    port: str = os.getenv("Port", default="5432") 

settings = Settings()