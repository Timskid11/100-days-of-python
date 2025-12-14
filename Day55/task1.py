from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

def make_bold(function):
    def bold():
        return f'<b> {function()} </b>'
    return bold
def make_underline(function):
    def underline():
        return f'<u> {function()} </u>'
    return underline
def make_italic(function):
    def italic():
        return f'<i> {function()} </i>'
    return italic
def make_colorful(function):
    def colorful():
        return (f'<h1 style="color: aqua;'
                f'background-color : gray;"> {function()} </h1>')
    return colorful

@app.route('/bye')
@make_bold
@make_underline
@make_italic
@make_colorful
def greeting():
    return "Good morning to everyone!\nHAVE A NICE DAY"

greeting()





if __name__ == '__main__':
    app.run(debug=True)
