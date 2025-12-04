from flask import Flask
from config import Config
from models.main_routers_db import *
from models.imp import db

app = Flask(__name__)
app.config.from_object(Config)
#db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")