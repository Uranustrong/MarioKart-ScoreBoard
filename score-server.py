from flask import Flask, request, abort, jsonify, send_from_directory, make_response, Response, session, render_template
from flask_cors import CORS
import pygsheets, os, re
import pandas as pd

app = Flask(__name__, static_folder="web/", static_url_path='')
CORS(app)

gc = pygsheets.authorize(service_file="./mariokart-credential.json")
sheets = dict(
    A=gc.open_by_url(f'https://docs.google.com/spreadsheets/d/1CsqSd8_76OR0TzE7HbpSjLAdDd-2WaHiLdfvMugAw68/edit?gid=856360843#gid=856360843'),
    B=gc.open_by_url(f'https://docs.google.com/spreadsheets/d/1-ZAHL2ic95nBDDcO8fsOLobVs872tHPffYkeA20OQXE/edit?gid=1490557090#gid=1490557090'),
)
worksheets = dict()

@app.route('/s/<group>/<match>')
def get(group, match):
    print(group, match)
    if group in sheets:
        sht = sheets[group]
    else:
        abort(400)
    if not re.fullmatch(r"[M|L]\d+", match):
        abort(400)
    key = f'{group} {match}'
    if key in worksheets:
        ws = worksheets[key]
    else:
        try:
            ws = sht.worksheet_by_title(match)
            worksheets[key] = ws
        except:
            abort(400)

    try:
        def parse_score(s):
            try:
                print(s)
                s = s + [None] * 4
                return dict(
                    id=s[0],
                    rank=int(s[2][1:]) if s[2] else None,
                    score=int(s[3]) if s[3] else None,
                )
            except:
                return None
        scores, maps = ws.get_values_batch(["C5:F8", "I5:"])
        scores = [parse_score(s) for s in scores]
        scores = [s for s in scores if s]
        maps = sum([i[::3] for i in maps[::6]], [])
        maps = len(maps)
    except Exception as e:
        print(e)
        abort(500)

    res = jsonify(scores=scores, maps=maps)
    return res

@app.route('/')
def home():
    return send_from_directory("web/", "index.html")

def run(): app.run(
    debug=True,
    host='0.0.0.0',
    port=os.getenv('PORT') or 4000
)
if __name__ == '__main__':
    run()