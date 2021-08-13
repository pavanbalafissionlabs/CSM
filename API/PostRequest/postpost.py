
from API.model import User, Content
from API import db, bcrypt
from flask import request, jsonify
import json

from flask import Blueprint

post_posts = Blueprint('posts', __name__)


@post_posts.route('/addcontent', methods=['POST'])
def add_Post():
    user = User.query.filter_by(
        email=request.authorization.get('username')).first()
    print(user)
    print(request.authorization.get('password'), user.password)
    try:
        if user and bcrypt.check_password_hash(user.password, request.authorization.get('password')):

            Title = request.json.get('Title')
            Body = request.json['Body']
            Summary = request.json['Summary']

            PostTags = request.json.get('Tags')
            posts = Content(Title=Title, Body=Body, Summary=Summary,
                            PostTags=json.dumps(PostTags), author=user, Filename="none")
            db.session.add(posts)
            db.session.commit()
            return jsonify({'Title': posts.Title, 'Body': posts.Body, "Summary": posts.Summary, "PostTags": json.loads(posts.PostTags), "Id": posts.id}), 201
        else:
            return jsonify({"error": "not authorized"})
    except Exception as e:
        print(e)
        a = {"Required": {
             "Title": "Should be title",
             "Body": "Should be Body",
             "summary": "Summary "},
             "Optional": {
                 "Tags": "Tags"}
             }
        return jsonify(a), 404


@post_posts.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']

    user = User.query.filter_by(email=email).first()
    print(user)
    if (user and bcrypt.check_password_hash(user.password, password)):

        all_post = user.post
        get_yourPosts = []
        for user in all_post:
            results = {}
            results["Title"] = user.Title
            results["Body"] = user.Body
            results["Summary"] = user.Summary
            get_yourPosts.append(results)
        return jsonify(get_yourPosts), 200
    else:
        return jsonify({"login": "you login details are invalid",
                        "required": {"email": "enter a valid user name",
                                     "password": "enter a valid password"}}), 404
