from flask import Flask, redirect

app = Flask(__name__)


@app.route("/") 
def index(): 
    return "Lets go to CHRONO SHOWWWW"

@app.route("/about-me") 
def about_me():
    return '''ĐI CHRONO ĐI NHÉ Ạ SHOW ÂM NHẠC VỚI HISAM, PHƯƠNG LY VÀ VÔ VÀN KHÁCH MỜI KHÁC.
    AI CHẤM BÀI EM THÌ GHÉ FANPAGE CNNSHINE TRÊN FACEBOOK NHÉ Ạ. CƠ HỘI NGÀN LẦN CÓ MỘT ĐỂ GẶP PHƯƠNG LY ĐÓ
    SIÊU ĐỈNH UHUHU ONCE IN A LIFE TIME. GRAB YOUR CHANCE!!!!!!!''' 

@app.route("/school")
def school(): 
    return redirect ("http://techkids.vn")

if __name__ == "__main__":
    app.run(debug=True)

