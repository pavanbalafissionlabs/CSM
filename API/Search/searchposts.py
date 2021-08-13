from operator import contains
from os import error
from flask import json, jsonify, request
from API.model import User, Content
from flask import Blueprint

search_posts = Blueprint('search_posts', __name__)


@search_posts.route('/search', methods=["GET"])
def Search():
    data = Content.query.all()

    if not request.args:

        message = {
            "Message": "use only query params",
            "help": "/search?Title=<Your search title>&Body=<Your search Body>&Tags=<Your Tags>",
            "Title": "/search?Title=<Your Title>",
            "Body": "/search?Body=<Your Body>",
            "Tags": "/search?Tags=<Your Tags>"
        }
        return message
    Title = request.args.get('Title')
    Body = request.args.get('Body')
    Tags = request.args.get('Tags')

    result = []
    if request.args.get('Title') and request.args.get('Body') and request.args.get('Tags'):
        for i in range(len(data)):

            if Title in data[i].Title:

                dict = {}
                dict['id'] = data[i].id
                dict['Title'] = data[i].Title
                dict['Body'] = data[i].Body
                dict['Summary'] = data[i].Summary
                dict['Filename'] = data[i].Filename
                dict['PostTags'] = json.loads(data[i].PostTags)
                dict['author'] = data[i].author.Fullname
                result.append(dict)
            elif data[i] not in result:
                if Body in data[i].Body:
                    dict = {}
                    dict['id'] = data[i].id
                    dict['Title'] = data[i].Title
                    dict['Body'] = data[i].Body
                    dict['Summary'] = data[i].Summary
                    dict['Filename'] = data[i].Filename
                    dict['PostTags'] = json.loads(data[i].PostTags)
                    dict['author'] = data[i].author.Fullname
                    result.append(dict)

            elif data[i] not in result:
                if Tags in data[i].PostTags:
                    dict = {}
                    dict['id'] = data[i].id
                    dict['Title'] = data[i].Title
                    dict['Body'] = data[i].Body
                    dict['Summary'] = data[i].Summary
                    dict['Filename'] = data[i].Filename
                    dict['PostTags'] = json.loads(data[i].PostTags)
                    dict['author'] = data[i].author.Fullname
                    result.append(dict)

    elif request.args.get('Body') and request.args.get('Tags'):
        for i in range(len(data)):

            if Body in data[i].Body:

                dict = {}
                dict['id'] = data[i].id
                dict['Title'] = data[i].Title
                dict['Body'] = data[i].Body
                dict['Summary'] = data[i].Summary
                dict['Filename'] = data[i].Filename
                dict['PostTags'] = json.loads(data[i].PostTags)
                dict['author'] = data[i].author.Fullname
                result.append(dict)
            elif data[i] not in result:
                if Tags in data[i].PostTags:
                    dict = {}
                    dict['id'] = data[i].id
                    dict['Title'] = data[i].Title
                    dict['Body'] = data[i].Body
                    dict['Summary'] = data[i].Summary
                    dict['Filename'] = data[i].Filename
                    dict['PostTags'] = json.loads(data[i].PostTags)
                    dict['author'] = data[i].author.Fullname
                    result.append(dict)
    elif request.args.get('Title') and request.args.get('Tags'):
        for i in range(len(data)):

            if Title in data[i].Title:

                dict = {}
                dict['id'] = data[i].id
                dict['Title'] = data[i].Title
                dict['Body'] = data[i].Body
                dict['Summary'] = data[i].Summary
                dict['Filename'] = data[i].Filename
                dict['PostTags'] = json.loads(data[i].PostTags)
                dict['author'] = data[i].author.Fullname
                result.append(dict)
            elif data[i] not in result:
                if Tags in data[i].PostTags:
                    dict = {}
                    dict['id'] = data[i].id
                    dict['Title'] = data[i].Title
                    dict['Body'] = data[i].Body
                    dict['Summary'] = data[i].Summary
                    dict['Filename'] = data[i].Filename
                    dict['PostTags'] = json.loads(data[i].PostTags)
                    dict['author'] = data[i].author.Fullname
                    result.append(dict)

    elif request.args.get('Title') and request.args.get('Body'):
        for i in range(len(data)):

            if Title in data[i].Title:

                dict = {}
                dict['id'] = data[i].id
                dict['Title'] = data[i].Title
                dict['Body'] = data[i].Body
                dict['Summary'] = data[i].Summary
                dict['Filename'] = data[i].Filename
                dict['PostTags'] = json.loads(data[i].PostTags)
                dict['author'] = data[i].author.Fullname
                result.append(dict)
            elif data[i] not in result:
                if Body in data[i].Body:
                    dict = {}
                    dict['id'] = data[i].id
                    dict['Title'] = data[i].Title
                    dict['Body'] = data[i].Body
                    dict['Summary'] = data[i].Summary
                    dict['Filename'] = data[i].Filename
                    dict['PostTags'] = json.loads(data[i].PostTags)
                    dict['author'] = data[i].author.Fullname
                    result.append(dict)

    elif request.args.get('Title'):
        for i in range(len(data)):

            if Title in data[i].Title:

                dict = {}
                dict['id'] = data[i].id
                dict['Title'] = data[i].Title
                dict['Body'] = data[i].Body
                dict['Summary'] = data[i].Summary
                dict['Filename'] = data[i].Filename
                dict['PostTags'] = json.loads(data[i].PostTags)
                dict['author'] = data[i].author.Fullname
                result.append(dict)

    elif request.args.get('Body'):
        for i in range(len(data)):

            if Body in data[i].Body:

                dict = {}
                dict['id'] = data[i].id
                dict['Title'] = data[i].Title
                dict['Body'] = data[i].Body
                dict['Summary'] = data[i].Summary
                dict['Filename'] = data[i].Filename
                dict['PostTags'] = json.loads(data[i].PostTags)
                dict['author'] = data[i].author.Fullname
                result.append(dict)

    elif request.args.get('Tags'):
        for i in range(len(data)):
            if Tags in data[i].PostTags:

                dict = {}
                dict['id'] = data[i].id
                dict['Title'] = data[i].Title
                dict['Body'] = data[i].Body
                dict['Summary'] = data[i].Summary
                dict['Filename'] = data[i].Filename
                dict['PostTags'] = json.loads(data[i].PostTags)
                dict['author'] = data[i].author.Fullname
                result.append(dict)

        return jsonify(result)
