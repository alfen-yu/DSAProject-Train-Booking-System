from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def user_registration():
    return render_template('home.html')

@app.route("/booking_details")
def booking_details():
    return render_template('booking.html')


if __name__ == "__main__":
    app.run(debug = True)