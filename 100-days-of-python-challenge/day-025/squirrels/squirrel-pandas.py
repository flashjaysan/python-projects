import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])
cinnamon_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])

squirrels_count_per_color_dict = {
    'color': ['Gray', 'Black', 'Cinnamon'],
    'count': [gray_squirrels_count, black_squirrels_count, cinnamon_squirrels_count],
}

squirrels_count_per_color_data_frame = pandas.DataFrame(squirrels_count_per_color_dict)
squirrels_count_per_color_data_frame.to_csv('squirrels_count_per_color.csv')
