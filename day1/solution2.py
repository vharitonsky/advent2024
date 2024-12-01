from collections import defaultdict


data = open('input').readlines()

left_numbers = []
right_numbers = defaultdict(int)

similarities = []

for line in data:
    numbers = line.strip().split('   ')
    left_numbers.append(int(numbers[0]))
    right_numbers[int(numbers[1])] += 1

for l in left_numbers:
    similarities.append(right_numbers[l] * l)

print(similarities)
print(sum(similarities))

    