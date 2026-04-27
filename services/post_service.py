from database import get_connection
from models.post import Post


class PostService:
    @staticmethod
    def create_post(user_id, title, content="", community_id=None, post_type="text"):
        if not user_id:
            return False, "User ID is required.", None

        if not title or not title.strip():
            return False, "Post title is required.", None

        post = Post(
            user_id=user_id,
            community_id=community_id,
            title=title.strip(),
            content=content.strip() if content else "",
            post_type=post_type
        )

        if not post.is_valid_post_type():
            return False, "Invalid post type.", None

        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)

            sql = """
                INSERT INTO posts (
                    user_id,
                    community_id,
                    title,
                    content,
                    post_type
                )
                VALUES (%s, %s, %s, %s, %s)
            """

            cursor.execute(
                sql,
                (
                    post.user_id,
                    post.community_id,
                    post.title,
                    post.content,
                    post.post_type
                )
            )

            conn.commit()
            post.post_id = cursor.lastrowid

            return True, "Post created successfully.", post

        except Exception as e:
            return False, f"Failed to create post: {e}", None

        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

    @staticmethod
    def get_all_posts():
        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)

            sql = """
                SELECT 
                    posts.post_id,
                    posts.user_id,
                    users.username,
                    posts.community_id,
                    communities.name AS community_name,
                    posts.title,
                    posts.content,
                    posts.post_type,
                    posts.created_at,
                    posts.updated_at
                FROM posts
                INNER JOIN users 
                    ON posts.user_id = users.user_id
                LEFT JOIN communities 
                    ON posts.community_id = communities.community_id
                ORDER BY posts.created_at DESC
            """

            cursor.execute(sql)
            posts = cursor.fetchall()

            return True, "Posts retrieved successfully.", posts

        except Exception as e:
            return False, f"Failed to retrieve posts: {e}", []

        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

    @staticmethod
    def get_post_by_id(post_id):
        if not post_id:
            return False, "Post ID is required.", None

        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)

            sql = """
                SELECT 
                    posts.post_id,
                    posts.user_id,
                    users.username,
                    posts.community_id,
                    communities.name AS community_name,
                    posts.title,
                    posts.content,
                    posts.post_type,
                    posts.created_at,
                    posts.updated_at
                FROM posts
                INNER JOIN users 
                    ON posts.user_id = users.user_id
                LEFT JOIN communities 
                    ON posts.community_id = communities.community_id
                WHERE posts.post_id = %s
            """

            cursor.execute(sql, (post_id,))
            post = cursor.fetchone()

            if post is None:
                return False, "Post not found.", None

            return True, "Post retrieved successfully.", post

        except Exception as e:
            return False, f"Failed to retrieve post: {e}", None

        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

    @staticmethod
    def get_posts_by_user(user_id):
        if not user_id:
            return False, "User ID is required.", []

        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)

            sql = """
                SELECT 
                    post_id,
                    user_id,
                    community_id,
                    title,
                    content,
                    post_type,
                    created_at,
                    updated_at
                FROM posts
                WHERE user_id = %s
                ORDER BY created_at DESC
            """

            cursor.execute(sql, (user_id,))
            posts = cursor.fetchall()

            return True, "User posts retrieved successfully.", posts

        except Exception as e:
            return False, f"Failed to retrieve user posts: {e}", []

        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

    @staticmethod
    def update_post(post_id, user_id, title, content="", post_type="text"):
        if not post_id:
            return False, "Post ID is required."

        if not user_id:
            return False, "User ID is required."

        if not title or not title.strip():
            return False, "Post title is required."

        post_model = Post(
            post_id=post_id,
            user_id=user_id,
            title=title.strip(),
            content=content.strip() if content else "",
            post_type=post_type
        )

        if not post_model.is_valid_post_type():
            return False, "Invalid post type."

        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)

            check_sql = """
                SELECT user_id
                FROM posts
                WHERE post_id = %s
            """

            cursor.execute(check_sql, (post_id,))
            post = cursor.fetchone()

            if post is None:
                return False, "Post not found."

            if post["user_id"] != user_id:
                return False, "You are not allowed to edit this post."

            update_sql = """
                UPDATE posts
                SET title = %s,
                    content = %s,
                    post_type = %s
                WHERE post_id = %s
            """

            cursor.execute(
                update_sql,
                (
                    post_model.title,
                    post_model.content,
                    post_model.post_type,
                    post_model.post_id
                )
            )

            conn.commit()

            return True, "Post updated successfully."

        except Exception as e:
            return False, f"Failed to update post: {e}"

        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

    @staticmethod
    def delete_post(post_id, user_id):
        if not post_id:
            return False, "Post ID is required."

        if not user_id:
            return False, "User ID is required."

        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)

            check_sql = """
                SELECT user_id
                FROM posts
                WHERE post_id = %s
            """

            cursor.execute(check_sql, (post_id,))
            post = cursor.fetchone()

            if post is None:
                return False, "Post not found."

            if post["user_id"] != user_id:
                return False, "You are not allowed to delete this post."

            delete_sql = """
                DELETE FROM posts
                WHERE post_id = %s
            """

            cursor.execute(delete_sql, (post_id,))
            conn.commit()

            return True, "Post deleted successfully."

        except Exception as e:
            return False, f"Failed to delete post: {e}"

        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass