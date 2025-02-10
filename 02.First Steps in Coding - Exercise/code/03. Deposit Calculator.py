depSum = float(input())
termOfDeposit = int(input())
annualInterestRate = float(input())
finaleSum = depSum + termOfDeposit*depSum*annualInterestRate/100/12
print(finaleSum)

