from enum import Enum

class UserRole(Enum):
    ADMIN = "admin"
    PARTNER = "partner"

class User:
    def __init__(self, username: str, password: str, role: UserRole):
        self.username = username
        self.password = password  # In a production app, use password hashing!
        self.role = role

    def __repr__(self):
        return f"User(username={self.username}, role={self.role.value})"

    def check_password(self, password: str) -> bool:
        """Check if the provided password is correct (currently without hashing)."""
        return self.password == password
