from flask import Flask, render_template

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)


@app.route('/')
@app.route("/home")
def home():
    return render_template(
        "home.html",
        title='Flask WebApp',
        description="Flask WebApp Dummy Page"
    )


if __name__ == "__main__":
    app.run(debug=True)
