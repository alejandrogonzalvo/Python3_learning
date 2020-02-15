"""This program returns the IDs of the current top articles on Hacker News"""


import requests as req


from operator import itemgetter


def show_info(submission_dict):
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])


# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = req.get(url)
print("Status code:", r.status_code)


# Process information abour each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # MAke a separate API call for each submission.
    url = ('https://hacker-news.firebaseio.com/v0/item/'
            + str(submission_id) + '.json')
    submission_r = req.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(
    submission_dicts,
    key = itemgetter('comments'),
    reverse = True
    )

for submission_dict in submission_dicts:
    show_info(submission_dict)
