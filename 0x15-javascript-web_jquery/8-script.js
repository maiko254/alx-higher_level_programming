$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  for (const result in data.results) {
    const movie = $('<li></li>').text(result.title);
    $('UL#list_movies').append(movie);
  }
});
