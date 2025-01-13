from flask import Flask, blueprints
from server.routes.user import user
from server.routes.category import category
from server.routes.record import record

app = Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(category)
app.register_blueprint(record)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')