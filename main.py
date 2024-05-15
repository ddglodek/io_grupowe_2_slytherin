def waluta_str_na_dict(input_str):
    
    currency_dict = {
        "galeon": 0,
        "sykl": 0,
        "knut": 0
    }

    tokens = input_str.split()

    for i in range(0, len(tokens), 2):
        value = int(tokens[i])
        key = tokens[i + 1]

        if key.startswith('g'):
            currency_dict["galeon"] = value
        elif key.startswith('s'):
            currency_dict["sykl"] = value
        elif key.startswith('k'):
            currency_dict["knut"] = value

    return currency_dict

