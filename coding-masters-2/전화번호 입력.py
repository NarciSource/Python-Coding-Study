import re
print("valid" if re.compile("^010-\d{4}-\d{4}$").match(input()) else "invalid")