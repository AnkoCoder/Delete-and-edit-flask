import json
from flask import render_template
from flask import request
from flask import Flask
from flask import redirect
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def items():
    with open('db.txt', 'r') as f:
        items = json.load(f)
        if request.method == 'POST':
            item = request.form['item']
            quantity = request.form['quantity']
            items.update({item: quantity})
            with open('db.txt', 'w') as f2:
                json.dump(items, f2)
        return render_template('post.html', items=items)


@app.route('/remove_items', methods=['GET', 'POST'])
def remove_items():
    with open('db.txt', 'r') as f:
        items = json.load(f)
        if request.method == 'POST':
            item = request.form['item']
            del items[item]
            with open('db.txt', 'w') as f2:
                json.dump(items, f2)
        return render_template('remove.html', items=items)


