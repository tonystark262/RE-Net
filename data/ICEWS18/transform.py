with open('train.txt', 'r') as f:
    a = [k.strip().split('\t') for k in f.readlines()]

with open('train.txt', 'w') as f:
    for k in a:
        f.write(f'{k[0]}\t{k[1]}\t{k[2]}\t{k[-1]}\t0\n')

with open('valid.txt', 'r') as f:
    a = [k.strip().split('\t') for k in f.readlines()]

with open('valid.txt', 'w') as f:
    for k in a:
        f.write(f'{k[0]}\t{k[1]}\t{k[2]}\t{k[-1]}\t0\n')

with open('test.txt', 'r') as f:
    a = [k.strip().split('\t') for k in f.readlines()]

with open('test.txt', 'w') as f:
    for k in a:
        f.write(f'{k[0]}\t{k[1]}\t{k[2]}\t{k[-1]}\t0\n')