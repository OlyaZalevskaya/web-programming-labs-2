from flask import Blueprint, render_template, request, Blueprint
import psycopg2

lab5 = Blueprint('lab5', __name__)

def dBConnect():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database = "knowledge_base_for_zalevskaya_olga",
        user = "zalevskaya_olga_knowledge_base",
        password = "password",
        port = 5432
    )

    return conn;

def dBClose(cursor,connection):
    cursor.close()
    connection.close()


@lab5.route("/lab5/")
def main():
    
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

    return render_template('lab5.html')

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