from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        amount = float(request.form["amount"])
        from_currency = request.form["from_currency"].upper()
        to_currency = request.form["to_currency"].upper()

        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            rate = data["rates"].get(to_currency)

            if rate:
                result = f"{round(amount * rate, 2)} {to_currency}"
            else:
                result = "Invalid currency"

        else:
            result = "API Error"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
