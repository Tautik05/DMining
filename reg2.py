import re
text = "Hello, how are you? Heyo, Heo, Heo! Heo"
pattern = r'He.*o'
matches = re.findall(pattern, text)
print(matches)