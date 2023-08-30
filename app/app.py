import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/healthz', methods=['GET'])
def readiness_probe():
    return 'OK', 200


@app.route('/hostname', methods=['GET'])
def get_hostname():
    hostname = socket.gethostname()
    return jsonify({'hostname': hostname})


@app.route('/author', methods=['GET'])
def get_author():
    author = os.environ.get('AUTHOR')
    return jsonify({'author': author})


@app.route('/id', methods=['GET'])
def get_uuid():
    uuid = os.environ.get('UUID')
    return jsonify({'uuid': uuid})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
