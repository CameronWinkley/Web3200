from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {'author': 'Cameron Winkley',
     'title': 'Blog Post 1',
     'content': 'First post content',
     'date_posted': 'April 9th, 2019'},

    {'author': 'Kiersten Winkley',
     'title': 'Blog Post 1',
     'content': 'Second post content',
     'date_posted': 'April 10th, 2019'}

]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/login')
def login():
    return render_template('login.htmle', title='Login')


if __name__ == '__main__':
    app.run()
