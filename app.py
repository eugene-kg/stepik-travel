import random

from flask import Flask, render_template
import data as tours_data

app = Flask(__name__)


# Main page
@app.route('/')
def main():
    tours = tours_data.tours
    departures = tours_data.departures
    title = tours_data.title
    subtitle = tours_data.subtitle
    description = tours_data.description

    # Shuffle the tour dictionary to make first 6 places different
    keys = list(tours.keys())
    random.shuffle(keys)
    tours_shuffled = {k: tours[k] for k in keys}

    return render_template('index.html', tours=tours_shuffled, departures=departures, title=title, subtitle=subtitle,
                           description=description)


# Directions
@app.route('/from/<direction>/')
def get_direction(direction):
    tours = tours_data.tours
    departures = tours_data.departures
    title = tours_data.title

    # TODO add check that direciton in in the list
    #if not direction in departures:

    tours_direction = dict()
    # Filter tour by direction
    for k, v in tours.items():
        if v['departure'] == direction:
            tours_direction[k] = v

    return render_template('direction.html', direction=direction, departures=departures, title=title,
                           tours=tours_direction)


# Tour
@app.route('/tours/<id>/')
def tour(id):
    tours = tours_data.tours
    title = tours_data.title
    departures = tours_data.departures
    direction = tours[int(id)]['departure']

    return render_template('tour.html', id=id, direction=direction, tours=tours, departures=departures, title=title)


@app.errorhandler(404)
def not_found(e):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!"


@app.errorhandler(500)
def server_error(e):
    return "Что-то не так, но мы все починим"

# Flask server
# app.run()


if __name__ == '__main__':
    app.run()
