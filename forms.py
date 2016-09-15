from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from flask_moment import Moment
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = os.urandom(26)


class NameForm(Form):
    name = StringField('What is your name?', validators=[DataRequired])
    password = PasswordField('Password', validators=[DataRequired])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
            name = form.name.data
    form.name.data = ''
    form.password.data = ''
    return render_template('index.html', form=form, name=name)


if __name__ == '__main__':
    app.run(debug=True)