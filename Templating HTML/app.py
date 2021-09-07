from flask import Flask, render_template

from data import generate_users

users = generate_users(100)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users')
def get_users():
    return render_template('users/index.html', users=users)


@app.route('/users/<int:id>')
def get_user(id):
    filtered_users = filter(lambda user: user['id'] == id, users)
    user = next(filtered_users, None)

    if user is None:
        return 'Page not found', 404

    return render_template('users/show.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)

