from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

all_heroes = [
    {'id': 11, 'name': 'Dr Nice'},
    {'id': 12, 'name': 'Narco'},
    {'id': 13, 'name': 'Bombasto'},
    {'id': 14, 'name': 'Celeritas'},
    {'id': 15, 'name': 'Magneta'},
    {'id': 16, 'name': 'RubberMan'},
    {'id': 17, 'name': 'Dynama'},
    {'id': 18, 'name': 'Dr IQ'},
    {'id': 19, 'name': 'Magma'},
    {'id': 20, 'name': 'Tornado'}
]

@app.route('/heroes', methods=['GET'])
def heroes():
    name = request.args.get('name', '').strip().lower()
    if name:
        filtered_heroes = [hero for hero in all_heroes if name in hero['name'].lower()]
        return jsonify(filtered_heroes)
    return jsonify(all_heroes)

@app.route('/detail/<id>', methods=['GET'])
def detail(id):
    for x in all_heroes:
        if int(x['id']) == int(id):
            return jsonify(x)
    return "Record not found", 400

@app.route('/update', methods=['POST'])
def update():
    data = request.get_json()
    for x in all_heroes:
        if x['id'] == data['id']:
            x['name'] = data['name']
            return jsonify(x)
    return "Not found", 400

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    new_id = max(hero['id'] for hero in all_heroes) + 1
    new_hero = {'id': new_id, 'name': data['name']}
    all_heroes.append(new_hero)
    return jsonify(new_hero), 201

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    global all_heroes
    all_heroes = [hero for hero in all_heroes if hero['id'] != id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
