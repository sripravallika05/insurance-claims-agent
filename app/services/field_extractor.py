import re


def extract_fields(text: str):

    data = {}

    patterns = {
        "policy_number": r"POLICY NUMBER[:\s]+([A-Z0-9-]+)",

        "incident_date": r"DATE OF LOSS.*?(\d{2}/\d{2}/\d{4})",

        "policyholder_name": r"NAME OF INSURED.*?\n([A-Z\s]+)",

        "vehicle_year": r"YEAR\s+(\d{4})",

        "claim_type": r"CLAIM TYPE[:\s]+([A-Z\s]+)",

        "estimated_damage": r"ESTIMATE AMOUNT[:\s]+\$?([\d,]+)"
    }

    for field, pattern in patterns.items():

        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            data[field] = match.group(1).strip()

    description_match = re.search(
        r"DESCRIPTION OF ACCIDENT(.*?)(OWNER'S NAME AND ADDRESS)",
        text,
        re.DOTALL
    )

    if description_match:
        data["description"] = description_match.group(1).strip()

    return data