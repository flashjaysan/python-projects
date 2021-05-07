lines = 10
for line in range(lines):
    print(' ' * (lines - 1 - line) + '*' * (line * 2 + 1))
for line in range(1, lines):
    print(' ' * (line) + '*' * ((lines - line) * 2 - 1))
