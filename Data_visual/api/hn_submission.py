import requests,pygal
from pygal.style import LightenStyle as LS, LightColorizedStyle as LCS
from operator import itemgetter

url='https://hacker-news.firebaseio.com/v0/topstories.json'
r=requests.get(url)
print('Status_code:',r.status_code,'\n',)
submission_ids=r.json()
submission_dicts=[]
for submission_id in submission_ids[:30]:
    url=f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    try:
        submission_r=requests.get(url)
    except:
        print(f'missing date id:{submission_id}')
        continue
    response_dict=submission_r.json()
    submission_dict={
        'label':str(response_dict['title']),
        'xlink':f'https://news.ycombinator.com/item?id={submission_id}',
        'value':response_dict.get('descendants',0),
        }
    submission_dicts.append(submission_dict)

submission_dicts=sorted(submission_dicts,key=itemgetter('value'),reverse=True)

my_config=pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend=False
my_config.title_font_size=24
my_config.label_font_size=14
my_config.major_label_font_size=19
my_config.truncate_label=10
my_config.show_y_guides=False
my_config.width=1000

style=LS('#449988',base_style=LCS)
chart=pygal.Bar(my_config,style=style)
chart.title='submission'
chart.add('commets',submission_dicts)
chart.render_to_file('python_submission.svg')
