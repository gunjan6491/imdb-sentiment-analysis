from flask import Flask, render_template, request
import joblib

app = Flask(__name__)


model = joblib.load("naive_bayes.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    review = ""

    if request.method == "POST":

        review = request.form.get("review", "").strip()

        if review:

            result = model.predict([review])[0]

            if result == 1:
                prediction = "Positive"
            else:
                prediction = "Negative"

    return render_template(
        "index.html",
        prediction=prediction,
        review=review
    )


if __name__ == "__main__":
    app.run(debug=True)