from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from pymongo import MongoClient
from routes.auth_routes import auth
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Setup MongoDB connection
mongo_uri = os.getenv('MONGO_URI')
client = MongoClient(mongo_uri)
db = client['sms_db']  # Your database

# Setup Bcrypt and LoginManager
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Register your auth routes
app.register_blueprint(auth)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
