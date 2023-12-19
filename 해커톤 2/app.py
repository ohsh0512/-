from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():

    detected_person_count = get_detected_person_count()
    return render_template('index.html', personCount = detected_person_count)

if __name__ == '__main__':
    app.run(debug=True)

