from flask import json, jsonify, send_from_directory, request
from API.model import User, Content
from flask import Blueprint

get_posts = Blueprint('get_posts', __name__)


@get_posts.route('/content', methods=['GET'])
def get_Content():

    all_posts = Content.query.all()

    result = []
    for i in range(len(all_posts)):
        dict = {}
        dict['id'] = all_posts[i].id
        dict['Title'] = all_posts[i].Title
        dict['Body'] = all_posts[i].Body
        dict['Summary'] = all_posts[i].Summary
        dict['Tags'] = json.loads(all_posts[i].PostTags)
        dict['File'] = all_posts[i].Filename
        dict['Author'] = all_posts[i].author.Fullname
        result.append(dict)
    print(result)
    return jsonify(result)


@get_posts.route('/download/<string:path>', methods=["GET"])
def downloadfile(path):
    return send_from_directory("static/documents/", path, as_attachment=True)
