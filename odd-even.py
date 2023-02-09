INPUT_NUM = input('Please type a number: ')

def determine_even(num):
    if int(num) % 2 == 0:
        return 'This is an even number.'
    else:
        return 'This is an odd number.'
    

try:
    print(determine_even(INPUT_NUM))
except ValueError:
    print(f'This is not a whole number: {INPUT_NUM}. Use a whole number!')
