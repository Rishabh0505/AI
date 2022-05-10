import random
def display(room):
    print(room)
# 3 rooms 
room = [0,0,0]# 0 for dirty 1 for clean
print("Dirty room")
display(room)
x =0
y=0
while x < 3:
    room[x] = random.choice([0,1])
    x+=1
print("Before cleaning detect all of these random dirts in the room")
display(room)
x =0
z=0
while x < 3:
    if room[x] == 0:
        y+=1
        print("Vaccum in this location now,",x+1)
        room[x] = 1
        print("Cleaned!!", x+1)
        z+=1
    x+=1
     
pro= (100-((z/3)*100))
print("Room cleaned")
display(room)
print('Performance=',pro,'%')
print('Moving cost=',y)