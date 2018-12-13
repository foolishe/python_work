#home work
def make_sandwich(name,*toppings):
    print(f'\n{name}\'s sandmaking a sandwich with the following toppings: ')
    for topping in toppings[0]:
        print(topping+' ',end='')
david=['mushrooms','green peppers','extra cheese']
alex=['cafe','dood','help']
make_sandwich('david',david)
make_sandwich('alex',alex)
