import re


def validate_job_post(text):
    """
    Validates whether the submitted text
    looks like a genuine job posting.
    """

    text = text.strip()

    # Empty
    if not text:
        return False, "Please enter a job description."

    # Too short
    words = text.split()

    if len(words) < 5:
        return (
            False,
            "The job description is too short for reliable analysis."
        )

    # Too many numbers
    letters = len(re.findall(r"[A-Za-z]", text))
    digits = len(re.findall(r"\d", text))

    if letters < 20:
        return (
            False,
            "The submitted text doesn't appear to contain enough descriptive content."
        )

    if digits > letters:
        return (
            False,
            "The submitted text appears to contain mostly numbers instead of a job description."
        )

    # Repeated word spam
    unique_words = len(set(word.lower() for word in words))

    if unique_words < len(words) * 0.30:
        return (
            False,
            "The submitted text appears repetitive or invalid."
        )

    # Looks OK
    return True, ""