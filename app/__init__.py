from flask import Flask
from config import CassandraConfig
from app.routes import task_routes

app = Flask(__name__)
app.config.from_object(CassandraConfig)

app.register_blueprint(task_routes)
