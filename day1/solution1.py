data = open('input').readlines()

left_numbers = []
right_numbers = []

distances = []

for line in data:
    numbers = line.strip().split('   ')
    left_numbers.append(int(numbers[0]))
    right_numbers.append(int(numbers[1]))

left_numbers.sort()
right_numbers.sort()

for l, r in zip(left_numbers, right_numbers):
    distances.append(abs(l - r))

print(distances)
print(sum(distances))

    