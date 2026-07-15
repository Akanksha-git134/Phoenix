import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


def get_available_keys():
    """
    Reads all Gemini API keys from the .env file.

    Supported:
    GEMINI_API_KEY_1
    GEMINI_API_KEY_2
    ...
    GEMINI_API_KEY_10
    """

    keys = []

    for i in range(1, 11):
        key = os.getenv(f"GEMINI_API_KEY_{i}")

        if key and key.strip():
            keys.append(key.strip())

    return keys


def generate_explanation(job_description, prediction, confidence):
    """
    Generates an AI explanation while preserving
    the Machine Learning prediction.
    """

    keys = get_available_keys()

    if not keys:
        return (
            "AI explanation is unavailable because no Gemini API key "
            "has been configured."
        )

    prompt = f"""
You are Phoenix AI.

A Machine Learning model has already analyzed this job posting.

Prediction:
{prediction}

Confidence:
{confidence}%

Job Posting:
{job_description}


Rules:

- NEVER change or contradict the Machine Learning prediction.

- Explain the reasoning naturally.

- Mention both positive and suspicious indicators when relevant.

-If the prediction is "Legitimate Job" or "Suspicious Job", mention any warning signs without contradicting the prediction. Mention that users should verify those details.

- Do NOT say "the model predicted..."

- Speak as Phoenix AI.

- Keep the explanation around 80–100 words.

- The safety recommendation must relate to the job posting.

- Do not give generic advice unless no specific recommendation is possible.

- Never describe the job as fake if the prediction is "Real Job".

- Never describe the job as legitimate if the prediction is "Fake Job".

- Do not mention probabilities.

- Do not mention AI limitations.

Output Format (follow exactly):

Overview:
Write exactly 2 sentences.

Key Indicators:
• Exactly 3 bullet points.
• Each bullet should be one short sentence.

Safety Recommendation:
Write exactly 1 sentence.

Do not add any extra headings.
Do not use bold.
Do not use markdown except the • bullet.
"""

    MODELS = [
        "gemini-flash-lite-latest",
        "gemini-flash-latest",
        "gemini-3.5-flash",
        "gemini-pro-latest",
    ]

    # Try every API key
    for api_key in keys:

        print(f"\nUsing API key ending with ...{api_key[-6:]}")

        genai.configure(api_key=api_key)

        # Try every model
        for model_name in MODELS:

            try:

                print(f"Trying model: {model_name}")

                model = genai.GenerativeModel(model_name)

                response = model.generate_content(prompt)

                if (
                    response
                    and hasattr(response, "text")
                    and response.text
                    and response.text.strip()
                ):
                    print(f"Success with {model_name}")
                    return response.text.strip()

            except Exception as e:

                print(f"{model_name} failed")
                print(e)
                print("-" * 60)

                continue

    return (
        "AI explanation is temporarily unavailable. "
        "The Machine Learning prediction remains valid."
    )