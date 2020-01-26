from flask import Flask, render_template
import data as tours_data

app = Flask(__name__)


# Main page
@app.route('/')
def main():
    return render_template('index.html')


# Directions
@app.route('/from/<direction>/')
def get_direction(direction):
    return render_template('direction.html', direction=direction)


# Tour
@app.route('/tours/<id>/')
def tour(id):
    tours = tours_data.tours
    departures = tours_data.departures
    return render_template('tour.html', id=id, tours=tours, departures=departures)


app.run()
