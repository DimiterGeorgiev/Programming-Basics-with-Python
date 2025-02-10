naylon_M2 = int(input())
paint_l = int(input())
looser_l = int(input())
hours = int(input())
price = (naylon_M2 + 2) * 1.5 + paint_l * 1.1 * 14.5 + looser_l * 5 + 0.4
workPrice = price * 0.3 * hours
fullPrice = price + workPrice
print(fullPrice)
