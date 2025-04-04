from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        data = request.form
        return render_template("character_sheet.html", data=data)
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
