import jwt, time, os
from flask import Flask, request

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

private_key = open('priv.txt').read()
public_key = open('pub.txt').read()
flag = open('flag.txt').read()

@app.route("/get_token")
def get_token():
    return app.encode({'admin': False, 'now': time.time()}, private_key, algorithm='RS256')

@app.route("/get_flag", methods=['POST'])
def get_flag():
  try:
    payload = app.decode(request.form['jwt'], public_key, algorithms=['RS256'])
    if payload['admin']:
      return flag
  except:
    return ":("

@app.route("/")
def sauce():
  return "%s" % open(__file__).read()

if __name__ == "__main__":
  app.run(host="0.0.0.0")