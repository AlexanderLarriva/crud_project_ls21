from flask import Flask, json, redirect, render_template, request, make_response

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    cart = json.loads(request.cookies.get('cart', json.dumps({})))
    return render_template('index.html', cart=cart)


# BEGIN (write your solution here)
@app.route('/cart-items', methods=['POST'])
def add_to_cart():
    item_id = request.form.get('item_id')
    item_name = request.form.get('item_name')

    cart = json.loads(request.cookies.get('cart', json.dumps({})))

    if item_id in cart:
        cart[item_id]['count'] += 1
    else:
        cart[item_id] = {'name': item_name, 'count': 1}

    resp = make_response(redirect('/'))
    resp.set_cookie('cart', json.dumps(cart))

    return resp


@app.route('/cart-items/clean', methods=['POST'])
def clean_cart():
    resp = make_response(redirect('/'))
    resp.set_cookie('cart', '', expires=0)

    return resp

# END
