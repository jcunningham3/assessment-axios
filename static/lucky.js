/** processForm: get data from form and make AJAX call to our API. */
let randnum = Math.floor(Math.random() * 100);


$("#lucky-form").on("submit", async function (event) {
  event.preventDefault();

  let name = $("#name").val();
  let year = $("#year").val();
  let email = $("#email").val();
  let color = $("#color").val();
  //error handling
  if(name == "") {
    document.querySelector("#name-err").innerHTML = "This field cannot be blank.";
  }
  else if(year < 1900 || year > 2020) {
    document.querySelector("#name-err").innerHTML = "";
    document.querySelector("#year-err").innerHTML = "This field must be an integer between 1900 - 2000.";
  }
  else if(email == "") {
    document.querySelector("#year-err").innerHTML = "";
    document.querySelector("#email-err").innerHTML = "This field cannot be blank.";
  }
  else if(color == "") {
    document.querySelector("#email-err").innerHTML = "";
    document.querySelector("#color-err").innerHTML = "This field cannot be blank.";
  }
  //if no errors
  else {
    let lucky_num_fact = await axios.get(`http://numbersapi.com/${randnum}`);
    let year_fact = await axios.get(`http://numbersapi.com/${year}`);
    let data = {
      name: name,
      year: year,
      email: email,
      color: color,
      lucky_num_fact: lucky_num_fact,
      year_fact: year_fact
    }
    //request and send data to the api on the BACKEND for processing
    await axios.post('http://127.0.0.1:5000/api/lucky', data);

    document.querySelector("#lucky-results").innerHTML = "<br>" +
      "Your Lucky Number is: " + randnum + '<br>' +
      "Lucky Number Fact: " + data.lucky_num_fact + '<br>' +
      "Your birth year is " + year + "<br>" +
      "Birth Year Fact: " + data.year_fact;

    $("#lucky-form").trigger("reset");
  }
});
