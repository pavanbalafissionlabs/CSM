from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bdbe7e1621612f790a6c829de37379a5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///CMS.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from API.Search.searchposts import search_posts
from API.PostRequest.postpost import post_posts
from API.DeleteRequest.deleteposts import delete_posts
from API.GetRequest .getposts import get_posts
from API.UpdateRequest.updateposts import update_posts
from API.UserRegister.user_Register import user_register

app.register_blueprint(post_posts)
app.register_blueprint(delete_posts)
app.register_blueprint(get_posts)
app.register_blueprint(update_posts)
app.register_blueprint(user_register)
app.register_blueprint(search_posts)
