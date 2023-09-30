from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect ("/menu", code=302)

@app.route("/menu")
def menu():
     return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>    
    <body>
        <header>
        НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        <ol>
            <li>
            <a href = '/lab1'>Первая лабораторная</a>
            </li>
        </ol>
       

        <footer>
            &copy; Залевская Ольга, ФБИ-14, 3 курс, 2023
        </footer> 
    </body>   
</html>
"""

@app.route("/lab1/")
def lab1():
    return """
<!doctype html>
<html>
    <head>
        <title>Залевская Ольга Сергеевна, лабораторная 1</title>
    </head>    
    <body>
        <header>
        НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>
            <p>Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </p>
        
        <a href = '/menu'>Меню</a>

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
"""

@app.route("/lab1/oak")
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

@app.route("/lab1/student")
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

@app.route("/lab1/python")
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

@app.route("/lab1/panda")
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

@app.route('/lab2/example')
def example():
    name = 'Ольга Залевская'
    numer = 2
    gruppa = 'ФБИ-14'
    curs = 3 
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    buch = [
        {'autor': 'Александр Дюма', 'name': 'Граф Монте-Кристо',  'ganr': 'приключенческая литература', 'col': '624'},
        {'autor': 'Михаил Булгаков', 'name': 'Мастер и Маргарита',  'ganr': 'фантастика', 'col': '624'},
        {'autor': 'Антуан де Сент-Экзюпери', 'name': ' Маленький принц',  'ganr': 'повесть', 'col': '96'},
        {'autor': 'Михаил Булгаков', 'name': 'Собачье сердце',  'ganr': 'повесть', 'col': '85'},
        {'autor': 'Федор Достоевский', 'name': 'Преступление и наказание',  'ganr': 'роман', 'col': '592'},
        {'autor': 'Михаил Лермонтов', 'name': 'Герой нашего времени',  'ganr': 'психологический роман', 'col': '256'},
        {'autor': 'Александр Пушкин', 'name': 'Евгений Онегин',  'ganr': 'роман в стихах', 'col': '288'},
        {'autor': 'Николай Гоголь', 'name': 'Мёртвые души',  'ganr': 'поэма', 'col': '350'},
        {'autor': 'Федор Достоевский', 'name': 'Идиот',  'ganr': 'роман', 'col': '640'},
        {'autor': 'Александр Пушкин', 'name': ' Капитанская дочка',  'ganr': 'историческая проза', 'col': '130'}
    ]
    return render_template('example.html', 
                           name=name, numer=numer, gruppa=gruppa, 
                           curs=curs, fruits=fruits, buch=buch)