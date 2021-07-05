from flask import Flask, flash, render_template, redirect, request, jsonify
from flask_cors import CORS
from models import Users, db, connect_db
import requests

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///lucky_num_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


@app.route("/")
def homepage():
    """Show homepage."""
    return render_template("index.html")


@app.route('/api/lucky', methods=['POST'])
def handle_lucky_user():

    # set the incoming header data to data
    data = request.json

    lucky_number = data['num_fact']
    birth_fact = data['year_fact']
    color = data['color']
    color = color.lower()

    #handling color flow
    ok_colors = ['red', 'orange', 'green', 'blue']
    for x in ok_colors:
        if color != x:
            color == "invalid"

    # return name error in JSON
    if data['name'] == '':
        return jsonify(
            {"error":
                {
                    "name": ["This field is required."]
                }
            })
    elif isinstance(data['name'], str) == False:
        return jsonify(
        {"error":
            {
                "name": ["This field is must be a string."]
            }
        })

    # return email error in JSON
    elif data['email'] == '':
        return jsonify(
        {"error":
            {
                "email": ["This field is required."]
            }
        })
    elif isinstance(data['email'], str) == False:
        return jsonify(
        {"error":
            {
                "email": ["This field is must be a string."]
            }
        })

    # return year error in JSON
    elif data['year'] == '':
        return jsonify(
            {"error":
                {
                    "year": ["This field is required."]
                }
            })
    elif data['year'] < 1900:
        return jsonify(
            {"error":
                {
                    "year": ["This field must be greater than or equal to 1900."]
                }
            })
    elif data['year'] > 2020:
        return jsonify(
            {"error":
                {
                    "year": ["This field must be less than or equal to 2020."]
                }
            })

    # return color error in JSON
    elif data['color'] == '':
        return jsonify(
            {"error":
                {
                    "color": ["This field is required."]
                }
            })
    elif color == 'invalid':
        return jsonify(
            {"error":
                {
                    "color": ["This field must be red, orange, green, or blue."]
                }
            })

    # return success with lucky num and year fact
    else:
        return jsonify(
            {
                "success":
                    {
                        "num_fact": [lucky_number],
                        "year_fact": [birth_fact]
                    }
            }
        )

    print(incoming_color)
