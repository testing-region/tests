from  flask import Flask, render_template, redirect
from forms import RegisterForm, LoginForm


app = Flask(
    __name__,
    static_folder='static',
    template_folder='templates'
)

app.config['SECRET_KEY'] = 'f1271ef85049627c2ab5447dd31c0b7f'

posts = [
    {
        "author": "Kweku Sampson",
        "title": "Blog Post 1",
        "content": "My First Business",
        "date_posted": "March 18, 2020"
    },
    {
        "author": "Kweku Khapps",
        "title": "Blog Post 2",
        "content": "My Second Business",
        "date_posted": "March 17, 2020"
    }
]



@app.route('/')
@app.route("/home")
def home():
    return render_template(
        "home.html",
        posts=posts,
    )


@app.route("/about")
def about():
    return render_template(
        "about.html",
        title="About"
    )


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    return render_template(
        "register.html",
        title="Register",
        form=form
    )


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template(
        "login.html",
        title="Login",
        form=form
    )



if __name__ == "__main__":
    app.run(debug=True)
