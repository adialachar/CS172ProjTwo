



function geocode() {

	var loc = "Miami,FL"
	axios.get('https://maps.googleapis.com/maps/api/geocode/json',{
	params:{
		address:loc,
		key = 'AIzaSyAxl5yLMYFQZl5OhdMIqnPz3jbD4qjSeIo'


	}

	})


	.then(function(response){

		console.log(response)

	})

	.catch(function(error)){


		console.log(error);

	});




