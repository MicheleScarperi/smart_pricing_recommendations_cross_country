import pandas as pd
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

products = {
    0: 'iPhone X',
    1: 'Samsung Galaxy',
    2: 'Nokia',
}

"""def product_repr(key):
    return {
        'url': request.host_url.rstrip('/') + url_for('products_list', key=key),
        'text': products[key]
    }"""


# Create a URL route in our application for "/"
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/search', methods=['POST'])
def search():
    data = request.form
    whatwassearched = [request.form.get('searchTerm'), 'Test1', 'Test2']

    # results = findProduct(whatwassearched)

    return render_template('results.html', result=whatwassearched)


@app.route('/tables', methods=['POST', 'GET'])
def show_tables():
    df1 = pd.read_csv('/Backend/merged.csv')

    return render_template('analysis.html')


@app.route('/search1', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If ID is not provided, display an error in the browser.
    if 'idd' in request.args:
        # idd = int(request.args['idd'])
        # use idd to look up produts that should be returned
        return request.args['idd']
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty array for the results
    searchResults = []

    # Loop through the data and match results that fit.
    # IDs are unique, but other fields might return many results.0,
    for searchResult in products:
        if searchResult['idd'] == idd:
            searchResults.append(searchResult)

    return jsonify(searchResults)


# http://0.0.0.0:5000/search?idd=1 this in the url will return Samsung Galaxy

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
