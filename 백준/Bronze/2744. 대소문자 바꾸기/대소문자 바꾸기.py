original = input().strip()
change = list()
for o in original:
    if(o.isupper()):
        change.append(o.lower())
    else:
        change.append(o.upper())
for c in change:
    print(c, end="")
print("")