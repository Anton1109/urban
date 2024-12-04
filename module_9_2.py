first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']


first_result = [len(s) for s in first_strings if len(s) >= 5]


second_result = []
for f in first_strings:
    for s in second_strings:
        if len(f) == len(s):
            second_result.append((f, s))


third_result = {}
for f in first_strings + second_strings:
    if len(f) % 2 == 0:
        third_result[f] = len(f)

print(first_result)
print(second_result)
print(third_result)