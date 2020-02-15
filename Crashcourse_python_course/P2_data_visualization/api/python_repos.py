"""This program shows the top rated python repositories in Github"""


import requests as req
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


def show_info(repo):
    """Shows basic info of the introduced repository"""

    print("\nSelected information about first repository:")
    print("\nName:", repo['name'])
    print("Owner:", repo['owner']['login'])
    print("Stars:", repo['stargazers_count'])
    print("Repository:", repo['html_url'])
    print("Created:", repo['created_at'])
    print('Updated:', repo['updated_at'])
    print('Description:', repo['description'])


# Get the api needed for extracting the info
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = req.get(url)
print("Status code:", r.status_code)

# Convert it to a manageable file
response_dict = r.json()

print("Total repositories:", response_dict['total_count'])
repo_dicts = response_dict['items']

names, stars = [], []
for repo in repo_dicts:
    names.append(repo['name'])
    stars.append(repo['stargazers_count'])

# Make visualization
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_OY_guides = False
my_config.width = 1000

chart = pygal.Bar(
    style = my_style,
    config = my_config
    )
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')

print("Repositories returned:", len(repo_dicts))

for repo in range(10):
    show_info(repo_dicts[repo])