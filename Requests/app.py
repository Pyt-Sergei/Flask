from flask import Flask, redirect, render_template, request

from user import generate_users

users = generate_users(5)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/users', methods=['GET'])
def get_users():
    return render_template('users/index.html', users=users)


@app.route('/users/create', methods=['GET'])
def get_user_form():
    return render_template('users/create.html', users=users)


@app.route('/users', methods=['POST'])
def create_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']

    if (first_name == ''):
        return "First name can't be blank", 422

    if (last_name == ''):
        return "Last name can't be blank", 422

    users.append({
        'first_name': first_name,
        'last_name': last_name
    })

    return redirect('/users')


if __name__ == '__main__':
    app.run(debug=True)

