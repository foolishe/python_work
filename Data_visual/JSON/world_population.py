import json
import pygal
from pygal.maps.world import COUNTRIES
from pygal.style import RotateStyle,LightColorizedStyle

def get_country_code(country_name):
    for code,name in COUNTRIES.items():
        if country_name==name:
            return code
    return None



filename='population_data.json'
with open(filename) as f :
    pop_data=json.load(f)
cc_populations={}
for pop_dict in pop_data:
    if pop_dict['Year']=='2010':
        country_name=pop_dict['Country Name']
        population=int(float(pop_dict['Value']))
        code=get_country_code(country_name)
        if code:
            cc_populations[code]=population
            cc_pops1,cc_pops2,cc_pops3={},{},{}
        else:print('error'+country_name)
for cc,pop in cc_populations.items():
    if pop<10000000:
        cc_pops1[cc]=pop
    elif pop<100000000:
        cc_pops2[cc]=pop
    else:
        cc_pops3[cc]=pop

wm_style=RotateStyle('#dd3388',style=LightColorizedStyle)
wm=pygal.maps.world.World(style=wm_style)
wm.title='populations of Countries in 2010,by countries'
wm.add('10**8<',cc_pops3)
wm.add('10**7-10**8',cc_pops2)
wm.add('0-10**7',cc_pops1)
wm.render_to_file('world populations.svg')
