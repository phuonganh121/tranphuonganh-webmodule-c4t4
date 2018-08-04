from mongoengine import * 

class Movie(Document):
    title = StringField()
    image_url = StringField()
    link = StringField()

# 1: Connect to mlab 
import mlab
mlab.connect()

# # 2: Create a movie 
# movie = Movie (title = "Avengers: Infinity War", image_url = "https://m.media-amazon.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_UX182_CR0,0,182,268_AL_.jpg", link = "https://www.imdb.com/title/tt4154756/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=MY4P09SJ9ZY9CFFQ4QZH&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_23")

# # 3: Send newly created movie to mlab 
# movie.save()

movie_list = Movie.objects() #lazyloading
for movie in movie_list:
    print(movie.title)

