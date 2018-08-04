import mlab 
from models.movie import Movie 

mlab.connect()

found_movie = Movie.objects(title__icontains="Batman") #match #contain

# print(len(found_movies))

# print(found_movie.title)
# print(found_movie.link)