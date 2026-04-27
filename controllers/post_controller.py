from services.post_service import PostService


class PostController:

    @staticmethod
    def create_post(user_id, title, content, community_id=None):
        return PostService.create_post(
            user_id=user_id,
            title=title,
            content=content,
            community_id=community_id,
            post_type="text"
        )
        
    @staticmethod
    def get_all_posts():
        return PostService.get_all_posts()