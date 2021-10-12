from flask import Flask, jsonify

app = Flask(__name__)


data = {
'course': 411,
'courseName': "Software in Telecommunications",
'releaseYear': 2021,
'courseActiv': True,
'droppedStudents': None,
'date': 20210218,
'someData': [[11,2],[22,4],[33,1],[44,5]],
'scores': {'a': 77,'b': 46,'c': 91}
}


@app.route('/')
def index():
    return "Akshaykumar Homework for week 7 "

@app.route("/data", methods=['GET'])
def get():
    return jsonify({'data':data})

@app.route('/scores', methods=['GET'])
def get_scores():
    return jsonify(data['scores'])








if __name__ == "__main__":
    app.run(debug=True)

