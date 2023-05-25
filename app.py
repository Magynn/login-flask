from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['MONGO_URI'] = 'MONGO_URI'
mongo = PyMongo(app)
login_manager = LoginManager(app)


class User(UserMixin):
    def __init__(self, username):
        self.username = username

    def get_id(self):
        return self.username


@login_manager.user_loader
def load_user(username):
    user = mongo.db.users.find_one({'username': username})
    if user:
        return User(user['username'])
    else:
        return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        if username and password and confirm_password:
            if password == confirm_password:
                user = mongo.db.users.find_one({'username': username})
                if user:
                    flash('O nome de usuário já existe.')
                else:
                    hashed_password = generate_password_hash(password)
                    mongo.db.users.insert_one(
                        {'username': username, 'password': hashed_password})
                    flash('Registro bem-sucedido.')
                    return redirect(url_for('login'))
            else:
                flash('As senhas não coincidem.')
        else:
            flash('Por favor preencha todos os campos.')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            user = mongo.db.users.find_one({'username': username})
            if user and check_password_hash(user['password'], password):
                login_user(User(user['username']))
                flash('Login bem-sucedido.')
                return redirect(url_for('profile'))
            else:
                flash('Credenciais inválidas.')
        else:
            flash('Por favor preencha todos os campos.')
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout bem-sucedido.')
    return redirect(url_for('index'))


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', username=current_user.username)
