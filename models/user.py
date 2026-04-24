class User:
    def __init__(
        self,
        user_id=None,
        username=None,
        email=None,
        password_hash=None,
        display_name=None,
        bio=None,
        profile_picture_path=None,
        created_at=None,
        updated_at=None
    ):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.display_name = display_name
        self.bio = bio
        self.profile_picture_path = profile_picture_path
        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def from_db_row(row):
       
        if row is None:
            return None

        return User(
            user_id=row.get("user_id"),
            username=row.get("username"),
            email=row.get("email"),
            password_hash=row.get("password_hash"),
            display_name=row.get("display_name"),
            bio=row.get("bio"),
            profile_picture_path=row.get("profile_picture_path"),
            created_at=row.get("created_at"),
            updated_at=row.get("updated_at")
        )

    def __str__(self):
        return f"User({self.user_id}, {self.username}, {self.email})"