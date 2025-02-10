count = int(input())

people_musala = 0
people_monblan = 0
people_kilimanjaro = 0
people_K2 = 0
people_everst = 0

all_people = 0

for i in range(1, count + 1):
    group = int(input())
    all_people += group
    if group <= 5:
        people_musala += group
    elif 6 <= group <= 12:
        people_monblan += group
    elif 13 <= group <= 25:
        people_kilimanjaro += group
    elif 26 <= group <= 40:
        people_K2 += group
    elif group >= 41:
        people_everst += group

percent_musala = people_musala / all_people * 100
percent_monblan = people_monblan / all_people * 100
percent_kilimangjaro = people_kilimanjaro / all_people * 100
percent_K2 = people_K2 / all_people * 100
percent_everest = people_everst / all_people * 100

print(f'{percent_musala:.2f}%')
print(f'{percent_monblan:.2f}%')
print(f'{percent_kilimangjaro:.2f}%')
print(f'{percent_K2:.2f}%')
print(f'{percent_everest:.2f}%')
