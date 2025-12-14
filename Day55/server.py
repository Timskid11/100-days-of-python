import random

from flask import Flask
app = Flask(__name__)

random_number = random.randint(0,9)
print(random_number)

@app.route('/')
def homepage():
    return f'<h1>Guess a number between 0 and 9</h1>' \
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt=A gif of random numbers between 0-9 displayed/>'

@app.route('/<int:guess>')
def guess_number(guess):
    if guess > random_number:
        return f'<h1 style="color: purple;">{guess} is too high,try again</h1>'\
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'

    elif guess < random_number:
        return f'<h1 style="color: red;">{guess} is too low,try again</h1>' \
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return f'<h1 style="color: green;">{guess} is correct</h1>' \
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


homepage()
if __name__ == '__main__':
    app.run(debug=True)