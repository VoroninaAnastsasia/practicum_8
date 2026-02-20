text = input()

maxsymb = 0
symb = 0
pre_ch = ''

for ch in text:
    if ch == pre_ch:
        symb += 1
    else:
        symb = 1
    maxsymb = max(maxsymb,symb)
    pre_ch = ch

print(maxsymb)
        
