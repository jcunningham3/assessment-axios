from flask import Flask, flash, render_template, redirect, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS
from models import Users, db, connect_db
import requests

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///lucky_num_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'crowBottom'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def homepage():
    """Show homepage."""
    return render_template("index.html")

# POST
@app.route('/api/lucky', methods=['POST'])
def handle_lucky_user():

    # set the incoming header data to data
    data = request.json
    print(data)
    # set our incoming data to be in the 'correct' format
    num_fact = data['num_fact']
    year_fact = data['year_fact']


    name = data['name']
    name = str(name)

    year = data['year']
    year = int(year)


    email = data['email']

    color = data['color']
    color = color.lower()
    print('color in')
    print(color)
    print('')
    colors = ['red', 'orange', 'green', 'blue']
    for x in colors:
        if x == color:
            color = 'success'


    print('color out')
    print(color)

    # color must be one named in the list


    #error handling
    if name == '':
        return jsonify({"error":
                {
                    "name": ["This field is required."]
                }
            })
    elif year <= 1899:
        return jsonify({"error":
                {
                    "year": ["This field should be between 1900 and 2000"]
                }
            })
    elif year >= 2000:
        return jsonify({"error":
                {
                    "year": ["This field should be between 1900 and 2000"]
                }
            })
    elif email == '':
        return jsonify({"error":
                {
                    "email": ["This field is required."]
                }
            })
    elif color != 'success':
        return jsonify({"error":
                {
                    "color": ["This field only accepts red, orange, green, or blue."]
                }
            })
    else:
        return jsonify({"success":
                {
                    "num_fact": [num_fact],
                    "year_fact":[year_fact]
                }
            })
