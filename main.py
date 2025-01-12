from flask import Flask, blueprints
from server.user import user

app = Flask(__name__)
app.register_blueprint(user)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')