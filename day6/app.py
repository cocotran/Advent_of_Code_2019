from collections import defaultdict

input = open('input.txt', 'r')

planets = defaultdict(list)

# store all unique planet in dictionary as keys
# with the list of children as value
for line in input:
	left, right = line.strip().split(')')
	planets[left].append(right)

# recursive function to count all the children of a planet
def count_orbits(planet):
	if planet not in planets:
		return 0

	children = planets[planet]
	return len(children) + sum([count_orbits(child) for child in children])

# sum of all the children of all planets 
print('Part 1: ', sum([count_orbits(planet) for planet in planets.keys()]))
