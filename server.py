from flask import Flask, jsonify
from flask.templating import render_template
from flask_cors import CORS

app = Flask(__name__,
            static_folder='./front_vue/dist/static',
            template_folder='./front_vue/dist')

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/v1.0/mensaje')
def mensaje():
    return jsonify('Nuevo mensaje desde el servidor vue')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)

