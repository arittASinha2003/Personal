from random import sample as s

print("".join(s([chr(c) for c in range(33,127)], int(input()))))
