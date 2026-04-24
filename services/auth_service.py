import hashlib
from database import get_connection
from models.user import User


class AuthService:
    @staticmethod
    def hash_password(password):
     
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def register_user(username, email, password):
       
        if not username or not email or not password:
            return False, "All fields are required."

        password_hash = AuthService.hash_password(password)

        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)

            # Check if username or email already exists
            check_sql = """
                SELECT * FROM users
                WHERE username = %s OR email = %s
            """
            cursor.execute(check_sql, (username, email))
            existing_user = cursor.fetchone()

            if existing_user:
                return False, "Username or email already exists."

            # Insert new user
            insert_sql = """
                INSERT INTO users (
                    username,
                    email,
                    password_hash,
                    display_name
                )
                VALUES (%s, %s, %s, %s)
            """

            cursor.execute(
                insert_sql,
                (username, email, password_hash, username)
            )

            conn.commit()

            return True, "Account registered successfully."

        except Exception as e:
            return False, f"Registration failed: {e}"

        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

    @staticmethod
    def login_user(username, password):
    
        if not username or not password:
            return False, "Username and password are required.", None

        password_hash = AuthService.hash_password(password)

        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)

            sql = """
                SELECT * FROM users
                WHERE username = %s AND password_hash = %s
            """

            cursor.execute(sql, (username, password_hash))
            row = cursor.fetchone()

            if row is None:
                return False, "Invalid username or password.", None

            user = User.from_db_row(row)

            return True, "Login successful.", user

        except Exception as e:
            return False, f"Login failed: {e}", None

        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass