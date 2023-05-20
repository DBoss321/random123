import numpy as np

def nearest_neighbor(cities, start_city):

    n = len(cities)
    unvisited = set(range(n))
    unvisited.remove(start_city)
    current_city = start_city
    path = [current_city]
    cost = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(cities[current_city], cities[city]))
        unvisited.remove(next_city)
        path.append(next_city)
        cost += distance(cities[current_city], cities[next_city])
        current_city = next_city
    
    cost += distance(cities[path[-1]], cities[start_city])
    path.append(start_city)
    
    return path, cost
    
def distance(city1, city2):

    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

cities = [(0, 0), (1, 7), (6, 2), (3, 5), (3, 4)]
start_city = 0
path, cost = nearest_neighbor(cities, start_city)
print("Shortest path:", path)
print("Cost:", cost)

#OUTPUT
#[Running] python -u "c:\Users\Admin\OneDrive\Desktop\Coding\tsp.py"
#Shortest path: [0, 4, 3, 1, 2, 0]
#Cost: 22.224050256948424

#[Done] exited with code=0 in 0.319 seconds