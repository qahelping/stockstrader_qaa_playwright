from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    email: str
    password: str
    account_number: Optional[int] = None


BASE_PASSWORD = "8ce9B9a*U(w"

USER = User(email="yanushevskayaelena132@gmail.com", password=BASE_PASSWORD)
