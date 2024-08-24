from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pet_name = request.form.get("pet_name")
        band_name = f"undefined {pet_name}"
        return render_template("index.html", band_name=band_name)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)