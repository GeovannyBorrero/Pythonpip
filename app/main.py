import utils
import read_csv
import charts
import pandas as pd

def run():
  df = pd.read_csv('data.csv') # = data = read_csv.read_csv('data.csv')
  df = df[df['Continent'] == 'South America']# =  data = list(filter(lambda item : item['Continent'] == 'South America',data))
  data = read_csv.read_csv('data.csv')

  countries = df['Country'].values # = countries = list(map(lambda x: x['Country'], data))
  percentages = df['World Population Percentage'].values# = percentages = list(map(lambda x: x['World Population Percentage'], data))

  countrys = input('Type Country => ')


  charts.generate_pie_chart(countries, percentages)


  result = utils.population_by_country(data, countrys)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(countrys,labels, values)


if __name__ == '__main__':
  run()