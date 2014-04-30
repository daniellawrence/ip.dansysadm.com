#!/usr/bin/env python
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def get_my_ip():
    xip = request.headers.get('X-Forwarded-For')
    if xip:
        return jsonify({'ip': xip}), 200
        return jsonify({'ip': request.remote_addr}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')
