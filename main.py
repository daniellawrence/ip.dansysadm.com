#!/usr/bin/env python
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def get_my_ip():
    ip = request.headers.get('X-Forwarded-For')
    if not ip:
        ip = request.remote_addr

    if 'json' in request.args:
        return jsonify({'ip': ip, 'cidr': '%s/32' % ip}), 200
    elif 'yaml' in request.args:
        return "---\nip: %s\ncidr: %s\32" % (ip, ip)
    elif 'plain' in request.args or 'txt' in request.args \
         or 'text' in request.args:
        return ip, 200
    elif 'bash' in request.args or 'zsh' in request.args \
         or 'ksh' in request.args:
        return "IP=%s" % ip, 200

    return jsonify({'ip': ip, 'cidr': '%s/32' % ip}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
#
