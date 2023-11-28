from flask import redirect, Blueprint, render_template, request
from Db import db
from Db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user
from flask import url_for

lab6 = Blueprint('lab6', __name__)


@lab6.route("/lab6/check")
def main():
    my_users = users.query.all()
    print(my_users)
    return "result in console!"


@lab6.route("/lab6/checkarticles")
def checkarticles():
    all_articles = articles.query.all()
    print(all_articles)
    return "result in console!"

@lab6.route("/lab6/register", methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template("register2.html")

    username_form = request.form.get("username")
    password_form = request.form.get("password")

    # Проверка пустого имени пользователя
    if not username_form:
        error = "Пустое имя!"
        return render_template("register2.html", error=error)

    # Проверка длины пароля
    if len(password_form) < 5:
        error = "Пароль должен содержать не менее 5 символов!"
        return render_template("register2.html", error=error)

    # Проверка наличия пользователя с таким именем
    existing_user = users.query.filter_by(username=username_form).first()
    if existing_user:
        error = "Пользователь с таким именем уже существует!"
        return render_template("register2.html", error=error)

    # Создание нового пользователя
    hashed_password = generate_password_hash(password_form, method="pbkdf2")
    new_user = users(username=username_form, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return redirect("/lab6/login")

@lab6.route('/lab6/')
def lab():
    return render_template('lab6.html')


@lab6.route("/lab6/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login3.html")

    username_form = request.form.get("username")
    password_form = request.form.get("password")

    if not username_form or not password_form:
        error_message = "Поле имя и/или пароль не заполнено"
        return render_template("login3.html", error_message=error_message)

    my_user = users.query.filter_by(username=username_form).first()

    if my_user is None:
        error_message = "Пользователь не существует"
        return render_template("login3.html", error_message=error_message)

    if not check_password_hash(my_user.password, password_form):
        error_message = "Неправильный пароль"
        return render_template("login3.html", error_message=error_message)

    login_user(my_user, remember=False)
    return redirect("/lab6/articles")