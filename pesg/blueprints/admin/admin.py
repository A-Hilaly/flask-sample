from flask import Blueprint, request, session, render_template, redirect, url_for



adminbp = Blueprint('adminbp', __name__)

@adminbp.route('/admin')
def homePage():
    return render_template('admin.html')
