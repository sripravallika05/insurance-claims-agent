def determine_route(data, missing_fields):

    description = data.get("description", "").lower()

    claim_type = data.get("claim_type", "").lower()

    estimated_damage = data.get("estimated_damage", "0")

    estimated_damage = estimated_damage.replace(",", "")

    try:
        estimated_damage = float(estimated_damage)
    except:
        estimated_damage = 0

    fraud_keywords = [
        "fraud",
        "staged",
        "inconsistent"
    ]

    if any(word in description for word in fraud_keywords):
        return "Investigation Flag"

    if missing_fields:
        return "Manual Review"

    if claim_type == "injury":
        return "Specialist Queue"

    if estimated_damage < 25000:
        return "Fast-track"

    return "Standard Review"