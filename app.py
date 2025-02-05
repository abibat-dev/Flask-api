from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)


@app.route('/')
def get_info():
    email = "olawalehabibat81@gmail.com"
    current_datetime = datetime.utcnow().isoformat() + "Z"

    github_url = "https://github.com/abibat-dev/flask_api"

    response = {
        "email": email,
        "current_datetime": current_datetime,
        "github_url": github_url
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
