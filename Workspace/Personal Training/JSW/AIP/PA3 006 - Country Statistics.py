import os
import csv
class Country:
    def __init__(self, name:str, gdp:float, life_expectancy:float, population_density:int, population:int):
        self.name:str = name
        self.gdp:float = self.parse_float(gdp)
        self.life_expectancy:float = self.parse_float(life_expectancy)
        self.population_density:int = self.parse_int(population_density)
        self.population:int = self.parse_int(population)
    def __str__(self):
        return f"{self.name}, {self.gdp}, {self.life_expectancy}, {self.population_density}, {self.population}"
    def parse_int(self, n):
        try:
            return int(n.replace('$', '').replace(' ', '').replace(',', ''))
        except:
            return None
    def parse_float(self, n):
        try:
            return float(n.replace('$', '').replace(' ', '').replace(',', ''))
        except:
            return None
        

class CountryStatistics:
    def __init__(self, path_csv:str):
        self.path_csv = path_csv
        self.keys = dict()
        self.list_country = []
        try:
            with open(self.path_csv, newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for index_line, items in enumerate(reader):
                    if index_line == 0:
                        self.keys = {k:i for i, k in enumerate(items)}
                        continue
                    country = Country(
                        items[self.keys['Country']],
                        items[self.keys['GDP']],
                        items[self.keys['Life expectancy']],
                        items[self.keys['Density (P/Km2)']],
                        items[self.keys['Population']]
                    )
                    self.list_country.append(country)
        except:
            raise Exception("비상상황")
    def top_5_gdp(self):
        return [(country.name, f"{country.gdp:,.0f}") for country in sorted(
            filter(lambda x: x.gdp != None, self.list_country), 
            key = lambda x: x.gdp,
            reverse = True
            )[:5]
        ] 
    def top_5_life_expectancy(self):
        return [(country.name, country.life_expectancy) for country in sorted(
            filter(lambda x: x.life_expectancy != None, self.list_country),
            key = lambda x: x.life_expectancy,
            reverse = True
            )][:5]
    def countries_by_density(self):
        return [(country.name, int(country.population_density)) for country in sorted(
            self.list_country,
            key = lambda x: x.population_density,
            reverse = True
            )][:5]
    def average_population(self):
        target_arr = list(map(lambda x: x.population, filter(lambda x: x.population != None, self.list_country)))
        result = sum(target_arr)//len(self.list_country)
        return f"{result:,}"