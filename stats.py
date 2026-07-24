scores = [3, 5, 2, 5, 4, 3, 5]
total = 0

for score in scores:
    total = total + score

average = total / len(scores)

print("Scores:", scores)
print("Total:", total)
print("Average:", average)
print("Highest:", max(scores))
print("Lowest:", min(scores))