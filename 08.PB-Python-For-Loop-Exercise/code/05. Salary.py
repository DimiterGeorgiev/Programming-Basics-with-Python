n = int(input())
salary = int(input())


for i in range(1, n + 1):
    site = input()
    fine = 0
    if site == 'Facebook':
        fine = 150
    elif site == 'Instagram':
        fine = 100
    elif site == 'Reddit':
        fine = 50
    salary -= fine
    if salary <= 0:
        print(f'You have lost your salary.')
        break

if salary > 0:
    print(salary)
