# Currency converter from EUR to USD,CAD,JPY,CHF,MXN,CNY,NOK
USD = 1.055
CAD = 1.353
JPY = 137.112
CHF = 1.035
MXN = 21.356
CNY = 6.972
NOK = 9.899

EUR = float(input("Enter the amount you want to convert (EUR) : "))
currency = input("Select the currency (USD,CAD,JPY,CHF,MXN,CNY,NOK): ")
if currency in ['USD', 'usd', 'Usd', 'uSd', 'usD'] :
    result = EUR * USD    
    rounded = round(result,2)
    print(rounded, 'USD (US dollars)')
elif currency in ['CAD', 'cad', 'Cad', 'cAd', 'caD'] :
    result = EUR * CAD
    rounded = round(result,2)
    print(rounded, 'CAD (Canadian dollars)')
elif currency in ['JPY', 'jpy', 'Jpy', 'jPy', 'jpY'] :
    result = EUR * JPY
    rounded = round(result,2)
    print(rounded, 'JPY (Japanese Yens)')
elif currency in ['CHF', 'chf', 'Chf', 'cHf', 'chF'] :
    result = EUR * CHF
    rounded = round(result,2)
    print(rounded, 'CHF (Swiss francs)')
elif currency in ['MXN', 'mxn', 'Mxn', 'mXn', 'mxN'] :
    result = EUR * MXN
    rounded = round(result,2)
    print(rounded, 'MXN (Mexican pesos')
elif currency in ['CNY', 'cny', 'Cny', 'cNy', 'cnY'] :
    result = EUR * CNY
    rounded = round(result,2)
    print(rounded, 'CNY (Chinese yuans)')
elif currency in ['NOK', 'nok', 'Nok', 'nOk', 'noK'] :
    result = EUR * NOK
    rounded = round(result,2)
    print(rounded, 'NOK (Norwegian krones)')
else:
    print("You entered the wrong currency!")