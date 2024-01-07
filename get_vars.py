def get_vars(ban):
    name = ban["name"]
    authid = ban["authid"]
    length = ban["length"]
    reason = ban["reason"]
    return name, authid, length, reason
