from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/saludo', methods=['GET'])
def obtener_saludo():
    return jsonify({'mensaje': 'Hola, esta es mi API Flask!'})

if __name__ == '__main__':
    app.run(debug=True)
    