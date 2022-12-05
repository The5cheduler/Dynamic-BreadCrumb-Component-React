
def getAllimmdieateChildren(data, pathString : str = None):
    children = list()
    path_values = pathString.split("/")  
    for key in data.keys(): 
        if key == "children": 
            children.append(*data[key].keys())
# check if children already exist in path
        if not pathString: 
            print(*getAllimmdieateChildren(data[key][pathString]))
            children.append(*getAllimmdieateChildren(data[key][pathString])) 
                  
    return children

