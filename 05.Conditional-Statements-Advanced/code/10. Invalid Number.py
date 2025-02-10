number = int(input())
is_valid = False
if number >= 100 and number <= 200 or number == 0:
    is_valid = True
if not is_valid:
    print('invalid')

#number = int(input())
#valid = 100 <= number <= 200 or number == 0
#if not valid:
#    print('invalid')
