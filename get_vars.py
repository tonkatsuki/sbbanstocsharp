from datetime import datetime


def get_vars(ban):
    authid = ban["authid"]
    name = ban["name"]
    created = datetime.utcfromtimestamp(ban["created"])
    ends = datetime.utcfromtimestamp(ban["ends"])
    length = ban["length"]
    reason = ban["reason"]

    return authid, name, created, ends, length, reason
