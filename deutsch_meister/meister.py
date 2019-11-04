from flask import Flask, render_template
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/deutschMeisterDB"
app.config["MONGO_DBNAME"] = 'Words'
mongo = PyMongo(app)
db = mongo.db
col = mongo.db['Words']
col.insert_one({'aa': 'bb'})
print(mongo.db.Words.find_one())


@app.route('/')
def index():
#     # return render_template('index.html') 
    print(list(mongo.db.Words.find()))
    return str(list(mongo.db.Words.find()))
    # doc = mongo.db.words.insert({'aaa': 'aaa'})
    # return "Inserted"

# if __name__ == '__main__':
#   app.run(host='127.0.0.1', port=8000, debug=True)
 