from flask import Flask, render_template, request

app = Flask(__name__)

messages = []

@app.route("/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        text = request.form["message"]
        messages.append(f"{name}: {text}")

    return render_template("contact.html", messages=messages)

if __name__ == "__main__":
    app.run(debug=True)
