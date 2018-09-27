#!/usr/bin/python3

import os
import requests
import re
from flask import Flask, redirect

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return redirect("https://junkmail.valentin-deville.eu/domains/list", code=302)

@app.route('/domain/<domain>')
def check_domain(domain):
    try:
        list_json = requests.get("https://junkmail.valentin-deville.eu/domains/list")
        list_json.raise_for_status()
        list_domains = list_json.json()
        for domain_nb in list_domains:
            if re.match("^" + domain + "$", list_domains[domain_nb]):
                return 'JUNK\n', 200
        return 'NOT JUNK\n', 200
    except:
        return "Failed to get domain list from API.\n"

@app.route('/')
def home():
    return redirect("https://junkmail.valentin-deville.eu/domains/list", code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
