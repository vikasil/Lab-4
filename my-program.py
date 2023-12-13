things = [   ['r',3, 25, 0],
        ['p',2, 15, 0],
        ['a',2, 15, 0],
        ['m',2, 20, 0],
        ['i',1, 5, 0],
        ['k',1, 15, 0],
        ['x',3, 20, 0],
        ['t',1, 25, 0],
        ['f',1, 15, 0],
        ['s',2, 20, 0],
        ['c',2, 20, 0]
]
my_place=9 # место в рюкзаке
for i in things:
    i[3]=i[2]/i[1]
things.sort(key=lambda x: x[3])
things.reverse()
place=1
cost=25 # очки выживания
problem=0
bag =''
for i in things:
    if place<my_place:
        place+=i[1]
        cost+=i[2]
        last_place=i[1] 
        last_cost=i[2] 
        bag = bag+i[0]*int(i[1])
        thing =i[0]*int(i[1])
    else:
        if place==my_place:
            cost-=i[2]
        else:
            problem=1
            if i[1]==place-my_place:
                place+=i[1]
                cost+=i[2]
                bag = bag+i[0]*int(i[1])
            else:
                cost-=i[2]
if problem==1:
    place-=last_place
    cost-=last_cost
    bag='d'+bag.replace(thing, '')
for i in range(0,9,3):
    print(bag[i],bag[i+1],bag[i+2])
print('итоговые очки выживания:',cost)
