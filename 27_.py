def output(s, l):
    if l == 0:
        return None
    print(s[l-1])
    output(s, l-1)
s = input()
l = len(s)
output(s,l)