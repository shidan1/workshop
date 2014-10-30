"""
A Static Malicious JavaScript Detection Using SVM - Feature 20:
the number of suspicious tag strings
"""

import re

def numberOfSuspiciousTagStrings(script):
    regex = "(?i)<\/?\w+((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[^'\">\s]+))?)+\s*|\s*)\/?>"
    tags = set()
    for match in re.finditer(regex, script):
        tags.add(repr(match.group()))
    return len(tags)

def run(script):
    return numberOfSuspiciousTagStrings(script)