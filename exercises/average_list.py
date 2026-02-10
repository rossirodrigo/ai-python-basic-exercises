average_list = [8.9, 7.5, 4.2, 1.4, 9.5]

for i, average in enumerate(average_list):
    average_list[i] = 10 if average > 10 else average + 1

print(average_list)