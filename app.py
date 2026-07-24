from flask import Flask, render_template, request
import joblib
from utils.validate_input import validate_job_post
from utils.text_preprocessing import clean_text
from utils.gemini_explainer import generate_explanation
from utils.risk_assessment import assess_risk

app = Flask(__name__)
# ----------------------------
# Load ML Model
# ----------------------------
try:
    model = joblib.load("trained_models/fake_job_detector.pkl")
    vectorizer = joblib.load("trained_models/tfidf_vectorizer.pkl")
except Exception as e:
    print("Error loading model:", e)
    model = None
    vectorizer = None


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    probability = None
    confidence_label = None
    confidence_color = None
    ai_explanation = None
    safety_tips = []
    error_message = None
    risk_level = None
    risk_reasons = []

    if request.method == "POST":

        if model is None or vectorizer is None:

            error_message = (
                "Machine Learning model could not be loaded."
            )

        else:

            try:

                job_description = request.form["job_description"].strip()

                is_valid, error_message = validate_job_post(job_description)

                if not is_valid:

                    return render_template(
                        "index.html",
                        error_message=error_message,
                        prediction=None,
                        probability=None,
                        confidence_label=None,
                        confidence_color=None,
                        ai_explanation=None,
                        safety_tips=[]
                    )

                cleaned_text = clean_text(job_description)

                vector = vectorizer.transform([cleaned_text])

                pred = model.predict(vector)[0]
                prob = model.predict_proba(vector)[0]

                probability = round(max(prob) * 100, 2)

                risk_level, risk_reasons = assess_risk(job_description)

                # ------------------------------
                # Three-Level Prediction
                # ------------------------------

                if pred == 1:
                    if probability >= 85 or risk_level == "HIGH":
                        prediction = "Fraudulent Job"
                    else:
                        prediction = "Suspicious Job"
                else:
                    if risk_level == "HIGH":
                        prediction = "Suspicious Job"

                    elif risk_level == "MEDIUM":
                         prediction = "Suspicious Job"
                         
                    else:
                        prediction = "Legitimate Job"

                # ----------------------------
                # Confidence Label
                # ----------------------------

                if probability >= 85:
                    confidence_label = "Very High Confidence"
                    confidence_color = "green"

                elif probability >= 70:
                    confidence_label = "High Confidence"
                    confidence_color = "green"

                elif probability >= 55:
                    confidence_label = "Moderate Confidence"
                    confidence_color = "orange"

                else:
                    confidence_label = "Low Confidence"
                    confidence_color = "red"

                # ----------------------------
                # Gemini Explanation
                # ----------------------------

                try:

                    ai_explanation = generate_explanation(
                        job_description,
                        prediction,
                        probability
                    )

                except Exception:

                    ai_explanation = (
                        "AI explanation is temporarily unavailable. "
                        "The Machine Learning prediction remains valid."
                    )

                # ----------------------------
                # Safety Tips
                # ----------------------------

                if prediction == "Legitimate Job":

                    safety_tips = [
                        "Verify the company website before applying.",
                        "Apply only through the official careers page.",
                        "Avoid sharing sensitive personal information too early."
                    ]

                elif prediction == "Suspicious Job":

                    safety_tips = [
                        "Never pay a registration or processing fee.",
                        "Verify the company's existence independently.",
                        "Avoid communicating outside official company channels."
                    ]

                else:

                    safety_tips = [
                        "Do not apply to this job posting.",
                        "Never send money or purchase training kits.",
                        "Report the listing on the job portal.",
                        "Block further communication with the recruiter.",
                        "Apply only through verified company websites.                    "
                    ]

            except Exception as e:

                print("Prediction Error:", e)

                error_message = (
                    "Something went wrong while analyzing the job posting."
                )

    return render_template(
        "index.html",
        prediction=prediction,
        probability=probability,
        confidence_label=confidence_label,
        confidence_color=confidence_color,
        ai_explanation=ai_explanation,
        safety_tips=safety_tips,
        risk_level=risk_level,
        risk_reasons=risk_reasons,
        error_message=error_message
    )


if __name__ == "__main__":
    app.run(debug=False)