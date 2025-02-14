import math
import random
import matplotlib.pyplot as plt

### Simulated Annealing
def simulated_annealing(current, distances, T, r, exact):
    # distance of current tour
    current_path = sum(distances[current[i]-1][current[i+1]+1] for i in range(len(current) - 1))

    # other parameters
    error = 1
    steps = 0
    n = len(distances)
    
    while error > 0.01:

        if steps == n**2:
            print(f"Current tour: {current}; Distance: {current_path}")
            print(f"Error: {error*100}%; Temperature: {T}")
            if T>1:
                T = T*r
            else:
                T = 100
            steps = 0

        # find a new neighbour
        i = random.randrange(1, n-2)
        j = random.randrange(i+2, n+1)
        next = current[0:i]+list(reversed(current[i:j]))+current[j:]
        next_path = sum(distances[next[i]-1][next[i+1]+1] for i in range(len(next) - 1))
        
        p = math.exp((current_path-next_path)/T)
        # p = math.exp(-abs(current_path-next_path)/T)
        R = random.uniform(0.0,1.0)
        # if next_path<=current_path or p>=R: # accept if new is worse then current and high ptobability
        if p>=R:
            current = next
            current_path = next_path

        error = 1-exact/current_path

        steps += 1
    
    print(f"The best tour: {current}; Distance: {current_path}")
    print(f"Error: {error*100}%; Temperature: {T}")
    return current


### EXAMPLE

# matrix with points and distances 
d = []

with open("c:/Users/DELL/Desktop/optimization lab 2/data194.txt", "r") as data: # 29 (Sahara) or 194 (Qatar)
    for line in data:
        if int(line[:2])<10: 
            x = line[2:12]
            y = line[13:len(line)-1]
        else: 
            x = line[3:13]
            y = line[14:len(line)-1]
        d.append([float(x), float(y)])
            
for target in d:
    for comparison in d:
        if target == comparison:
            target.append(math.inf)
        else:
            target.append(int(math.sqrt((target[0]-comparison[0])**2 + (target[1]-comparison[1])**2)))

# basic solution
basic = [x+1 for x in range(len(d))]+[1]


# the best solution
solution = simulated_annealing(current=basic, distances=d, T=100, r=0.9, exact=9352) # exact=27603 (Sahara); exact=9352 (Qatar)

# plotting a graph
for i in range(len(d)):
    plt.scatter(d[i][1], d[i][0], color='black', s=8)
line = plt.plot([d[i - 1][1] for i in solution], [d[i - 1][0] for i in solution], color='blue', linestyle='-', linewidth=1, zorder=1)
plt.grid(True)
plt.draw()
plt.show()