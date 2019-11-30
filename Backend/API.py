import flask

# Create 	POST 	Create a new, unique thing
# Read 	GET 	Read the information about a thing or collection of things
# Update 	PUT 	Update the information about an existing thing
# Delete 	DELETE 	Delete a thing

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


app.run()

# test comment
