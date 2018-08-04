from mongoengine import * 
import mlab

class Post(Document):
    title = StringField()
    content = StringField()
    author = StringField()
    meta = {"collection": "posts"}


post = Post (
    title = "abc",
    content = "xyz",
    author = "abc"
)

mlab.connect()
post.save()
