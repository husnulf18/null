from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/map")
def galaxy_map():
    return render_template("galaxy_map.html")
@app.route("/anxiety")
def anxiety():
    return render_template("anxiety.html")


@app.route("/sadness")
def sadness():
    return render_template("sadness.html")


@app.route("/anger")
def anger():
    return render_template("anger.html")


@app.route("/hope")
def hope():
    return render_template("hope.html")


@app.route("/overthinking")
def overthinking():
    return render_template("overthinking.html")
if __name__ == "__main__":
    app.run(port=5555, debug=True)