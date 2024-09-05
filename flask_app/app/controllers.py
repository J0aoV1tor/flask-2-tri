from flask import request, jsonify
from app import db
from app.models import User

def create_user(name, email, password):
    new_user = User(name=name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

def get_all_users():
    return User.query.all()

def get_user(user_id):
    return User.query.get(user_id)

def update_user(user_id, name=None, email=None, password=None):
    user = User.query.get(user_id)
    if user:
        if name:
            user.name = name
        if email:
            user.email = email
        if password:
            user.password = password
        db.session.commit()

def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
