from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, Blueprint, redirect,session
import psycopg2

lab5 = Blueprint('lab5', __name__)

#отдельную функцию, которая будет возвращать connection.

def dBConnect():
    #параметры подключения к бд
    conn = psycopg2.connect(
        host="127.0.0.1",
        database = "knowledge_base_for_zalevskaya_olga",
        user = "zalevskaya_olga_knowledge_base",
        password = "password",
        port = 5432
    )

    return conn;


def dBClose(cursor,connection):
    #закрытие курсора и соединения
    cursor.close()
    connection.close()


@lab5.route("/lab5/")
def main():
    visibleUser = session.get('username', 'Anon')
    # Прописываем параметры подключения к БД
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base_for_zalevskaya_olga",
        user="zalevskaya_olga_knowledge_base",
        password="password",
        port = 5432
    )
    # Получаем курсор. С помощью него мы можем выполнять SQL-запросы
    cur = conn.cursor()
    # Пишем запрос, который курсор должен выполнить
    cur.execute("SELECT * FROM users;")
    # fetchall - получить все строки, которые получились в результате выполнения SQL-запроса в execute
    # Сохраняем эти строки в переменную result
    result = cur.fetchall()

    # Закрываем соединение с БД
    cur.close()
    conn.close()

    print(result)

    return render_template('lab5.html',  visibleUser= visibleUser)


@lab5.route('/lab5/users')
def user():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database = "knowledge_base_for_zalevskaya_olga",
        user = "zalevskaya_olga_knowledge_base",
        password = "password",
        port = 5432
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    result = cur.fetchall()
    return render_template('users.html', users=result)


@lab5.route('/lab5/register', methods=['GET', 'POST'])
def registerPage():
    errors = []

#если метод GET, то возращается шаблон
    if request.method == 'GET':
        return render_template('register.html', errors=errors)
#если метод POST, попадаем сюда. 
    username = request.form.get('username') 
    password = request.form.get('password')
#проверяем на пустоту. Если любой из низ пустой, добавляем ошибку
    if not (username and password):
        errors.append("Пожалуйста, заполните все поля")
        print(errors)
        return render_template('register.html', errors=errors)

    hashPassword = generate_password_hash(password)
#если попали сюда, то все зоплненою Подключаемся к БД
    conn = dBConnect()
    cur = conn.cursor()
    # Пишем запрос, который курсор должен выполнить,проверяем наличие клиента в базе. 
    cur.execute(f"SELECT username FROM users WHERE username = '{username}';")
    #только один пользователь с таким именем может быть в бд
    if cur.fetchone() is not None:
        errors.append("Пользователь с данным именем уже существует")

        conn.close()
        cur.close()
        return render_template('register.html', errors=errors)
    
     # Пишем запрос, который курсор должен выполнить
    cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}','{hashPassword}');")
    conn.commit()
    conn.close()
    cur.close()

    return redirect("/lab5/login")


@lab5.route('/lab5/login', methods=['GET', 'POST'])
def loginPage():
    errors = []

    if request.method == 'GET':
        return render_template('login2.html', errors=errors)

    username = request.form.get('username')
    password = request.form.get('password')

    if not (username and password):
        errors.append("Пожалуйста, заполните все поля")
        return render_template('login2.html', errors=errors)

    conn = dBConnect()
    cur = conn.cursor()
    cur.execute(f"SELECT id, password FROM users WHERE username = '{username}'")
    result = cur.fetchone()

    if result is None:
        errors.append("Неправильный логин или пароль")
        conn.close()  # Закрытие соединения
        return render_template('login2.html', errors=errors)
    
    userID, hashPassword = result
    #check_password_hash сравниваем хэш и пароль из бд. Сама переведет password в хэш
    if check_password_hash(hashPassword, password):
        #сохраняем id и username в сессию
        session['id'] = userID
        session['username'] = username
        conn.close()  # Закрытие соединения
        return redirect("/lab5/")
    else:
        errors.append("Неправильный логин или пароль")
        return render_template("login2.html", errors=errors )


@lab5.route("/lab5/new_article", methods=["GET", "POST"])
def createArticle():
    errors = []
    #проверяем авторизован ли пользователь. читаем из токена id 
    userID = session.get("id")

    if userID is not None:
        if request.method == "GET":
            return render_template("new_article.html")
        
        if request.method == "POST":
            text_article = request.form.get("text_article")
            title = request.form.get("title_article")
        
        if len(text_article) == 0:
            errors.append("Заполните текст")
            return render_template("new_article.html", errors=errors)
        
        conn = dBConnect()
        cur = conn.cursor()

        cur.execute(f"INSERT INTO articles(user_id, title, article_text) VALUES ({userID}, '{title}', '{text_article}') RETURNING id")
        new_article_id = cur.fetchone()[0] #получаем id от вновь созданной базы
        conn.commit()

        dBClose(cur,conn)

        return redirect(f"/lab5/articles/{new_article_id}")
    return redirect("/lab5/login")


@lab5.route("/lab5/articles/<string:article_id>") #позволяет получить значение в роуте
def getArticle(article_id):
    userID = session.get("id")

    if userID is not None:
        conn = dBConnect()
        cur = conn.cursor()

        cur.execute("SELECT title, article_text FROM articles WHERE id = %s and user_id = %s", (article_id, userID))

        articleBody = cur.fetchone()

        dBClose(cur, conn)

        if articleBody is None:
            return "Not found!"
        
        text = articleBody[1].splitlines() #разбитие сторки на массив

        return render_template("articleN.html", article_text=text,
        article_title=articleBody[0], username=session.get("username"))


@lab5.route("/lab5/article_list")
def getArticleList():
    userID = session.get("id")
    username = session.get("username")
    if userID is None:
        articles_list = []
    else:
        conn = dBConnect()
        cur = conn.cursor()
        
        cur.execute(f"SELECT id, title FROM articles WHERE user_id = {userID}")
        articles_list = cur.fetchall()

    return render_template("article_list.html", articles_list=articles_list, username=username)

@lab5.route("/lab5/logout")
def logout():
    session.clear()
    return redirect("/lab5/login")

