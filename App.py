from flask import *
import pymongo
import restHandlers as rh

client = pymongo.MongoClient(host="localhost")

db = client.get_database('test1')

app = Flask(__name__)

note = rh.MongoCrud(db.note)

index_page_data = {"numbers": [1, 2, 3, 4, 5], "msg": "Value from Flask"}

@app.route('/')
def index_page():
    return render_template('index.html', data=index_page_data)


@app.route('/note/', methods=['GET'])
@app.route('/note/<note_id>', methods=['GET'])
def read_note(note_id=None):
    return note.read(note_id)


@app.route('/note/', methods=['POST'])
def create_note():
    return note.create(request.data)


@app.route('/note/<note_id>', methods=['PUT'])
def update_note(note_id):
    return note.update(note_id, request.data)


@app.route('/note/<note_id>', methods=['DELETE'])
def delete_note(note_id):
    return note.delete(note_id)


@app.route('/note/drop', methods=['DELETE'])
def drop_note():
    return note.drop()


if __name__ == "__main__":
    app.run(debug=True)

