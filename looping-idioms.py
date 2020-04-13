'Learn common patterns for looping in Python'

names = 'raymond rachel matthew'.split()
colors = 'red blue yellow green'.split()
cities = 'austin dallas chicago austin houston austin chicago dallas'.split()

print('Task 1: Show all the names in a different case')



for i in range(len(names)):
    print(names[i].upper())



for name in names:
    print(name.title())


print('\nTask2: SHow all the colors and their ordinal posn')

for i, color in enumerate(colors, start = 1):
    print(f'{i} -> {color}')

    
print('Task3: show all the colors in reverse order')

for color in reversed(colors):
    print(color.title())

    
# C-style - How to do it
# P-Style - What to do

print('\n Tasks 4: Show the name and the corresponding color,\
       ignoring mis-matches')

nn = len(names)
nc = len(colors)

n = nn if nn < nc else nc
for i in range(n):
    print(f'{names[i]} -> {colors[i]}')

for name, color in zip(names, colors):
    print (name, '->', color)

    


    
    

