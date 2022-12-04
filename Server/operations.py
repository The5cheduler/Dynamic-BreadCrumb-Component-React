
def getAllimmdieateChildren(data):
    stack = list(data.items())
    for key, value in data.items():
        if key == "type" and value == "dir":
            return stack