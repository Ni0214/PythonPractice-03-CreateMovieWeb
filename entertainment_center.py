import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story",
                      "A story of a boy and his toys that come to life",
                      "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=vwyZH85NQC4"
                      )
#print(toy_story.storyline)

avater = media.Movie("Avatar",
                      "A marine on an alien planet",
                      "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                      "http://www.youtube.com/watch?v=-9ceBgWV8io"
                      )
#print(avater.storyline)
#avater.show_trailer()

school_of_rock = media.Movie("School of Rock",
                      "Using rock music to learn",
                      "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                      "http://www.youtube.com/watch?v=3PsUJFEBC74"
                      )

rataouille = media.Movie("Rataouille",
                      "A rat is chef in Paris",
                      "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                      "http://www.youtube.com/watch?v=c3sBBRxDqk"
                      )

midnight_in_paris = media.Movie("Midnight in Paris",
                      "Going back in time to meet authors",
                      "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                      "http://www.youtube.com/watch?v=atLg2wQxvU"
                      )

hunger_games = media.Movie("Hunger Games",
                      "A really reality show",
                      "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                      "http://www.youtube.com/watch?v=PbA63a7H0bo"
                      )

movies=[toy_story, avater, school_of_rock, rataouille, midnight_in_paris, hunger_games]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
