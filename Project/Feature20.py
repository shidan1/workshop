import re

def numberOfSuspiciousTagStrings(path):
    f = open(path)
    script = f.read()
    regex = "(?i)<\/?\w+((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[^'\">\s]+))?)+\s*|\s*)\/?>"
    tags = set()
    for match in re.finditer(regex, script):
        tags.add(repr(match.group()))
    return len(tags)

print(numberOfSuspiciousTagStrings('scripts/workshop_ex8.js'))

