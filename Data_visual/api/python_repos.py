import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print('status code:',r.status_code)
response_dict=r.json()
print(response_dict.keys())
print('Total repositories:',response_dict['total_count'])
repo_dicts=response_dict['items']
names,stars=[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

style=LS('#aa7799',base_style=LCS)
chart=pygal.Bar(style=style, x_label_rotation=45,show_legend=False)
chart.title='Most-star Python projects on Github'
chart.x_labels=names
chart.add('',stars)
chart.render_to_file('python_repos.svg')
#print('Repositories returned:',len(repo_dicts))

# repo_dict=repo_dicts[0]
#print('\nKeys:',len(repo_dict))
#for key in sorted(repo_dict.keys()):
    #print(key)
#
# print('Selected information about first repository:')
# for repo_dict in repo_dicts:
#     # print('\n\nName:',repo_dict['name'])
#     # print('Owner:',repo_dict['owner']['login'])
    # print('Stars:',repo_dict['stargazers_count'])
    # print('Repostiory:',repo_dict['html_url'])
    # print('Create:',repo_dict['created_at'])
    # print('Updated:',repo_dict['updated_at'])
    # print('Description',repo_dict['description'])
