
a = int(input())
h = int(a / 3600)
m = int((a % 3600) / 60)
s = int((a % 3600) % 60)

print("{0}{1}{2}{3}{4}".format(h,":", m, ":", s))
