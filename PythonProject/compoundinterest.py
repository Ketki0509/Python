'''
Amount = P(1+(R/100)) ** T
CI = Amount - P
'''

P = float(input("Enter the principal amount :"))
R = float(input("Enter the rate of interest :"))
T = float(input("Enter the time of tenure :"))
Amount = P * pow(1 + (R/100), T)
CI = Amount - P
print("CI is :",round(CI,2))