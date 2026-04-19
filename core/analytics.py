def calculate_error_rate(key1, key2):
    if len(key1) == 0:
        return 1.0

    errors = 0

    for a, b in zip(key1, key2):
        if a != b:
            errors += 1

    return errors / len(key1)


def security_status(rate, threshold=0.15):
    if rate > threshold:
        return "⚠️ Eve Detected"
    return "✅ Secure Communication"