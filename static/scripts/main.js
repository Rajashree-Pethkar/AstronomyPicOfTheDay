$(document).ready(function() {
});

function getAstronomyPicOfTheDay() {
      $.ajax({
          url: "/astronomyPicOftheDay",
          type: "GET"
      }).done(function(response) {
          $("#picoftheday").attr("src", response.url);
      });
};