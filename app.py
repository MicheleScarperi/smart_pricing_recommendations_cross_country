from flask import Flask, request, url_for, jsonify, render_template
import pandas as pd

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


@app.route('/tables')
def show_tables():
    data1 = pd.read_csv('merged.csv', index_col=0)
    data1.index.name = None
    prodname = data1.loc[data1.productname]
    return render_template('analysis.html', tables=[prodname.to_html], titles=['Product Name'])


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
    # IDs are unique, but other fields might return many results.
    for searchResult in products:
        if searchResult['idd'] == idd:
            searchResults.append(searchResult)

    return jsonify(searchResults)


# http://0.0.0.0:5000/search?idd=1 this in the url will return Samsung Galaxy

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
