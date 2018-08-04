from mongoengine import * 

class Movie(Document):
    title = StringField(max_length=100)
    image_url = StringField()
    link = StringField()

