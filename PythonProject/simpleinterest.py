'''SI = (p *R * T)/100'''
P = float(input("Enter principal amount: "))
R = float(input("Enter rate of interest :"))
T = float(input("Enter time of tenure :"))
result = (P * R * T )/100
print("SI is :",round(result,2))