from datetime import datetime
import re


def sanitize_name(name):
    sanitized = re.sub(r"(--.*$)|(')|(;)", "", name, flags=re.MULTILINE)
    sanitized = re.sub(r"[^a-zA-Z0-9\s]", "", sanitized)
    return sanitized


def sanitize_reason(reason):
    sanitized = re.sub(r"(--.*$)|(')|(;)", "", reason, flags=re.MULTILINE)
    return sanitized


def get_vars(ban):
    authid = ban["authid"]
    name = sanitize_name(ban["name"])
    created = datetime.utcfromtimestamp(ban["created"])
    ends = datetime.utcfromtimestamp(ban["ends"])
    length = ban["length"]
    reason = sanitize_reason(ban["reason"])

    return authid, name, created, ends, length, reason
