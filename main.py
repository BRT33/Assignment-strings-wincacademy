# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line


scorer_1 = 'Ruud Gullit'
scorer_2 = 'Marco van Basten'


goal_0 = 32
goal_1 = 54


scorers = scorer_1 + " " + str(goal_0) + ", " + scorer_2 + " " + str(goal_1)


report =  f'{(scorer_1)} scored in the {(goal_0)}nd minute\n{scorer_2} scored in the {goal_1}th minute'


player = scorer_1

start_first_name = player.find('R')
end_first_name = player.find('d')
first_name = player[start_first_name:end_first_name+1]
first_name_len = len(first_name)


start_last_name = player.find('G')
end_last_name = player.find('t')
last_name = player[ start_last_name:end_last_name+1]
last_name_len = len(last_name)

initial = player[0]

name_short = initial+'.'+' '+last_name


chant = f'{first_name}! ' * (first_name_len - 1) + f'{first_name}!'     #did i cheat?, what was the intended solution?
chant_len = len(chant)






print(chant)
print(chant_len)
good_chant = chant[22] != ' '
print(good_chant)
