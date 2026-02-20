count = 0

def luck(ticket):
    if len(ticket) % 2 != 0:
        return False

    half = len(ticket) // 2
    s1 = 0
    s2 = 0
    for digit in ticket[:half]:
        s1 += int(digit)
    for digit in ticket [half:]:
        s2 += int(digit)
    return s1 == s2

tickets = input().split()

for ticket in tickets:
    count += 1
    if luck(ticket):
        print(count)
        break


            
           
