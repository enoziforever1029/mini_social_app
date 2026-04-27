from flask import Blueprint, request, jsonify
from services.post_service import PostService

post_api = Blueprint("post_api", __name__)


@post_api.route("/posts", methods=["GET"])
def get_all_posts():
    success, message, posts = PostService.get_all_posts()

    return jsonify({
        "success": success,
        "message": message,
        "data": posts
    }), 200 if success else 500


@post_api.route("/posts/<int:post_id>", methods=["GET"])
def get_post_by_id(post_id):
    success, message, post = PostService.get_post_by_id(post_id)

    return jsonify({
        "success": success,
        "message": message,
        "data": post
    }), 200 if success else 404


@post_api.route("/posts/user/<int:user_id>", methods=["GET"])
def get_posts_by_user(user_id):
    success, message, posts = PostService.get_posts_by_user(user_id)

    return jsonify({
        "success": success,
        "message": message,
        "data": posts
    }), 200 if success else 400


@post_api.route("/posts", methods=["POST"])
def create_post():
    data = request.get_json()

    user_id = data.get("user_id")
    title = data.get("title")
    content = data.get("content", "")
    community_id = data.get("community_id")
    post_type = data.get("post_type", "text")

    success, message, post = PostService.create_post(
        user_id=user_id,
        title=title,
        content=content,
        community_id=community_id,
        post_type=post_type
    )

    return jsonify({
        "success": success,
        "message": message,
        "data": post.to_dict() if hasattr(post, "to_dict") else post
    }), 201 if success else 400


@post_api.route("/posts/<int:post_id>", methods=["PUT"])
def update_post(post_id):
    data = request.get_json()

    user_id = data.get("user_id")
    title = data.get("title")
    content = data.get("content", "")
    post_type = data.get("post_type", "text")

    success, message = PostService.update_post(
        post_id=post_id,
        user_id=user_id,
        title=title,
        content=content,
        post_type=post_type
    )

    return jsonify({
        "success": success,
        "message": message
    }), 200 if success else 400


@post_api.route("/posts/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    data = request.get_json()

    user_id = data.get("user_id")

    success, message = PostService.delete_post(
        post_id=post_id,
        user_id=user_id
    )

    return jsonify({
        "success": success,
        "message": message
    }), 200 if success else 400