from flask import Flask, render_template, g, jsonify
import sqlite3
from dbdati import sodien, varda_datums, mekle_pec_burtiem, mekle_pec_burtiem2


DATUBAZE = "vardi.db"

app = Flask('app')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATUBAZE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def hello_world():
  return render_template("index.html")

@app.route('/meklesana')
def meklesana():
  return render_template("meklesana.html")


@app.route('/api/vardi/sodien')
def sodienas_vardi():
  cur = get_db().cursor()
  vardi = sodien(cur)
  return jsonify(vardi)


@app.route('/api/vardi/mekle/<vards>')
def mekle_vardu(vards):
  cur = get_db().cursor()
  datums = varda_datums(cur, vards)
  return jsonify(datums)


@app.route('/api/vardi/lidzigi/<burti>')
def mekle_lidzigus(burti):
  cur = get_db().cursor()
  vardi = mekle_pec_burtiem(cur, burti)
  return jsonify(vardi)


@app.route('/api/vardi/lidzigi/<sakums>/<beigas>')
def mekle_lidzigus2(sakums, beigas):
  cur = get_db().cursor()
  vardi = mekle_pec_burtiem2(cur, sakums, beigas)
  return jsonify(vardi)


@app.route('/api/vardi/test')
def test_vardi():
  cur = get_db().cursor()
  # cur.execute('SELECT vards FROM vardadienas LIMIT 1')
  # vards = cur.fetchone()
  vardi = sodien(cur)
  print(vardi)
  return jsonify(vardi)



app.run(host='0.0.0.0', port=8080)
