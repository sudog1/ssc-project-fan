from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.plgtff3.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    nickname = request.form['nickname']
    comment = request.form['comment']
    doc = {
        'nickname': nickname,
        'comment': comment
    }
    db.fan.insert_one(doc)
    return jsonify({'msg': '저장 완료'})

@app.route("/guestbook", methods=["GET"])
def guestbook_get():
    fan = list(db.fan.find({}, {'_id': False}))
    return jsonify({'fan': fan})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)