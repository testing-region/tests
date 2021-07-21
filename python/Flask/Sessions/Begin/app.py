from flask import Flask, Markup, render_template


#creating flask app object
app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder='templates',
    static_folder='static'
    )


@app.route('/hello')
def hello():
    '''The return type must be a string, dict, tuple, Response instance, or WSGI callable, but it was a int. It is not supported as a return type'''
    return "Hello World!"


@app.route('/markup')
def html():
    '''To serve raw html, use Markup in flask'''
    return Markup('<h1>Hello World!</h1>')

#Rendering templates
@app.route('/home')
def home():
    nav = [
    {'name': 'Home', 'url': '#'},
    {'name': 'About', 'url': '#'},
    {'name': 'Pics', 'url': '#'}
    ]

    return render_template(
        'home.html',
        nav=nav,
        title="Test Homepage",
        description="A flask test app"
        )


