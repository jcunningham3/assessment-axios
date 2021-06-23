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
    elif isinstance(data['color'], str) == False:
        return jsonify(
            {"error":
                {
                    "name": ["This field is must be a string."]
                }
            })
    elif data['color'] != 'red':
        if data['color'] != 'orange':
            if data['color'] != 'green':
                if data['color'] != 'blue':
                    return jsonify(
                        {"error":
                            {
                                "color": ["This field is must red, orange, green, or blue."]
                            }
                        })
    else:
        return jsonify(
            {
                "success":
                    {
                        "num_fact": [data['num_fact']],
                        "year_fact": [data['year_fact']]
                    }
            }
        )
