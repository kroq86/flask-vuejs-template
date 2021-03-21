from flask import Flask, render_template, json, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return render_template('index.html', name='')


@app.route('/api')
def api():
    myDict = {"Title":ttile, 
              "Text":ttext}
    
    return json.dumps(myDict)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    text = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return self.text


def start():
    db.create_all()
    admin = Post(title='Как очищают воду? Экскурсия по КОС', 
                 text='Представители «Нижневартовских коммунальных систем» провели экскурсию по канализационно-очистным сооружениям города. Обо всех стадиях очистки и обеззараживания сточных вод специалисты рассказали журналистам, общественникам, представителям администрации и депутатам Думы города. Сточные воды проходят несколько этапов обработки, в среднем на весь процесс требуется порядка 18-ти часов. Начинается всё с механической очистки от мусора и песка, затем стоки разделяют на твердую и жидкую фракции и проводят очистку биологическую. В этом этапе  задействованы полезные бактерии.')
    db.session.add(admin)    
    db.session.commit()
    return Post.query.all()


kek = start ()
ttile = str(kek[0].title)
ttext = str(kek[0].text)


