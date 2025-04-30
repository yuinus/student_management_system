from flask import Flask
from dotenv import load_dotenv
from extensions import bcrypt, login_manager
from pymongo import MongoClient
import os

# Load .env
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# MongoDB setup
mongo_uri = os.getenv('MONGO_URI')
client = MongoClient(mongo_uri)
db = client['sms_db']

# Init extensions
bcrypt.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Attach db globally (optional)
app.db = db

# Register blueprints (after extensions are defined)
from routes.auth_routes import auth
app.register_blueprint(auth)
99
if __name__ == '__main__':
    app.run(debug=True)
