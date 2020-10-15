data = np.vstack((country_name, country_code, gdp_2015, gdp_2017)).T
df = pd.DataFrame(data, columns=['Country Name', 'Country Code', 2015, 2017])
df
