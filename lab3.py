from flask import Blueprint, render_template, request
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route('/lab3/forml')
def forml():
    user = request.args.get('user')
    return render_template('forml.html', user=user)