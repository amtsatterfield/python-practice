LIST = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
INPUT_NUM = input('Type any integer: ')

NEW_LIST = [num for num in LIST if num < int(INPUT_NUM)]

print(f'These are the numbers less than {INPUT_NUM}: {NEW_LIST}')

