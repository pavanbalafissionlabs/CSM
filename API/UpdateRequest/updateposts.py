from API.model import User, Content
from API import db, bcrypt
from flask import request, jsonify
from werkzeug.utils import secure_filename
from flask import Blueprint
import os
from API import app
import json
update_posts = Blueprint('update_posts', __name__)


@update_posts.route('/content/<id>', methods=['PUT'])
def EditContent(id):
    user = User.query.filter_by(
        email=request.authorization.get('username')).first()
    try:
        if user and bcrypt.check_password_hash(user.password, request.authorization.get('password')):
            editpost = Content.query.get(id)
            if user.email == editpost.author.email:
                editpost.Title = request.json.get(
                    'Title') if request.json.get('Title') else editpost.Title
                editpost.Body = request.json.get(
                    'Body') if request.json.get('Body') else editpost.Body
                editpost.Summary = request.json.get(
                    'Summary') if request.json.get('Summary') else editpost.Summary
                editpost.PostTags = json.dumps(request.json.get(
                    'PostTags'))if request.json.get('PostTags') else editpost.PostTags
                db.session.commit()
                return jsonify({'Title': editpost.Title, 'Body': editpost.Body, "Summary": editpost.Summary,
                                "PostTags": json.loads(editpost.PostTags), "author": editpost.author.email}), 200
            else:
                return jsonify({'error': "You can edit only your posts"})
        else:
            return jsonify({"error": "not authorized"}), 401
    except Exception as e:
        error = {"Required": {
            "Title": "Should be title",
            "Body": "Should be Body",
            "summary": "Summary "},
            "Optional": {
            "Tags": "Tags"
        }
        }
        return jsonify(error), 404


@update_posts.route('/uploadDocument/<id>', methods=['PUT'])
def uploadDocument(id):
    editpost = Content.query.get(id)
    try:
        file = request.files['file']
        filename = secure_filename(file.filename)
        print("filename", filename,)
        path = os.path.join('API/static/documents/', filename)
        file.save(path)
        editpost.Filename = "localhost:5000/user/post/download/"+filename
        db.session.commit()
        return jsonify({"uploaded": True, "filename": editpost.Filename}), 200
    except Exception as e:

        error = {"error": "file not found"}
        return jsonify(error), 404
