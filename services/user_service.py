from database import get_connection
from models.user import User


class UserService:

    @staticmethod
    def get_user_by_id(user_id):
        if not user_id:
            return False, "User ID is required.", None

        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)

            sql = """
                SELECT *
                FROM users
                WHERE user_id = %s
            """

            cursor.execute(sql, (user_id,))
            row = cursor.fetchone()

            if row is None:
                return False, "User not found.", None

            user = User.from_db_row(row)

            return True, "User retrieved successfully.", user

        except Exception as e:
            return False, f"Failed to retrieve user: {e}", None

        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

    @staticmethod
    def update_profile(user_id, display_name, bio):
        if not user_id:
            return False, "User ID is required."

        display_name = display_name.strip() if display_name else ""
        bio = bio.strip() if bio else ""

        if not display_name:
            return False, "Display name is required."

        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)

            sql = """
                UPDATE users
                SET display_name = %s,
                    bio = %s
                WHERE user_id = %s
            """

            cursor.execute(sql, (display_name, bio, user_id))
            conn.commit()

            if cursor.rowcount == 0:
                return False, "User not found or no changes made."

            return True, "Profile updated successfully."

        except Exception as e:
            return False, f"Failed to update profile: {e}"

        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

    @staticmethod
    def upload_profile_picture(user_id, profile_picture_path):
        if not user_id:
            return False, "User ID is required."

        if not profile_picture_path:
            return False, "Profile picture path is required."

        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)

            sql = """
                UPDATE users
                SET profile_picture_path = %s
                WHERE user_id = %s
            """

            cursor.execute(sql, (profile_picture_path, user_id))
            conn.commit()

            if cursor.rowcount == 0:
                return False, "User not found or no changes made."

            return True, "Profile picture updated successfully."

        except Exception as e:
            return False, f"Failed to update profile picture: {e}"

        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass