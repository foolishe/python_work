from random import randint
import pygal

class Die():
    def __init__(self,num_sides=6):
        self.num_sides=num_sides

    def roll(self):
        return randint(1,self.num_sides)
def throw():
    die=Die()
    results=[]
    for roll_numb in range(1000):
        result=die.roll()
        results.append(result)
    frequencies=[]
    for value in range(1,die.num_sides+1):
        frequency=results.count(value)
        frequencies.append(frequency)
    return results

    hist=pygal.Bar()
    hist.title='Results of rolling one D6 1000 times.'
    hist.x_labels=range(1,7)
    hist.x_title='result'
    hist.y_title='frequency'
    hist.add('D6',frequencies)
    hist.render_to_file('die_visual.svg')
def throw_two_times():
    frequencies=[]
    result1=throw()
    result2=throw()
    result=[]
    for i in range(len(result1)):
        result.append(result1[i]+result2[i])
    for i in range(2,13):
        frequency=result.count(i)
        frequencies.append(frequency)
    hist=pygal.Bar()
    hist.title='Results of rolling one D6 1000 times.'
    hist.x_labels=range(2,13)
    hist.x_title='result'
    hist.y_title='frequency'
    hist.add('D6+D6',frequencies)
    hist.render_to_file('die_visual+.svg')

if __name__ == '__main__':
    throw_two_times()
