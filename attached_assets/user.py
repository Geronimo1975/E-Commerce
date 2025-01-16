from enum import Enum

class UserRole(Enum):
    ADMIN = "admin"
    PARTNER = "partner"

class User:
    def __init__(self, username: str, password: str, role: UserRole):
        self.username = username
        self.password = password  # Într-o aplicație reală, folosește hashing pentru parole!
        self.role = role

    def __repr__(self):
        return f"User(username={self.username}, role={self.role.value})"

    def check_password(self, password: str) -> bool:
        """Verifică dacă parola introdusă este corectă (momentan fără hashing)."""
        return self.password == password

