def analyze_password(password,
                     min_length=8,
                     require_digit=True,
                     require_upper=True,
                     require_symbol=False,
                     banned_words=None):

    symbols = "!@#$%^&*()-_=+[]{};:,.?"

    if banned_words is None:
        banned_words = ['heslo', 'password', '1234']

    total_rules = 0
    passed_rules = 0
    missing_rules = []

    # pravidlo: minimální délka
    total_rules += 1
    if len(password) >= min_length:
        passed_rules += 1
    else:
        missing_rules.append("min_length")

    # pravidlo: číslice
    if require_digit:
        total_rules += 1
        if any(c.isdigit() for c in password):
            passed_rules += 1
        else:
            missing_rules.append("digit")

    # pravidlo: velké písmeno
    if require_upper:
        total_rules += 1
        if any(c.isupper() for c in password):
            passed_rules += 1
        else:
            missing_rules.append("upper")

    # pravidlo: symbol
    if require_symbol:
        total_rules += 1
        if any(c in symbols for c in password):
            passed_rules += 1
        else:
            missing_rules.append("symbol")

    # pravidlo: zakázaná slova
    total_rules += 1
    lower_password = password.lower()
    if any(word in lower_password for word in banned_words):
        missing_rules.append("banned_word")
    else:
        passed_rules += 1

    score_percent = int((passed_rules / total_rules) * 100)
    is_strong = len(missing_rules) == 0

    return is_strong, score_percent, missing_rules
