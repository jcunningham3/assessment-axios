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

@app.route('/api/lucky')
# list all todos
def list_lucky_users():
    all_users = [user.serialized() for user in Users.query.all()]
    return jsonify(users=all_users)

@app.route('/api/lucky', methods=['POST'])
def make_lucky_user():
    data = request.json

    # BACKEND error handling
    if data['name'] == '':
        return jsonify(message='name field must not be blank')
    elif data['email'] == '':
        return jsonify(message='name field must not be blank')
    elif int(data['year']) < 1900:
        return jsonify(message='year must be an integer bwtween 1900 and 2000')
    elif int(data['year']) > 2020:
        return jsonify(message='year must be an integer bwtween 1900 and 2000')
    elif data['color'] == '':
        return jsonify(message='color field must not be blank')

    # OTHERWISE CREATE A USER
    else:
        user = Users(name = data['name'], year = data['year'], email = data['email'], color = data['color'])
        db.session.add(user)
        db.session.commit()

        return(jsonify(user=user.serialized()), 201)

@app.route('/purtiy')
def nothing_func():
    return
    """async function processForm(event) {
      event.preventDefault();
      //get the name value and check for errors
      let name = document.querySelector('#name').innerHTML;
      if(name == ""){
         document.querySelector('#name-err').innerText = "This field cannot be blank.";
      }
      //get the year value and check for errors
      let year = document.querySelector('#year')..innerHTML;
      if(year < 1900 || year > 2000){
         document.querySelector('#year-err').innerText = "Please enter a year between 1900 and 2000.";
      }
      //get the email value and check for errors
      let email = document.querySelector('#email')..innerHTML;
      if(email == ""){
         document.querySelector('#email-err').innerText = "This field cannot be blank.";
      }
      //get the color value and check for errors
      let color = document.querySelector('#color')..innerHTML;
      color = color.toLowerCase()
      if(color == ""){
         document.querySelector('#color-err').innerText = "Colors are limited to: red, green, orange, and blue.";
      }
      const newLuckyNumResponse = await axios.post('${BASE_URL}/lucky', {
        name,
        year,
        email,
        color
      });
    }


    $("#lucky-form").on("submit", processForm);
    """
