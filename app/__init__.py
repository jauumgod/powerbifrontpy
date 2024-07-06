from flask import Flask, render_template, url_for, request, redirect, flash
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import pymysql
from flask_login import LoginManager, login_manager, login_required, login_user, logout_user
import time


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config.from_object('config')
migrate = Migrate(app,db)
db.init_app(app)


from .views import rotas
from .models import usuarios

