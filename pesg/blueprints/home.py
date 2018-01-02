from flask import Blueprint, request, session, render_template, redirect, url_for



homebp = Blueprint('homebp', __name__)

@homebp.route('/home')
@homebp.route('/')
def homePage():
    return render_template('home.html')

@homebp.route('/k')
def kkk():
    return redirect(url_for('errorbp.error'))
