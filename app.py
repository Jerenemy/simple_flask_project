from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/')
def serve_frontend():
    return send_from_directory('static', 'index.html')

@app.route('/api/data')
def get_data():
    return jsonify({"message": "Hello from Flask"})

if __name__ == '__main__':
    app.run(debug=True)
    
    