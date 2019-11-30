from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
PHONES = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp()
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp()
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp()
    }
}


# Create a handler for our read (GET) PHONES
def read():
    """
    This function responds to a request for /api/people
    with the complete lists of phones

    :return:        sorted list of PHONES dictionary.
    """
    # Create the list of phones from our data
    return [PHONES[key] for key in sorted(PHONES.keys())]
