import re
text = "The cat sat on the mat. A boat floated by the dock. Bats sleep upside down."
pattern = r'\b[aAbBfF]\w*t\b'
matches = re.findall(pattern, text, re.IGNORECASE)
print(matches)