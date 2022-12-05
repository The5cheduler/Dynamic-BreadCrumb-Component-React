
def getAllimmdieateChildren(data, pathString : str = None):
    children = set()       
    for key in data.keys():
        if key == "children":
            children.add(*data[key].keys())
        if pathString is not None and pathString in children:
            children.add(*getAllimmdieateChildren(data[key][pathString]))           
    return children

