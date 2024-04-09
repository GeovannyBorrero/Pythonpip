import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  
  countrys = input('Type Country => ')


  charts.generate_pie_chart(countries, percentages)


  result = utils.population_by_country(data, countrys)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(countrys,labels, values)


if __name__ == '__main__':
  run()