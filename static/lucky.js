/** processForm: get data from form and make AJAX call to our API. */

$("#lucky-form").on("submit", async function (event) {
  event.preventDefault();

  //collect the form data from index.html with jquery
  let name = $("#name").val();
  let year = $("#year").val();
  year = parseInt(year)
  let email = $("#email").val();
  let color = $("#color").val();

  //make a GET request to the numbers api and set the result to variables
  let rand_num = Math.floor(Math.random() * 100);
  let num_fact = await axios.get('http://numbersapi.com/' + rand_num );
  let year_fact = await axios.get('http://numbersapi.com/' + year);

  //create a header called data with the form data and the 2 GET requests to be sent as a parameter of the axios post request
  let data = {
    name: name,
    year: year,
    email: email,
    color: color,
    num_fact: num_fact,
    year_fact: year_fact
  }

  //request and send data to the api on the BACKEND for processing and handle the response and errors
  let res = await axios.post('http://127.0.0.1:5000/api/lucky', data)
    .then(function(res){
      console.log(res)
      //document.querySelector('#lucky-results').innerHTML = res;
    })
    .catch(function(error){
      console.log(error)
    })

  //clear the form
  $("#lucky-form").trigger("reset");
});
