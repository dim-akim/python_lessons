import sys
import re
pattern = r"\b(\w{1})(\w{1})"
replacement = r"\2\1"

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, replacement, line))

