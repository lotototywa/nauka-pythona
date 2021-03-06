def hello(name):
    if name != "" :
        name = name.capitalize()
        return f"Hello {name}"
    else:
        return "Hello World"
    # jeśli name nie jest pustym stringiem to
        # zamień name na name.capitalize()
        # zwróć Hello {name}!
    