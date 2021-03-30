from flask import Flask, render_template, json, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import PostForm
from flask import request
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config ['TEMPLATES_AUTO_RELOAD'] = True
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)


@app.route('/admin', methods=['POST','GET'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        post = Post(title=title, text=body)
        db.session.add(post)
        db.session.commit()
    form = PostForm()
    return render_template('admin.html', form = form)    


@app.route('/')
def index_page():
    return render_template('index.html', name='')

@app.route('/post')
def post_page():
    return render_template('post.html', name='')


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    text = db.Column(db.String(1500), unique=True, nullable=False)
    time = db.Column(db.DateTime, default = datetime.now())
    
    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)

    def __repr__(self):
        return self.title


class PostSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "text", "time")
        
        
post_schema = PostSchema()
posts_schema = PostSchema(many=True)


class PostListResource(Resource):
    def get(self):
        posts = Post.query.all()
        return posts_schema.jsonify(posts)

    def post(self):
        new_post = Post(
            title=request.json['title'],
            content=request.json['text'],
            time=request.json['time']
        )
        db.session.add(new_post)
        db.session.commit()
        return post_schema.dump(new_post)
    
    
class PostResource(Resource):
    def get(self, post_id):
        post = Post.query.get_or_404(post_id)
        return post_schema.jsonify(post)

    def patch(self, post_id):
        post = Post.query.get_or_404(post_id)

        if 'title' in request.json:
            post.title = request.json['title']
        if 'text' in request.json:
            post.content = request.json['text']
        if 'time' in request.json:
            post.content = request.json['time']

        db.session.commit()
        return post_schema.dump(post)

    def delete(self, post_id):
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return '', 204
    

api.add_resource(PostListResource, '/posts')
api.add_resource(PostResource, '/posts/<int:post_id>')


if __name__== "__main__":
    app.run(debug=True)
    
    
