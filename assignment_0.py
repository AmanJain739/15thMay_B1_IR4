
###########################################################################################################################################

#PROGRAM 1

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
742, 717, 958,743, 527]

for i in numbers:
    if(i==237):
        break
    elif(i%2==0):
        print(i)

############################################################################################################################################

#PROGRAM 2

color_list_1=set(["White", "Black", "Red"])
color_list_2=set(["Red", "Green"])
print(color_list_1-color_list_2)

############################################################################################################################################

#Program 3

alphabets="abcdefghijklmnopqrstuvwxyz"
flag=0
string=input("Enter a String: ")
for i in alphabets:
    if i not in string.lower():
        flag=-1
    else:
        flag=0
if(flag==0):
    print("Given String is a Pangram")
elif(flag==-1):
    print("Given String is not a Pangram")

############################################################################################################################################

#Program 4

n=int(eval(input("Enter a number: ")))
result=n+((n*10)+n)+((n*100)+(n*10)+n)
print(result)

############################################################################################################################################

#Program 5

n=input("Enter the input: ")
result=n.split('#')
list1=[int(i) for i in list(result[0].split())]
list2=[int(i) for i in list(result[1].split())]
print(list1)
print(list2)

############################################################################################################################################

#Program 6

sequence=input("Enter the sequence: ")
result=sequence.split(",")
print(",".join(sorted(result)))

############################################################################################################################################

#Program 7

d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],'Marks': [57,87,67,79]}
count=0
for i in d['Marks']:
    if(i!=max(d['Marks'])):
         count+=1
    elif(i==max(d['Marks'])):
         count=count
         break
print(d['Student'][count])

##############################################################################################################################################

#Program 8

alphabets="abcdefghijklmnopqrstuvwxyz"
numbers="0123456789"
string=input("Enter the sentence: ")
count=0
count1=0
for i in string:
    if(i in alphabets):
        count+=1
    elif(i in numbers):
        count1+=1
print("LETTERS ",count)
print("DIGITS ",count1)

################################################################################################################################################

#Program 9

d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
n=input("Enter Subject: ")
list1=[]
newdata={}
for i in range(len(d['Subject'])):
    if(d['Subject'][i]!=n):
        continue
    else:
        list1.append(i)
newdata['Name'] = []
newdata['Subject'] = []
newdata['Ratings'] = []
for i in list1:
    newdata['Name'].append(d['Name'][i])
    newdata['Subject'].append(d['Subject'][i])
    newdata['Ratings'].append(d['Ratings'][i])
print(newdata)

##################################################################################################################################################

#Program 10

n = int(input("Enter the range upto: "))
def generator(n):
    for i in range(n):
        if i % 7 == 0:
            yield i
        else:
            continue
print(list(generator(n)))

##################################################################################################################################################

#Program 11

import math
initial_position = [0,0]
while True:
    s = input("Choose direction from: Up,Down,left,Right and Enter Steps: ")
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction.lower()=="up":
        initial_position[0]+=steps
    elif direction.lower()=="down":
        initial_position[0]-=steps
    elif direction.lower()=="left":
        initial_position[1]-=steps
    elif direction.lower()=="right":
        initial_position[1]+=steps
    ask=input("Do you want to continue: ")
    if(ask.lower()=='yes'):
        continue
    else:
        c=int(round(math.sqrt(initial_position[1]**2+initial_position[0]**2)))
        print("Distance from initial position is: ",c)
        break

#####################################################################################################################################################


