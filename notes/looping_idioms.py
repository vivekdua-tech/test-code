'Learn common patterns for looping in Python'

from operator import itemgetter

names = 'raymond rachel matthew'.split()
colors = 'red blue yellow green'.split()
cities = 'austin dallas chicago austin houston austin chicago dallas'.split()

print('Task 1: Show all the names in a different case')

for i in range(len(names)):
    print(names[i].upper())

for name in names:
    print(name.title())

print('\nTask 2: Show all the colors and their ordinal position')

for i in range(len(colors)):
    print('%d -> %s' % (i+1, colors[i]))

for i, color in enumerate(colors, start=1):
    print('%d -> %s' % (i, color))

print('\nTask 3: Show all the colors in reverse order')

for i in range(len(colors) - 1, -1, -1):
    print(colors[i].upper())

for color in reversed(colors):
    print(color.title())

print('\nTask 4: Show the name and corresponding color, ignoring mismatches')

nn = len(names)
nc = len(colors)
n = nn if nn < nc else nc
for i in range(n):
    print('%s -> %s' % (names[i], colors[i]))

n = min(len(names), len(colors))
for i in range(n):
    print('%s -> %s' % (names[i], colors[i]))

for name, color in zip(names, colors):
    print('%s -> %s' % (name, color))    

print('\nTask 5: Show all the colors in alphabetical order')

for color in sorted(colors):
    print(color)

print('\nTask 6: Show all the colors by the length of the name')
# SELECT color FROM Colors ORDER BY LENGTH(color);

for color in sorted(colors, key=len):
    print(color)

print('\nTask 7: Sort the colors by the second letter of the color')
def second_letter(word):
    return word[1]

for color in sorted(colors, key=second_letter):
    print(color)

# SELECT color FROM Colors ORDER BY SUBSTRING(color, 2, 1);
for color in sorted(colors, key=lambda word: word[1]):
    print(color)

for color in sorted(colors, key=itemgetter(1)):
    print(color)

print('\nTask 8:  Show all of the cities, just once, in alpha order')
# SELECT DISTINCT city FROM cities ORDER BY city;

for city in sorted(set(cities)):
    print(city)

print('\nTask 9: Show the names in reverse alphabetical order')

for name in sorted(names, reverse=True):
    print(name)



    
'''

/* Goal: Call strlen() once per datum
         rather than twice per comparison
*/         

int
decocmp(struct entry *p, struct *q) {
    int pl = p->n;
    int ql = q->n;
    if (pl < ql) return -1;
    if (ql < pl) return 1;
    return 0;    
}

struct entry {
    int n;
    char *s;
} *decorated;

decorated = malloc(sizeof(entry) * n);
for (i=0 ; i<n ; i++) {
    decorated->n = strlen(colors[i]);
    s = color[i];
}

qsort(decorated, decocmp);

for (i=0 ; i<n ; i++) {
    colors[i] = decorated[i]->s;
}

free(decorated);

/***********************************************/

int
lencmp(char *p, char *q)
{
    int pl = strlen(p);
    int ql = strlen(q);
    if (pl < ql) return -1;
    if (ql < pl) return 1;
    return 0;
}

qsort(colors, lencmp);


for (i=0 ; i<n ; i++) {
    printf("%s\n", upper(names[i]));
}

for (i=0 ; i<n ; i++) {
    printf("%d -> %s\n", i+1, colors[i]);
}

for (i=n-1 ; i > -1 ; i--) {
    printf("%s\n", upper(colors[i]));
}

n = (nn < nc) ? nn : nc;
for (i=0 ; i<n ; i++) {
    printf("%s -> %s", names[i], colors[i]);
}

'''

















































