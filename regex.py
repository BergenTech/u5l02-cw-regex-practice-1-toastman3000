import re

# 1. Match the word "cat" in a string.
pattern = r""
text = "The cat sat on the mat."
match = re.search(pattern, text)
print(match.group() if match else "No match")

'''

# 2. Match "cat" regardless of its case.
pattern = r""
text = "The Cat sat on the mat."
match = re.search(pattern, text)
print(match.group() if match else "No match")

# 3. Match any three-letter word ending with 'at'.
pattern = r""
text = "The cat sat on the mat."
matches = re.findall(pattern, text)
print(matches)

# 4. Match any sequence of digits.
pattern = r""
text = "There are 123 apples."
matches = re.findall(pattern, text)
print(matches)

# 5. Match sequences not containing digits.
pattern = r""
text = "There are 123 apples."
matches = re.findall(pattern, text)
print(matches)

# 6. Match "cat" as a whole word.
pattern = r""
text = "The cat sat on the concatenate."
matches = re.findall(pattern, text)
print(matches)

# 7. Match "cat" or "bat".
pattern = r""
text = "The cat and the bat."
matches = re.findall(pattern, text)
print(matches)

# 8. Match any word starting with a letter in the range 'a' to 'c'.
pattern = r""
text = "cat, bat, rat, mat."
matches = re.findall(pattern, text)
print(matches)

# 9. Match any three-letter word not starting with 'b' or 'c'.
pattern = r""
text = "cat, bat, rat, mat."
matches = re.findall(pattern, text)
print(matches)

# 10. Check if the string starts with "The".
pattern = r""
text = "The cat sat."
match = re.search(pattern, text)
print(match.group() if match else "No match")

# 11. Check if the string ends with "sat."
pattern = r""
text = "The cat sat."
match = re.search(pattern, text)
print(match.group() if match else "No match")

# 12. Match "color" and "colour".
pattern = r""
text = "Both color and colour are correct."
matches = re.findall(pattern, text)
print(matches)

# 13. Match "o" followed by any number of "o"s.
pattern = r""
text = "The book is on the stool."
matches = re.findall(pattern, text)
print(matches)

# 14. Match "o" followed by one or more "o"s.
pattern = r""
text = "The book is on the stool."
matches = re.findall(pattern, text)
print(matches)

# 15. Match "o" exactly twice.
pattern = r""
text = "The book is on the stool."
matches = re.findall(pattern, text)
print(matches)

# 16. Match "o" between two and three times.
pattern = r""
text = "The book is on the stool."
matches = re.findall(pattern, text)
print(matches)

# 17. Match the smallest possible string of "o"s.
pattern = r""
text = "The booooook is long."
match = re.search(pattern, text)
print(match.group() if match else "No match")

# 18. Match and group "cat" or "bat".
pattern = r""
text = "The cat in the hat chased the bat."
matches = re.findall(pattern, text)
print(matches)

# 19. Match and capture nested groups.
pattern = r""
text = "The number is 123-456-7890."
match = re.search(pattern, text)
print(match.groups() if match else "No match")

# 20. Match repeated words.
pattern = r""
text = "The the cat sat sat on the the mat."
matches = re.findall(pattern, text)
print(matches)

# 21. Match simple email addresses.
pattern = r""
text = "Contact us at info@example.com."
matches = re.findall(pattern, text)
print(matches)

# 22. Match web URLs.
pattern = r""
text = "Visit https://www.example.com for more info."
matches = re.findall(pattern, text)
print(matches)

# 23. Match phone numbers in various formats.
pattern = r""
text = "Call 123-456-7890 or (123) 456-7890."
matches = re.findall(pattern, text)
print(matches)

# 24. Case-insensitive match of "python".
pattern = r""
text = "Python is fun. python is powerful."
matches = re.findall(pattern, text)
print(matches)

# 25. Split a string at each space or comma.
pattern = r""
text = "The,quick brown,fox jumps"
words = re.split(pattern, text)
print(words)

# 26. Replace "cat" with "dog".
pattern = r""
text = "The cat sat on the mat."
new_text = re.sub(pattern, "dog", text)
print(new_text)

# 27. Match "color" or "colour" without capturing the group.
pattern = r""
text = "Both color and colour are correct."
matches = re.findall(pattern, text)
print(matches)

# 28. Match "John" only if followed by "Smith".
pattern = r""
text = "John Smith vs. John Doe"
matches = re.findall(pattern, text)
print(matches)

# 29. Match "Smith" only if preceded by "John".
pattern = r""
text = "John Smith vs. John Doe"
matches = re.findall(pattern, text)
print(matches)

# 30. Match any Unicode letter.
pattern = r""
text = "Résumé"
matches = re.findall(pattern, text, re.UNICODE)
print(matches)

# 31. Match hexadecimal numbers (e.g., #a3c113).
pattern = r""
text = "The color code is #a3c113."
matches = re.findall(pattern, text)
print(matches)

# 32. Match words containing 'ing'.
pattern = r""
text = "Playing, singing, and swimming are fun."
matches = re.findall(pattern, text)
print(matches)

# 33. Match sentences ending with a question mark.
pattern = r""
text = "What is your name? How old are you?"
matches = re.findall(pattern, text)
print(matches)

# 34. Match all words starting with 's' and ending with 'e'.
pattern = r""
text = "Store and sell are similar words."
matches = re.findall(pattern, text)
print(matches)

# 35. Match all HTML tags.
pattern = r""
text = "<html><head><title>Title</title></head></html>"
matches = re.findall(pattern, text)
print(matches)

# 36. Match all Twitter handles (e.g., @username).
pattern = r""
text = "Follow me on Twitter @example_user."
matches = re.findall(pattern, text)
print(matches)

# 37. Match dates in the format YYYY-MM-DD.
pattern = r""
text = "Today's date is 2023-01-01."
matches = re.findall(pattern, text)
print(matches)

# 38. Match all words longer than 5 letters.
pattern = r""
text = "Regular expressions are powerful."
matches = re.findall(pattern, text)
print(matches)

# 39. Match all floating-point numbers.
pattern = r""
text = "The temperature is -3.14 degrees."
matches = re.findall(pattern, text)
print(matches)

# 40. Match all XML tags.
pattern = r""
text = "<note><to>User</to><from>Admin</from></note>"
matches = re.findall(pattern, text)
print(matches)
'''
