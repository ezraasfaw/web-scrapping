import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_excel(r'C:/Users/EEEFL_DESKTOP/PycharmProjects/webScrapping/Day1/GasPrices-montreal.xlsx')
df2 = pd.read_excel(r'C:/Users/EEEFL_DESKTOP/PycharmProjects/webScrapping/Day2/GasPrices-montreal.xlsx')
df3 = pd.read_excel(r'C:/Users/EEEFL_DESKTOP/PycharmProjects/webScrapping/Day3/GasPrices-montreal.xlsx')
df4 = pd.read_excel(r'C:/Users/EEEFL_DESKTOP/PycharmProjects/webScrapping/Day4/GasPrices-montreal.xlsx')

gasPriceDay1 = df1['Price'].tolist()
gasPriceDay2 = df2['Price'].tolist()
gasPriceDay3 = df3['Price'].tolist()
gasPriceDay4 = df4['Price'].tolist()

avgPriceDay1 = np.mean(gasPriceDay1)
avgPriceDay2 = np.mean(gasPriceDay2)
avgPriceDay3 = np.mean(gasPriceDay3)
avgPriceDay4 = np.mean(gasPriceDay4)

x_data = [1, 2, 3, 4]
y_data = [avgPriceDay1, avgPriceDay2, avgPriceDay3, avgPriceDay4]
print(y_data)

#Find optimal coefficients for the polynomial using NumPy.
polyOrder = 3
a = np.polyfit(x_data, y_data, polyOrder)
y_model = np.poly1d(a)
MSE = np.sum((y_data - y_model(x_data))**2)
x_interp = np.linspace(1, 4, 200)

#Plot the output.
plt.plot(x_data, y_data, 'g.')
plt.plot(x_interp, y_model(x_interp), 'r--')
plt.xlabel('Days')
plt.ylabel('Prices')
plt.title('Montreal Gas Prices between 23rd to 26th of December\n  MSE = %4.2f' %MSE)
plt.show()

print(y_model(4))
