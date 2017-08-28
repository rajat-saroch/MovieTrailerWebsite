import media
import fresh_tomatoes

# instance variables for different movies
toy_story = media.Movie('Toy Story',
                        'Toy Story is a American computer-animated buddy' +
                        'comedy adventure film', 'http://www.gstatic.com' +
                        '/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')
dangal = media.Movie('Dangal',
                     'Dangal is a 2016 Indian Hindi-language biographical' +
                     'sports drama film ', 'https://upload.wikimedia.org' +
                     '/wikipedia/en/9/99/Dangal_Poster.jpg',
                     'https://www.youtube.com/watch?v=x_7YlGv9u1g')
chak_de_india = media.Movie('Chak De India',
                            'Chak De! India is a 2007 Indian sports film',
                            'http://www.gstatic.com/tv/thumb/movieposters' +
                            '/168383/p168383_p_v8_ae.jpg',
                            'https://www.youtube.com/watch?v=6a0-dSMWm5g')
idiots = media.Movie('3 Idiots',
                     '3 Idiots is a 2009 Indian comedy-drama film', 'https' +
                     '://c.saavncdn.com/344/3-Idiots-Hindi-2009-500x500.jpg',
                     'https://www.youtube.com/watch?v=K0eDlFX9GMc')
the_dark_knight = media.Movie('The Dark Knight',
                              'The Dark Knight is a 2008 superhero film',
                              'http://www.gstatic.com/tv/thumb/movieposters' +
                              '/173378/p173378_p_v8_au.jpg',
                              'https://www.youtube.com/watch?v=yQ5U8suTUw0')
deadpool = media.Movie('Deadpool', 'Deadpool is a 2016 superhero film',
                       'http://t2.gstatic.com/images?q=tbn:ANd9GcTvrIHJfasS6' +
                       'poy34esN1O5hZonXaiqfEZb4WbnbAa9qJCIL8_9',
                       'https://www.youtube.com/watch?v=gtTfd6tISfw')

# creating array of movie names
movies = [toy_story, dangal, chak_de_india, idiots, the_dark_knight, deadpool]
# calling open_movies_page function from fresh tomatoes
fresh_tomatoes.open_movies_page(movies)
