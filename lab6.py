from flask import Blueprint, render_template
lab4 = Blueprint('lab6', __name__)

@lab4.route('/lab6/')
def lab():
    return render_template('lab6.html')