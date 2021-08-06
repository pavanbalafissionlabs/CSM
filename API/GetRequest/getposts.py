from flask import json, jsonify, send_from_directory
from API.model import User, Content
from flask import Blueprint

get_posts = Blueprint('get_posts', __name__)


@get_posts.route('/api', methods=['GET'])
def get_TotalPost():
    all_records = User.query.all()

    outer = []
    for i in range(len(all_records)):
        d = {}
        d['id'] = all_records[i].id
        d['Fullname'] = all_records[i].Fullname
        # d['password'] = all_records[i].password
        # d['Pincode'] = all_records[i].Pincode
        posts = Content.query.filter_by(author=all_records[i])
        postlist = []
        for j in posts:
            post = {}
            print(j.id)
            post['id'] = j.id
            post['Title'] = j.Title
            post['body'] = j.Body
            post['Summary'] = j.Summary
            post['Tags'] = json.loads(j.PostTags)
            post['File'] = j.Filename
            postlist.append(post)
        d['posts'] = postlist
        outer.append(d)
        print(outer)
    return jsonify(outer)


@get_posts.route('/post/all', methods=['GET'])
def get_post():
    all_post = Content.query.all()
    print(len(all_post))
    outer = []
    for i in range(len(all_post)):
        d = {}
        d['id'] = all_post[i].id
        d['Title'] = all_post[i].Title
        d['Body'] = all_post[i].Body
        d['Summary'] = all_post[i].Summary
        d['Tags'] = json.loads(all_post[i].PostTags)
        d['File'] = all_post[i].Filename
        d['Author'] = all_post[i].author.Fullname
        outer.append(d)
    print(outer)
    return jsonify(outer)


@get_posts.route('/user/post/download/<string:path>', methods=["GET"])
def downloadfile(path):
    print(path)
    return send_from_directory("static/documents/", path, as_attachment=True)
