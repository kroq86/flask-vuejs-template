# Flask_VUE

App Used a uniqe Delimeters [[VUE]] and {{FLASK}} 

# Features
* Flask Rest
* Flask SQLalchemy
* Flask Marshmallow

## Application Structure

### Rest Api

jsonify SQL and send via API at frontend VUE

![VUE](https://user-images.githubusercontent.com/29804069/111898146-fef86400-8a45-11eb-87b3-001912d1211b.png)

#### Client Application

Fetch from VUE, but can use Axios

CSS is Bootstrap 4 from cdn

VUE load from CDN and script read at index.html/ FLASK local load JS files

API is a path /posts for all, or /post/1 for id, dictionary from Flask model Post

![API](https://user-images.githubusercontent.com/29804069/111898150-061f7200-8a46-11eb-82d0-9dc8b1a90c73.png)

#### CRUD
/admin path for add new post, use app DB Browser for SQLite

###### HOW TO RUN 
``` bash
cd Snews
pip3 install requirements.txt
export FLASK_APP=run.py 
flask run

