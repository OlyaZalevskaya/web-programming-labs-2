from flask import Blueprint, render_template
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/example')
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


@lab2.route("/lab2/")
def lab():
    return render_template('lab2.html')


@lab2.route("/lab2/flowers")
def flowers():
    return render_template('flowers.html') 
   
    