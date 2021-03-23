from flask import Flask, render_template, json, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import PostForm
from flask import request




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


@app.route('/admin', methods=['POST','GET'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        # try:
        post = Post(title=title, text=body)
        db.session.add(post)
        db.session.commit()
        # except:
        #     print('error in Post')

    form = PostForm()
    return render_template('admin.html', form = form)    

@app.route('/')
def index_page():
    return render_template('index.html', name='')


@app.route('/api')
def api():
    myDict = {"Title":ttitle, 
              "Text":ttext,
              "Time":ttime}
    return json.dumps(myDict)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    text = db.Column(db.String(1500), unique=True, nullable=False)
    time = db.Column(db.DateTime, default = datetime.now())
    
    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)

    def __repr__(self):
        return self.text


# def start():
#     db.create_all()
#     admin = Post(title='Как очищают воду? Экскурсия по КОС', 
#                  text='Представители «Нижневартовских коммунальных систем» провели экскурсию по канализационно-очистным сооружениям города. Обо всех стадиях очистки и обеззараживания сточных вод специалисты рассказали журналистам, общественникам, представителям администрации и депутатам Думы города. Сточные воды проходят несколько этапов обработки, в среднем на весь процесс требуется порядка 18-ти часов. Начинается всё с механической очистки от мусора и песка, затем стоки разделяют на твердую и жидкую фракции и проводят очистку биологическую. В этом этапе  задействованы полезные бактерии.')
#     db.session.add(admin)    
#     db.session.commit()
#     return Post.query.all()


body = Post.query.all()
ttitle = str(body[0].title)
ttext = str(body[0].text)
ttime = str(body[0].time)


if __name__== "__main__":
    app.run(debug=True)