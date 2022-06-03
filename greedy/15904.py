import sys
ucpc = sys.stdin.readline().rstrip('\n')
idx = ucpc.find('U')
idx2 = -1
if idx != -1:
    idx2 = ucpc[idx:].find('C')
    idx = idx + idx2
    if idx2 != -1:
        idx2 = ucpc[idx:].find('P')
        idx = idx + idx2
        if idx2 != -1:
            idx2 = ucpc[idx:].find('C')
print('I hate UCPC' if idx2 == -1 else 'I love UCPC')