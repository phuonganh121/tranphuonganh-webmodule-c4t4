from mongoengine import * 
import mlab
from movie import Movie

# class Movie(Document):
#     title = StringField()

# movie1 = Movie (title = "abc")
# movie2 = Movie (title = "xyz")
# movie3 = Movie (title = "aaa")

mlab.connect()
movie_list = Movie.objects()

for movie in movie_list: 
    print (movie.title, movie.image_url, movie.link)
