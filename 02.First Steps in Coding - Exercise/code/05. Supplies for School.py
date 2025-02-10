countPacking = int(input())
countMarkers = int(input())
preparatLiter = int(input())
discount = int(input())
price = countPacking * 5.8 + countMarkers * 7.2 + preparatLiter * 1.2
finalPrice = price - price*discount/100
print(finalPrice)


