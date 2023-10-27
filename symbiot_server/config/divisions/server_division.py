from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from injector import Module


class ServerDivision(Module):
    app: Flask = None
    db: SQLAlchemy = None
