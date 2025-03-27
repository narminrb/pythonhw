# e = input('Enter the number ')


# # new = e.removeprefix('+994')

# if e.startswith('994') and len(e) == 12:
#     new = e.removeprefix('+994')
#     if new.startswith('55'):
#         print('Bakcell')

# elif e.startswith('+994') and len(e) == 13:
#     new = e.removeprefix('994')
#     if new.startswith('55'):
#         print('Bakcell')

# elif e.startswith('05') and len(e) == 10:
#     new = e.removeprefix('0')
#     if new.startswith('55'):
#         print('Bakcell')

# elif e.startswith('55') and len(e) == 9:
#         print('Bakcell')


# elif e.startswith('+994') and len(e) == 13:
#     new = e.removeprefix('+994')
#     if new.startswith('77') or new.startswith('70'):
#         print('Nar')

# elif e.startswith('07') and len(e) == 10:
#     new = e.removeprefix('0')
#     if new.startswith('77') or new.startswith('70'):
#         print('Nar')


# elif new.startswith('77')  or new.startswith('70') and len(e) == 9:
#         print('Nar')

# else:
#      print('Printed number is not right')


e = input('Enter the number: ')

if e.startswith('+994') and len(e) == 13:
    new = e.removeprefix('+994')
    if new.startswith('55'):
        print('Bakcell')
    elif new.startswith('77') or new.startswith('70'):
        print('Nar')


elif e.startswith('994') and len(e) == 12:
    new = e.removeprefix('994')
    if new.startswith('55'):
        print('Bakcell')
    elif new.startswith('77') or new.startswith('70'):
        print('Nar')


elif e.startswith('05') and len(e) == 10:
    new = e.removeprefix('0')
    if new.startswith('55'):
        print('Bakcell')
    elif new.startswith('77') or new.startswith('70'):
        print('Nar')

elif e.startswith('55') and len(e) == 9:
    print('Bakcell')

elif e.startswith('07') and len(e) == 10:
    new = e.removeprefix('0')
    if new.startswith('77') or new.startswith('70'):
        print('Nar')

else:
    print('Printed number is not right')
