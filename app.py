from flask import Flask

from flask import *
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo

app = Flask('note_manage')
app.config['MONGO_URI'] = 'mongodb://localhost:27017/note_manage-db'

Bootstrap(app)
mongo = PyMongo(app)

@app.route('/',methods=['GET','POST'])
def note_saver():
    if request.method =='GET':
        print ('hi')
        doc=[x for x in mongo.db.NoteCollection.find({})]
        print(doc)
        return render_template('page.html', savedNotes=doc)
    elif request.method =='POST':
        doc={}
        print('hello')
        for item in request.form:
            doc[item]=request.form[item]
        print(doc)
        mongo.db.NoteCollection.insert_one(doc)
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
