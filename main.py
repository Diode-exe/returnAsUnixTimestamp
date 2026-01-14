import datetime
from flask import Flask

app = Flask(__name__)

@app.route("/time")
def hello_world():
    now = datetime.datetime.now()
    res = str(now.timestamp())
    return res

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')