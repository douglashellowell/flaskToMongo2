# import flask and mongodb tools
from flask import Flask, request
from bson.json_util import dumps
from flask import jsonify
from flask_pymongo import PyMongo

# setup app as flask server
app = Flask(__name__)
# config to look at hosted mongodb database
app.config["MONGO_URI"] = "mongodb://localhost:27017/testrun"
mongo = PyMongo(app)

# On root request
@app.route('/', methods=['GET', 'POST'])
def home():
    print('request made to root')
    dougs_collection = mongo.db.collectionone

    if request.method == 'GET':
        print('Get request made!')
        # point to 'collectionone' collection
        output = []
        for item in dougs_collection.find():
            item['_id'] = str(item['_id'])
            output.append(item)
        return jsonify({'result': output})
    elif request.method == 'POST':
        try:
            data_to_post = request.json
            print('VVVVVVVVVVVVVV')
            print(data_to_post.target_room)
            print('^^^^^^^^^^^^^^')
            print('trying to post data...')
            dougs_collection.update_one(
                filter={'roomName': data_to_post.target_room},
                update={'$push': {data_to_post.questions_to_add}}
            )

        except:
            print('failed to add data! :(')
        finally:
            print('request ended')


#     request.args: the key/value pairs in the URL query string

#     request.form: the key/value pairs in the body, from a HTML post form, or JavaScript request that isn't JSON encoded

#     request.files: the files in the body, which Flask keeps separate from form. HTML forms must use enctype=multipart/form-data or files will not be uploaded.

#     request.values: combined args and form, preferring args if keys overlap

#     request.json: parsed JSON data. The request must have the application/json content type, or use request.get_json(force=True) to ignore the content type.

# All of these are MultiDict instances (except for json). You can access values using:

#     request.form['name']: use indexing if you know the key exists

#     request.form.get('name'): use get if the key might not exist

#     request.form.getlist('name'): use getlist if the key is sent multiple times and you want a list of values. get only returns the first value.
