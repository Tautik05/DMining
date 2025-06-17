import re
text = "abc# ax#a# aadf# a123# aa# aaB# a##"
pattern = r'a.{3}#'
matches = re.findall(pattern, text)
print(matches)
print("Number of occurrences:", len(matches))