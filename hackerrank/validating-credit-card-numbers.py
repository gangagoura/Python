import re

start_with_456 = lambda x: x[0]=='4' or x[0]=='5' or x[0]=='6'

contain_16_digits = lambda x: bool(re.fullmatch(r'\d{16}', ''.join(x.split('-'))))

groups_of_4 = lambda x: all([len(i)==4 for i in x.split('-') if '-' in x])
    
repeating_characters = lambda x: not(bool(re.search(r'(\d)\1{3,}', ''.join(x.split('-')))))
    
tests = [start_with_456, contain_16_digits, groups_of_4, repeating_characters]

N = int(input())
for _ in range(N):
    s = input()
    if all(map(lambda x: x(s), tests)):
        print('Valid')
    else:
        print('Invalid')
