from random import*
r = randrange(6)
C = 'o '
s = '-----\n|'+C[r < 1]+' '+C[r < 3]+'|\n|'+C[r < 5]
print (s+C[r & 1]+s[::-1])
