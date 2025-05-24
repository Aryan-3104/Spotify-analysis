import matplotlib.pyplot as plt

# Data
countries = ['India', 'China', 'Japan', 'South Korea', 'Indonesia']
gdp = [2.8, 14.9, 5.1, 1.8, 1.1]

# Bar plot
plt.bar(countries, gdp, color='blue')
plt.xlabel('Country')
plt.ylabel('GDP (in trillion USD)')
plt.title('GDP of Asian Countries')
plt.legend(['GDP'])
plt.xticks(rotation=45)
plt.show()