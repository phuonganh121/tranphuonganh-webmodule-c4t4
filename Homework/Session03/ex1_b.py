from mongoengine import *
import mlab

class Hobby(Document):
    title = StringField(max_length=100)
    image_url = StringField()
    link = StringField()

mlab.connect()

hobby = Hobby (title = "Phuong Ly", image_url = "https://znews-photo-td.zadn.vn/w1024/Uploaded/unvjuas/2018_01_14/NGUYEN_BA_NGOC2349_ZING.jpg", link = "http://kenh14.vn/doi-song/chum-anh-phuong-ly-em-gai-phuong-linh-ngay-cang-xinh-dep-20150312045943786.chn")

hobby.save()

