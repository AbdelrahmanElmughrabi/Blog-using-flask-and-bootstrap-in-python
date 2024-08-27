from flask import Flask, render_template, url_for
import requests



web_text= requests.get("https://api.npoint.io/38ae4df05a03e07e9c9a").json()

# for item in web_text:
#     if item["id"]==1:
#         print(item["title"])
#     if item["id"]==2:
#         print(item["title"])
#     if item["id"]==3:
#         print(item["title"])
#
app=Flask(__name__)

@app.route("/")
def home():
    # url_for('static', filename='assets/css/ styles.css')
    return render_template("index.html",web_text=web_text)

@app.route("/about")
def about():
    # url_for('static', filename='assets/css/ styles.css')
    return render_template("about.html",web_text=web_text)

@app.route("/contact")
def contact():
    # url_for('static', filename='assets/css/ styles.css')
    return render_template("contact.html",web_text=web_text)

@app.route("/post/<int:index>")
def post(index):
    # url_for('static', filename='assets/css/ styles.css')
    requested_post=None
    for blog_post in web_text:
        if blog_post["id"]==index:
            requested_post=blog_post
    return render_template("post.html",post=requested_post)


@app.route("/pwoekr/wer/<int:index>")
def sdksnf(index):
    holder=None
    for item in web_text:
        if item["id"]==index:
            holder=item
    render_template("post.html",data=holder)



if __name__=="__main__":
    app.run(debug=True)