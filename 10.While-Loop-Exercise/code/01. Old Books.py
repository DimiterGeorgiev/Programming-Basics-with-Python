book_name = input()

current_book = input()

count = 0

is_book_found = False

while current_book != 'No More Books':
    if current_book == book_name:
        is_book_found = True
        print(f'You checked {count} books and found it.')
        break
    count += 1
    current_book = input()

if not is_book_found:
    print(f'The book you search is not here!')
    print(f'You checked {count} books.')
