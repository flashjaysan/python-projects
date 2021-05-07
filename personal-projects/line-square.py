lines = 10
for line in range(lines):
    if line == 0 or line == lines - 1:
        print('*' * lines)
    else:
        print('*' + ' ' * (lines - 2) + '*')
