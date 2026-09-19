# numbers = [3, 5, 3, 8, 5, 3, 9, 8, 5]
# frequency = {}
# for number in numbers:
#     if number in frequency:
#         frequency[number] += 1
#     else:
#         frequency[number] = 1
# print("Frequency:")
# for number, count in frequency.items():
#     print(number, "-", count)

#exercise 2
# numbers = [4, 7, 2, 7, 9, 4, 7, 2, 7]
# frequency = {}
# for number in numbers:
#     if number in frequency:
#         frequency[number] += 1
#     else:
#         frequency[number] = 1
# most_frequent = numbers[0]
# for number in frequency:
#     if frequency[number] > frequency[most_frequent]:
#         most_frequent = number
# print("Most frequent number:", most_frequent)
# print("Frequency:", frequency[most_frequent])

#exercise 3
# numbers = [1, 4, 6, 2, 4, 8]
# seen = set()
# duplicate_found = False
# for number in numbers:
#     if number in seen:
#         print("Duplicate found:", number)
#         duplicate_found = True
#         break
#     seen.add(number)
# if duplicate_found == False:
#     print("No duplicates")

#exercise 4
numbers = [3, 8, 12, 4, 7]
target = 11
seen = {}
for number in numbers:
    needed = target - number
    if needed in seen:
        print("Pair:", needed, number)
        break
    seen[number] = True