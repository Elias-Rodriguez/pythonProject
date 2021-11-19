# Information gathered from:
# https://www.rssweather.com/climate/Oklahoma/Oklahoma%20City/
import matplotlib.pyplot as plt

high_temps = [47.1,53.5,62.5,71.2,78.9,87.2,93.1,92.5,84.1,73.4,59.6,49.8]
low_temps = [26.2,31.1,39.4,48.1,	57.9,66.4,	70.8,69.8,62.2,50.6,38.2,29.2]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov',
          'Dec']
plt.scatter(months,high_temps, color ="red", marker = '+')
plt.scatter(months,low_temps, color ="blue", marker = '^')

plt.xlabel('Months')
plt.ylabel('Temperature in Degrees Fahrenheit')
plt.title('Oklahoma Highs and Lows')
plt.legend(['Highs', 'Lows'])


plt.show()
