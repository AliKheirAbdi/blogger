from flask import url_for
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from werkzeug.wrappers import auth

from app import db
from app.models import User
from app.users.forms import RegistrationForm
from ..email import mail_message


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm(FlaskForm)
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

        mail_message("Welcome to watchlist","email/welcome_user",user.email,user=user)

        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)