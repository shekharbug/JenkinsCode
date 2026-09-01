from flask import Flask
import subprocess
import os

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'Hello from Jenkins + Docker CI/CD!'

@app.route('/health')
def health():
    return {'status': 'Healthy'}, 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
