weight = {          #stores each coin weights in kilograms.
    0.05 : 0.002,
    0.10 : 0.00225,
    0.25 : 0.0054, #(aluminium bronze, golden which is predominant)
    0.5  : 0.0058,
    1.0  : 0.00635,
    2.0  : 0.0072,
    }

while (True): # just so it loops. it could be reimplemented for an actual use someday.
    x = float(input("Enter the weight of your coins (Kilograms): "))
    y = float(input("Enter the kind coins you wish to weight (AR$): "))
    result = lambda x,y: x/weight[y] #lambda functions ftw
    print (result(x,y))
