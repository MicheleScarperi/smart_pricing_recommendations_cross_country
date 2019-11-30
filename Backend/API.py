from flask import render_template
import connexion
from flask import request, url_for, jsonify
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
    :return:        Output from the products dictionary.
    """
    if request.method == 'POST':
        product = str(request.data.get('text', ''))
        idx = max(products.keys()) + 1
        products[idx] = product
        return product_repr(idx), status.HTTP_201_CREATED

    # request.method == 'GET'
    return [product_repr(idx) for idx in sorted(products.keys())]


#@app.route('/search', methods=['GET'])
#def api_all():
 #   search = param.get("key")
  #  result = products[search]
   # return jsonify(result)

@app.route('/search', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If ID is not provided, display an error in the browser.
    if 'idd' in request.args:
        idd = int(request.args['idd'])
        return products[idd]
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty array for the results
    searchResults = []

    # Loop through the data and match results that fit.
    # IDs are unique, but other fields might return many results.
    for searchResult in products:
        if searchResult['idd'] == idd:
            searchResults.append(searchResult)

    return jsonify(searchResults)


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
