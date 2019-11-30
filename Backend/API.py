from flask import render_template
import connexion
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

products = {
    0: 'iPhone X',
    1: 'Samsung Galaxy',
    2: 'Nokia',
}


def product_repr(key):
    return {
        'url': request.host_url.rstrip('/') + url_for('products_list', key=key),
        'text': products[key]
    }


# Create a URL route in our application for "/"
@app.route('/', methods=['GET', 'POST'])
def products_list():
    """
    List products.
    :return:        the rendered template 'home.html'
    """
    if request.method == 'POST':
        product = str(request.data.get('text', ''))
        idx = max(products.keys()) + 1
        products[idx] = product
        return product_repr(idx), status.HTTP_201_CREATED

    # request.method == 'GET'
    return [product_repr(idx) for idx in sorted(products.keys())]


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
