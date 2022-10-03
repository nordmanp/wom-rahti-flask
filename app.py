import os
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    ret = { 
        'msg': 'GitHub Webhook deployment works!', 
        'env': os.environ.get('ENV_VAR', 'Cannot find variable ENV_VAR') 
    }

    return ret


if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')

###http://flask-test-nordmanp.rahtiapp.fi/