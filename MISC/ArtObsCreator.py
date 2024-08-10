###     Artificial map creator      ###
###     Henok Gashaw, Bahir Dar, Ethiopia
###     2023 GC

import random
file = open("HongKong.xml", "w") #Change the name to the desired one.

file.write("<environment>\n")
file.write('<material id="1" resistivity="100" relativePermittivity="4.5" relativePermeability="1" /> <!-- concrete-->\n')

for i in range(-2500, 2500, 50):
    if i == 0 or i in [100, 150, 200, 250, 300, 350, 400, 450] or i in range(200, 8000, 200) or i in range(-8000, -400, 200):
        continue
    for j in range(-2500, 2500, 50):
        if j == 0 or j in [100, 150, 200, 250, 300, 350, 400, 450] or j in range(200, 8000, 200) or j in range(-8000, -400, 200):
          continue
        x = f'<object position="min {i} {j} 0" orientation=" 0 0 0" shape="cuboid {random.randint(10, 15)} {random.randint(25, 30)} {random.randint(50, 250)} " material="1" fill-color="42 111 199" />\n'
        file.write(x)

file.write('</environment>')

file.close()    