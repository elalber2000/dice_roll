from random import randint
import matplotlib.pyplot as plt



#Function that rolls a set of dice
#The input data is a string list with the format:
# [ "1D6" , "2D4" , "5D3" ]
def roll_dice(input):
  res = 0
  temp = 0
  for current_roll_str in input:
    current_roll = current_roll_str.split('D')
    for i in range(int(current_roll[0])):
      res += randint(1,int(current_roll[1]))  #We generate the roll
  return res



  #Variables
input_str = "5D30" #The input, with the format: " 1D6 + 2D4 + 5D3 "
max_it = 10**5  #Number of iterations
yy = [0]
max_xx = 0

#We split the input
input_str = input_str.strip()
input_str = input_str.upper()
input = input_str.split('+')





#We roll the dice n number of times (n = number of iterations)
for i in range(max_it):

  roll = roll_dice(input)

  #We resize the list if necessary
  for temp in range(len(yy),roll):
    yy.append(0)

  #We add the roll result
  yy[roll-1] += 1

  if roll > max_xx:
    max_xx = roll #We find the maximum possible roll

#We change the roll format to probabilities
for i in range(len(yy)):
  yy[i] /= max_it

avg_roll = yy.index(max(yy))+1




#We plot the graph
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
if len(yy)<15 and yy[round(len(yy)/2)]-yy[0] < 0.1:
  plt.ylim([0, 0.51])
#ax.bar(range(1,max_xx+1),yy)
ax.bar(range(1,max_xx+1),yy)
plt.show