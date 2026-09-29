from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/geodesy')
def geodesy():
    return render_template('geodesy.html')

@app.route('/geology')
def geology():
    return render_template('geology.html')

@app.route('/ecology')
def ecology():
    return render_template('ecology.html')

@app.route('/hydrology')
def hydrology():
    return render_template('hydrology.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/documents')
def documents():
    return render_template('documents.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name', '')
    phone = data.get('phone', '')
    email = data.get('email', '')
    services = data.get('services', [])
    message = data.get('message', '')
    
    print(f"Новая заявка: {name}, {phone}, {email}, Услуги: {services}, Сообщение: {message}")
    
    return jsonify({'status': 'success', 'message': 'Заявка отправлена'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
