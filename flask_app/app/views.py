from flask import render_template, request, redirect, url_for
from app import db
from app.models import User
from app.controllers import create_user, get_all_users, get_user, update_user, delete_user

@app.route('/users', methods=['GET'])
def list_users():
    users = get_all_users()
    return render_template('list_users.html', users=users)

@app.route('/user/<int:user_id>', methods=['GET'])
def view_user(user_id):
    user = get_user(user_id)
    return render_template('view_user.html', user=user)

@app.route('/user/new', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        create_user(name, email, password)
        return redirect(url_for('list_users'))
    return render_template('new_user.html')

@app.route('/user/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = get_user(user_id)
    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']
        user.password = request.form['password']
        update_user(user_id, user.name, user.email, user.password)
        return redirect(url_for('view_user', user_id=user_id))
    return render_template('edit_user.html', user=user)

@app.route('/user/delete/<int:user_id>', methods=['POST'])
def delete_user_route(user_id):
    delete_user(user_id)
    return redirect(url_for('list_users'))
