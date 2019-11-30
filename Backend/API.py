import flask

# Create 	POST 	Create a new, unique thing
# Read 	GET 	Read the information about a thing or collection of things
# Update 	PUT 	Update the information about an existing thing
# Delete 	DELETE 	Delete a thing

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to Smart Price Recommendations!</h1><p>You can find the best price for the most value here.</p>"


app.run()

# test comment
