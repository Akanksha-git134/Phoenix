def assess_risk(job_description):
    """
    Rule-based risk assessment.
    Does NOT change the ML prediction.
    """

    text = job_description.lower()

    score = 0
    reasons = []

    rules = {

        "registration fee": 3,
        "processing fee": 3,
        "application fee": 3,
        "security deposit": 3,
        "refundable": 2,
        "whatsapp": 2,
        "telegram": 2,
        "urgent hiring": 2,
        "limited vacancies": 1,
        "no interview": 3,
        "no experience": 1,
        "immediate joining": 2,
        "appointment letter": 1,
        "pay now": 3,
        "today only": 2

    }

    for keyword, weight in rules.items():

        if keyword in text:

            score += weight
            reasons.append(keyword)

    # Unrealistic salary

    if (
        "₹90,000" in text
        or "₹95,000" in text
        or "100000" in text
        or "1 lakh" in text
    ):

        score += 3
        reasons.append("Unusually high salary")

    # Final Risk

    if score >= 8:
        level = "HIGH"

    elif score >= 4:
        level = "MEDIUM"

    else:
        level = "LOW"

    return level, reasons