from operator import contains
from flask import json, jsonify
from API.model import User, Content
from flask import Blueprint

search_posts = Blueprint('search_posts', __name__)


@search_posts.route("/posts/searchbytitle/<string:Title>")
def searchbyTitle(Title):
    data = Content.query.filter(Content.Title.contains(Title)).all()
    print(data)
    if data:
        l = []
        for i in data:
            print("i", i)
            d = {}
            d['id'] = i.id
            d['Title'] = i.Title
            d['Body'] = i.Body
            d['Summary'] = i.Summary
            d['PostTags'] = json.loads(i.PostTags)
            d['Author'] = i.author.Fullname
            l.append(d)
        return jsonify(l), 200
    else:
        return jsonify({"Sucess": f"No post avaible with this title '{Title}'"}), 404


@search_posts.route("/posts/searchbybody/<string:Body>")
def searchbyBody(Body):
    print("body", Body)
    data = Content.query.filter(Content.Body.contains(Body)).all()
    # print(data)
    if data:
        l = []
        for i in data:
            print("i", i)
            d = {}
            d['id'] = i.id
            d['Title'] = i.Title
            d['Body'] = i.Body
            d['Summary'] = i.Summary
            d['PostTags'] = json.loads(i.PostTags)
            d['Author'] = i.author.Fullname
            l.append(d)
        return jsonify(l), 200
    else:
        return jsonify({"Sucess": f"No post avaible with this title '{Body}'"}), 404


@search_posts.route("/posts/searchbyTags/<string:PostTags>")
def searchbyTags(PostTags):
    # print("body", Body)
    data = Content.query.filter(Content.PostTags.contains(PostTags)).all()
    # print(data)
    if data:
        l = []
        for i in data:
            print("i", i)
            d = {}
            d['id'] = i.id
            d['Title'] = i.Title
            d['Body'] = i.Body
            d['Summary'] = i.Summary
            d['PostTags'] = json.loads(i.PostTags)
            d['Author'] = i.author.Fullname
            l.append(d)
        return jsonify(l), 200
    else:
        return jsonify({"Sucess": f"No post avaible with this title '{PostTags}'"}), 404


@search_posts.route("/posts/Searchbyauthor/<string:Fullname>")
def searchbyAuthor(Fullname):
    data = User.query.filter(User.Fullname.contains(Fullname)).all()
    print(data)
    if data:
        l = []
        for i in data:
            content = Content.query.filter_by(author=i)
            for j in content:
                d = {}
                d['id'] = j.id
                d['Title'] = j.Title
                d['Body'] = j.Body
                d['Summary'] = j.Summary
                d['Filename'] = j.Filename
                d['PostTags'] = json.loads(j.PostTags)
                d['author'] = j.author.Fullname
                l.append(d)
            print("i", i)
        return jsonify(l), 200
    else:
        return jsonify({"Sucess": f"No post avaible with this email '{Fullname}'"}), 404
