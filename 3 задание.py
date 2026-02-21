text = input()

text = text.lower()
unique_symb = ''
for ch in text: 
  if ch.isalpha(): 
    unique_symb += ch

print(len(set(unique_symb)))
