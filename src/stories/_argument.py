def arguments(*names):
    def decorator(f):
        f.arguments = list(names)
        return f

    return decorator
