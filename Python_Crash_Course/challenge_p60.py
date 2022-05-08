counting_1 = []
for count in range(1, 21):
    counting_1.append(count)
print(counting_1)

counting_2 = [count for count in range(1, 21)]
print(counting_2)

million = [count for count in range(1, 1_000_000)]
print(million)
print(sum(million))