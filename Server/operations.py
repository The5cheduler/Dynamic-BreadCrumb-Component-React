
# def getAllimmdieateChildren(data, path_values : list()):
#     children = list()

#     for key in data.keys(): 
#         if key == "children": 
#             children.append(*data[key].keys())

# # check if children already exist in path
#             path_len = len(path_values)
#             for i in path_values: 
#                 child_data = data[key].values()
#                 print(getAllimmdieateChildren(data[key][i], path_values = [i]))
#                 # children.append(*getAllimmdieateChildren(data[key][i],i))
#     return children

def getAllimmdieateChildren(data):
    children = list()

    for key, value in data.items(): 
        if key == "type" and value == "dir":
            child = [*data["children"].keys()]
            print(child)
            # children.extend(*data["children"].keys())
        if isinstance(value, dict):
            getAllimmdieateChildren(value)
            # print(key, ": ", value)
            
    return children

