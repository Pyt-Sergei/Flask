from flask import Flask, json, redirect, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    cart = json.loads(request.cookies.get('cart', json.dumps({})))
    return render_template('index.html', cart=cart)


@app.route('/cart-items', methods=['POST'])
def add_item_to_cart():
    cart = json.loads(request.cookies.get('cart', json.dumps({})))

    item_id = request.form['item_id']
    item_name = request.form['item_name']

    item = cart.setdefault(item_id, {'name': item_name, 'count': 0})
    item['count'] += 1

    encoded_cart = json.dumps(cart)

    response = redirect('/')
    response.set_cookie('cart', encoded_cart)

    return response


@app.route('/cart-items/clean', methods=['POST'])
def clean_cart():
    response = redirect('/')
    response.delete_cookie('cart')

    return response


if __name__ == '__main__':
    app.run(debug=True)
