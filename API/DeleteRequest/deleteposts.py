from API import db, bcrypt
from flask import Flask, request, jsonify
from API.model import User, Content

from flask import Blueprint

delete_posts = Blueprint('delete', __name__)


@delete_posts.route('/post/delete/<id>', methods=['DELETE'])
def del_Post(id):
    try:
        user = User.query.filter_by(
            email=request.authorization.get('username')).first()
        if user and bcrypt.check_password_hash(user.password, request.authorization.get('password')):
            deletepost = Content.query.get(id)
            if user.email == deletepost.author.email:
                outer = []
                d = {}
                d['id'] = deletepost.id
                d['Title'] = deletepost.Title
                d['Body'] = deletepost.Body
                d['Summary'] = deletepost.Summary
                db.session.delete(deletepost)
                db.session.commit()
                outer.append(d)
                print(outer)
                return jsonify(outer), 200
            else:
                return jsonify({'error': "You can delete only your posts"})
        else:
            return jsonify({"error": "not authorized"})
    except Exception as e:
        a = {"error": "url not found or login with your account"}
        return jsonify(a), 404
