from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1', __name__)


@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect ("/menu", code=302)


@lab1.route("/menu")
def menu():
     return '''
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>    
    <body>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <header>
        НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        <ol>
            <li>
            <a href = '/lab1'>Первая лабораторная</a>
            </li>
            <li>
            <a href = '/lab2/'>Вторая лабораторная</a>
            </li>
            <li>
            <a href = '/lab3/'>Третья лабораторная</a>
            </li>
            <li>
            <a href = '/lab4/'>Четвертая лабораторная</a>
            </li>
            <li>
            <a href = '/lab5/'>Пятая лабораторная</a>
            </li>
            <li>
            <a href = '/lab6/'>Шестая лабораторная</a>
            </li>
            <li>
            <a href = '/lab7/'>Седьмая лабораторная</a>
            </li>
            <li>
            <a href = '/lab8/'>Восьмая лабораторная</a>
            </li>
            <li>
            <a href = '/lab9/'>Девятая лабораторная</a>
            </li>
        </ol>
       

        <footer>
            &copy; Залевская Ольга, ФБИ-14, 3 курс, 2023
        </footer> 
    </body>   
</html>
'''


@lab1.route("/lab1/")
def lab():
    return '''
<!doctype html>
<html>
    <head>
        <title>Залевская Ольга Сергеевна, лабораторная 1</title>
    </head>    
    <body>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <header>
        НГТУ, ФБ, Лабораторная работа 1
        </header>

        <a href = '/menu'>Меню</a>

        <h1>web-сервер на flask</h1>
            <p>Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </p>
        

         <h2>Реализованные роуты</h2>    
        <ul>
            <li>
            <a href = '/lab1/oak'>/lab1/oak-дуб</a>
            </li>

            <li>
            <a href = '/lab1/student'>/lab1/student-студент</a>
            </li>

            <li>
            <a href = '/lab1/python'>/lab1/python-python</a>
            </li>

            <li>
            <a href = '/lab1/panda'>/lab1/panda-панда</a>
            </li>
        </ul>


        <footer>
            &copy; Залевская Ольга, ФБИ-14, 3 курс, 2023
        </footer> 
    </body>   
</html>
'''

@lab1.route("/lab1/oak")
def oak():
    return '''
<!doctype html>
<html>
    <head>
        <title>Залевская Ольга Сергеевна, лабораторная 1</title>
    </head>    
    
    <body>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <header>
        НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>Дуб</h1>

        <img src="''' + url_for('static', filename='oak.jpg') + '''">
        
        <footer>
            &copy; Залевская Ольга, ФБИ-14, 3 курс, 2023
        </footer> 
    </body>   
</html>
'''


@lab1.route("/lab1/student")
def stud():
    return '''
<!doctype html>
<html>
    <head>
        <title>Залевская Ольга Сергеевна, лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>    
    <body>
        <header>
        НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>Залевская Ольга Сергеевна</h1>

         <img src="''' + url_for('static', filename='ngtu.jpg') + '''">

        <footer>
            &copy; Залевская Ольга, ФБИ-14, 3 курс, 2023
        </footer> 
    </body>   
</html>
'''


@lab1.route("/lab1/python")
def pyt():
    return '''
<!doctype html>
<html>
    <head>
        <title>Залевская Ольга Сергеевна, лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>    
    <body>
        <header>
        НГТУ, ФБ, Лабораторная работа 1
        </header>
        
        <h2>Python</h2>

        <p>Python — это язык программирования, который широко используется в интернет-приложениях, разработке 
        программного обеспечения, науке о данных и машинном обучении (ML). Разработчики используют Python, 
        потому что он эффективен, прост в изучении и работает на разных платформах. </p>

        <p>Программы на языке Python можно скачать бесплатно, они совместимы со всеми типами систем и повышают 
        скорость разработки.Чаще всего Python используют в веб-разработке. Для него написано множество фреймворков: FastAPI, 
        Flask, Tornado, Pyramid, TurboGears, CherryPy и, самый популярный, Django.</p>

        <img src="''' + url_for('static', filename='pyt.jpeg') + '''">

        <footer>
            &copy; Залевская Ольга, ФБИ-14, 3 курс, 2023
        </footer> 
    </body>   
</html>
'''


@lab1.route("/lab1/panda")
def pand():
    return '''
<!doctype html>
<html>
    <head>
        <title>Залевская Ольга Сергеевна, лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>    
    <body>
        <header>
        НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h2>Панда</h2>

        <p>Род млекопитающих семейства медвежьих, обладающих некоторыми признаками енотов. Он включает 
        один живущий и четыре вымерших вида. Единственный современный вид рода - большая панда. </p>
        
        <p>Эти звери обитают в горных регионах центрального Китая: Сычуань и Тибет. Вес взрослой особи может
        колебаться в достаточно широком диапазоне - от 17 до 160 килограммов. </p>

        <p>Со второй половины XX века панда стала чем-то вроде национальной эмблемы Китая. Китайское название означает 
        «медведь-кошка». Его западное наименование происходит от малой панды. Раньше его также называли 
        пятнистым медведем.</p>

         <img src="''' + url_for('static', filename='5.jpg') + '''">


        <footer>
            &copy; Залевская Ольга, ФБИ-14, 3 курс, 2023
        </footer> 
    </body>   
</html>
'''
