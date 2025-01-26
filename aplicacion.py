# pip install Flask
# python app.py
# http://127.0.0.1:5000/
# http://127.0.0.1:5000/contacto
# http://127.0.0.1:5000/saludo
# http://127.0.0.1:5000/info

from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('bootresponsive/bootresponsive.html')

@app.route('/contactos')
def contactos():
    return render_template('contactos.html')

@app.route('/menu')
def menu():
    return render_template('Menu/menu.html')

@app.route('/flexbox')
def flexbox():
    return render_template('Flexbox/flexbox.html')

@app.route('/halloween')
def halloween():
    return render_template('Halloween/halloween.html')

@app.route('/goku')
def goku():
    return render_template('Goku/goku.html')

@app.route('/animacion')
def animacion():
    return render_template('Animacion/animacion.html')

@app.route('/iframe')
def iframe():
    return render_template('Animacion/iframe.html')

@app.route('/menu2')
def menu2():
    return render_template('bootstrap/menu.html')

@app.route('/info', methods=['GET'])
def obtener_info():
    return jsonify([{'nombre': 'Federico Rico'},{'nombre': 'Pedro'}])

if __name__ == '__main__':
    app.run(debug=True)