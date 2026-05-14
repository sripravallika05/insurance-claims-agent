REQUIRED_FIELDS = [
    "policy_number",
    "policyholder_name",
    "incident_date",
    "claim_type",
    "estimated_damage"
]


def validate_fields(data):

    missing = []

    for field in REQUIRED_FIELDS:

        if field not in data or not data[field]:
            missing.append(field)

    return missing