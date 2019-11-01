# -*- coding: utf-8 -*-

from flask import Flask, request
import json
from utils.destinations import destinations
import swapi

app = Flask(__name__)

# POST: /api/starships/recommend
# =====================
# --------------------------------------------------
# Content-Type: application/json
#
# { "id": 6 }
# --------------------------------------------------
# Example response:
# --------------------------------------------------
# Content-Type: application/json
#
# { "alternatives": [ {starship 1}, {starship 2}, {starship 3} ...] }
# --------------------------------------------------

""" Write your API endpoint here """

# GET: /api/starships/
# =====================

@app.route('/api/starships', methods=['GET'])
def get_starships():
    try:
        starships = swapi.get_all("starships")
    except:
        response = {"error": "something went wrong"}

    return json.dumps(starships, default=lambda o: o.__dict__, indent=4)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
