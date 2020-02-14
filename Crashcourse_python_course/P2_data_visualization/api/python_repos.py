import requests as req


def show_info(repo):
    print("\nSelected information about first repository:")
    print("\nName:", repo['name'])
    print("Owner:", repo['owner']['login'])
    print("Stars:", repo['stargazers_count'])
    print("Repository:", repo['html_url'])
    print("Created:", repo['created_at'])
    print('Updated:', repo['updated_at'])
    print('Description:', repo['description'])




url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = req.get(url)
print("Status code:", r.status_code)

response_dict = r.json()

print("Total repositories:", response_dict['total_count'])
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

for repo in range(10):
    show_info(repo_dicts[repo])