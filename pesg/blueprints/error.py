from flask import Blueprint, request, session, render_template



errorbp = Blueprint('errorbp', __name__)


@errorbp.route('/error')
def error():
    return render_template('error.html')
