from flask import Flask
from config import Config
from models.main_routers_db import *
from models.imp import db
from blueprints.all_routers_bpp import register_all_routers_bpp

app = Flask(__name__)

app.config.from_object(Config)

#db.init_app(app)

register_all_routers_bpp(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6543)