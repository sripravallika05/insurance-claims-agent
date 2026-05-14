def generate_reasoning(route):

    reasons = {
        "Fast-track":
            "Estimated damage is below 25,000.",

        "Manual Review":
            "Mandatory fields are missing.",

        "Investigation Flag":
            "Fraud-related keywords detected in claim description.",

        "Specialist Queue":
            "Claim involves injury handling.",

        "Standard Review":
            "Claim requires standard assessment."
    }

    return reasons.get(route, "")