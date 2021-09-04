import re

class_patterns = [
    re.compile(r"(class=\")([\w\s\-]+)(\")"),  # Classes from HTML
    re.compile(r"(\.)([\w\-]+)(,|\s)"),  # Classes from CSS
]

id_patterns = [
    re.compile(r"(id=\")([\w\s\-]+)(\")"),  # Classes from HTML
    re.compile(r"(#)([\w\-]+)(,|\s)"),  # Classes from CSS
]
