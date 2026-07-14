import re
import string
import html
import contractions
def clean_text(text):

    # Handle missing values
    if not isinstance(text, str):
        return ""

    text = html.unescape(text)

    text = contractions.fix(text)

    text = text.lower()

    # Remove HTML tags
    text = re.sub(r"<.*?>", " ", text)

    # Remove URLs
    text = re.sub(r"https?://\S+|www\.\S+",
        " ",
        text,
    )

    # Remove email addresses
    text = re.sub(
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
        " ",
        text,
    )

    # Replace periods with spaces
    text = re.sub(r"\.", " ", text)

    # Replace hyphens with spaces
    text = re.sub(r"-", " ", text)

    # Remove numbers
    text = re.sub(r"\d+", " ", text)

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text