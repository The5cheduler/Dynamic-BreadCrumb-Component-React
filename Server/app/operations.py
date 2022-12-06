def getfirstchild(data):
    result = {}
    for key, value in data.items(): 
        if key == "type" and value == "dir":
            result["currentNodeType"] = value
            result["childrenNodes"] = [*data["children"].keys()]
            return result

def findkeys(node, kv):
    if isinstance(node, list):
        for i in node:
            for x in findkeys(i, kv):
               yield x
    elif isinstance(node, dict):
        if kv in node:
            yield node[kv]
        for j in node.values():
            for x in findkeys(j, kv):
                yield x

def pathIsPath(data):
    result = dict(getfirstchild(data))
    result["previousNodes"] = []
    result["currentNode"] = None
    return result





