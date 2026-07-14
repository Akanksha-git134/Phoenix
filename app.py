from flask import Flask, render_template, request
import joblib

from utils.text_preprocessing import clean_text

from utils.lime_explainer import generate_lime_explanation

app = Flask(__name__)

model = joblib.load("trained_models/fake_job_detector.pkl")
vectorizer = joblib.load("trained_models/tfidf_vectorizer.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    probability = None
    ai_explanation = None
    safety_tips = []
    lime_explanation = []

    if request.method == "POST":

        job_description = request.form["job_description"]

        cleaned_text = clean_text(job_description)

        vector = vectorizer.transform([cleaned_text])

        pred = model.predict(vector)[0]

        prob = model.predict_proba(vector)[0]

        prediction = "Fake Job" if pred == 1 else "Real Job"

        lime_explanation = generate_lime_explanation(

            job_description,

            model,

            vectorizer

        )

        probability = round(max(prob) * 100, 2)

        # ------------------------------
        # Temporary AI Explanation
        # ------------------------------

        if prediction == "Real Job":

            ai_explanation = (
                "Phoenix detected professional language, realistic job "
                "requirements, and no major fraud indicators. "
                "This posting appears to be genuine."
            )

            safety_tips = [
                "Verify the company website.",
                "Apply through the official careers page.",
                "Avoid sharing sensitive information too early."
            ]

        else:

            ai_explanation = (
                "Phoenix detected multiple suspicious indicators "
                "commonly associated with fake job postings."
            )

            safety_tips = [
                "Do not pay any registration fee.",
                "Verify the company independently.",
                "Avoid communicating outside official channels."
            ]

    return render_template(

        "index.html",

        prediction=prediction,

        probability=probability,

        ai_explanation=ai_explanation,

        safety_tips=safety_tips,

        lime_explanation=lime_explanation

    )

if __name__ == "__main__":
    app.run(debug=True)