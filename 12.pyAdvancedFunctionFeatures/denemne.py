def azalt(s):
    if len(s) == 0:
        return s
    else:
        print(s)
        return azalt(s[1:])

print(azalt('istihza'))