from flask import Flask, render_template, url_for, redirect
from .blueprints.home import homebp
from .blueprints.error import errorbp
from .blueprints.admin import adminbp

app = Flask(__name__)
app.register_blueprint(homebp)
# Blueprint can be registered many times
app.register_blueprint(adminbp)
app.register_blueprint(errorbp)

@app.errorhandler(404)
def Errorh(msg):
    return redirect(url_for('errorbp.error'))

if __name__=='__main__':
  app.run()
