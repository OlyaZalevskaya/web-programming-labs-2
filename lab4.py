from flask import Blueprint, render_template, request
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')

@lab4.route('/lab4/login', methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    username = request.form.get('username')
    if username == '':
        error = 'Не введен логин'
        return render_template('login.html', error=error, username=username)
    password = request.form.get('password')
    if password == '':
        error = 'Не введен пароль'
        return render_template('login.html', error=error, password=password)
    
    if username == 'alex' and password == '123':
        return render_template('suces.html', username=username, password=password)
    else:
        error = 'Неверный логин и/или пароль'
        return render_template('login.html', error=error, username=username, password=password)
    
@lab4.route('/lab4/holodil', methods=['GET', 'POST'])
def holodil():
    if request.method == 'GET':
        return render_template('holodil.html')
    
    temperature = request.form.get('temperature')
    error = ''
    message = ''  # Начальное значение для переменной message
    snowflakes = ''  # Начальное значение для переменной snowflakes
    
    if temperature is None or temperature == '':
        error = 'ошибка: не задана температура'
    elif int(temperature) < -12:
        error = 'не удалось установить температуру — слишком низкое значение'
    elif int(temperature) > -1:
        error = 'не удалось установить температуру — слишком высокое значение'
    elif -12 <= int(temperature) <= -9:
        message = f'Установлена температура: {temperature}°C'
        snowflakes = '❄️❄️❄️'
    elif -8 <= int(temperature) <= -5:
        message = f'Установлена температура: {temperature}°C'
        snowflakes = '❄️❄️'
    elif -4 <= int(temperature) <= -1:
        message = f'Установлена температура: {temperature}°C'
        snowflakes = '❄️'
    
    return render_template('holodil.html', error=error, temperature=temperature, message=message, snowflakes=snowflakes)
    