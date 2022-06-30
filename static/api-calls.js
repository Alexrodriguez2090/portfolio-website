function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

const getPokemon = async () => {
    //Get pokemon 1-898 and add it to api call
    var idToGet = Math.floor(Math.random() * 898) + 1;
    var apiSite = "https://pokeapi.co/api/v2/pokemon/";
    var webToCall = apiSite + idToGet;

    //Perform api call
    const response = await fetch(webToCall);
    const myJson = await response.json();

    //Setting up name and image
    var nameToShow = capitalizeFirstLetter(myJson.name);
    var imgToShow = "<img src='" + myJson.sprites.front_default +"'>";

    //Show user information
    document.getElementById("pokemonName").innerHTML = nameToShow;
    document.getElementById("pokemonSprite").innerHTML = imgToShow;
}