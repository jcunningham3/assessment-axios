/* processForm: get data from form and make AJAX call to our API. */

$("#lucky-form").on("submit", async function (event) {
  event.preventDefault();

  //create a random number as the lucky number
  let rand_num = Math.floor(Math.random() * 100);

  //collect the form data from index.html with jquery
  let name = $("#name").val();
  let year = $("#year").val();
  if(year == ''){year = "0";}
  year = parseInt(year, 10)
  let email = $("#email").val();
  let color = $("#color").val();
  let num_fact = await axios.get('http://numbersapi.com/' + rand_num);
  let year_fact = '';
  //make a GET request to the numbers api and set the result to variables
  year_fact = await axios.get('http://numbersapi.com/' + year);

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
    .then((res) => {
      //console the response data
      console.log(res);

      //if there ae no errors
      if(res.data.success){
        document.querySelector('#lucky-results').innerHTML = res.data.success.num_fact[0].data + "<br>" + res.data.success.year_fact[0].data;
      }

      //handling name errors
      if(res.data.error.name){
        document.querySelector('#name-err').innerHTML = res.data.error.name[0];
      }

      //handling email errors
      else if(res.data.error.email){
        document.querySelector('#name-err').innerHTML = "";
        document.querySelector('#email-err').innerHTML = res.data.error.email[0];
      }

      //handling year errors
      else if(res.data.error.year){
        document.querySelector('#email-err').innerHTML = '';
        document.querySelector('#year-err').innerHTML = res.data.error.year[0];
      }

      //handling color errors
      else if(res.data.error.color){
        document.querySelector('#year-err').innerHTML = '';
        document.querySelector('#email-err').innerHTML = '';
        document.querySelector('#color-err').innerHTML = res.data.error.color[0];
      }

      //clear the error field from colors
      else{
        document.querySelector('#color-err').innerHTML = '';
      }

    })
    .catch((err) => {
      console.log("ERRORS!!", err);
    })

    //clear the form
    $("#lucky-form").trigger("reset");
});
