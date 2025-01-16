from inventory.user import User, UserRole

class UserManager:
    def __init__(self):
        """Initializes the user manager with a default admin user."""
        self.users = {
            "admin": User("admin", "admin123", UserRole.ADMIN)
        }

    def register_user(self, username: str, password: str, role: UserRole):
        """Registers a new user if the username is not already taken."""
        if username in self.users:
            raise ValueError(f"Username '{username}' is already taken.")
        self.users[username] = User(username, password, role)

    def authenticate_user(self, username: str, password: str):
        """Authenticates the user and returns the User object if valid."""
        user = self.users.get(username)
        if user and user.check_password(password):
            return user
        return None

    def get_all_users(self):
        """Returns the list of existing users as a dictionary."""
        return {username: user.__dict__ for username, user in self.users.items()}