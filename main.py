#!/usr/bin/env python
from flask import Flask
from flask import request
from flask import jsonify
from collections import defaultdict
import random

app = Flask(__name__)

KNOWN_IPS = defaultdict(str)

@app.route("/")
def get_my_ip():
    ip = request.headers.get('X-Forwarded-For')
    changed = None
    if not ip:
        ip = request.remote_addr

    if 'key' in request.args:
        key = request.args.get('key')
    else:
        key = random.randint(0, 10000)

    old_ip = KNOWN_IPS[key]
    KNOWN_IPS[key] = ip
    if old_ip == ip:
        changed = False
    else:
        changed = True



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

    return jsonify({
        'ip': ip, 
        'cidr': '%s/32' % ip,
        'key': key,
        'old_ip': old_ip,
        'changed': changed
    }
    ), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
#
