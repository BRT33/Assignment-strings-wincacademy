# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line


scorer_1 = 'Ruud Gullit'
scorer_2 = 'Marco van Basten'


goal_0 = 32
goal_1 = 54


scorers = scorer_1 + " " + str(goal_0) + ", " + scorer_2 + " " + str(goal_1)


report =  f'{(scorer_1)} scored in the {(goal_0)}nd minute\n{scorer_2}\
          scored in the {goal_1}th minute'


player = 'Ruud Gullit'

end_first_name = player.find(' ')
first_name = player[:end_first_name]
first_name_len = len(first_name)

start_last_name = player.find(' ')
last_name = player[start_last_name +1:]
last_name_len = len(last_name)

initial = player[0]

name_short = initial+'.'+' '+last_name


chant = f'{first_name}! ' * (first_name_len - 1) + f'{first_name}!'     
# Het is mij niet gelukt om dit in 1 f-string te krijgen, zou je een hint kunnen geven? 
chant_len = len(chant)


print(chant)
good_chant = chant[-1] != ' '
print(good_chant)