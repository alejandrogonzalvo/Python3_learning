import json

filename = '/home/alejandrogonzalvo4eso/Escritorio/python3_learning/Crashcourse_python_course/P2_data_visualization/data_download/population_data.json'
with open(filename) as f:
    data = json.load(f)

for pop_dict in data:
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        population = pop_dict['Value']
        print("\n" + country + ": " + population)
