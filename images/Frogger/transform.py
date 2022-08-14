
my_file = open('forward_frog_3.txt','r')
right = open('right_frog_3.txt','w')
left = open('left_frog_3.txt','w')
back = open('back_frog_3.txt','w')


og_frog = []


#Read pixel map from file,create nested list og_frog
with my_file as fp:
    #Iterate through each line
    for line in fp:
        og_frog_element = ""
        og_frog_row = []
        for elem in line:
            if(elem != "," and (elem.isspace() == 0) and elem != "\n"):
                og_frog_element += elem
            if elem == "\n":
                og_frog_row.append(str(og_frog_element))
                og_frog.extend([og_frog_row])
                break
            if elem == ",":
                og_frog_row.append(str(og_frog_element))
                og_frog_element = ""


#Transform right frog
right_frog = []

for row in range(1,17):
    new_row = []
    for col in range(1,17):
        new_row.append(og_frog[16-col][16-row])
    right_frog.extend([new_row])

    
#Write right frog
for lis in right_frog:
    j = "\n.hword "
    temp = ""
    for i in lis:
        j += i + ", "
    print(j)
    print("\n")
    right.write(j)



#Transform left frog
left_frog = []

for row in range(1,17):
    new_row = []
    for col in range(1,17):
        new_row.append(og_frog[col-1][row-1])
    left_frog.extend([new_row])
#Write left frog
for lis in left_frog:
    j = "\n.hword "
    temp = ""
    for i in lis:
        j += i + ", "
    left.write(j)




#Transform down frog
down_frog = []
for row in range(1,17):
    down_frog.append(og_frog[16-row-1])
#Write Down Frog
for lis in down_frog:
    j = "\n.hword "
    temp = ""
    for i in lis:
        j += i + ", "
    back.write(j)
        



#TEST: Write transformed frog into into file
front = open('check_write', 'w')
count = 0
for lis in og_frog:
    j = "\n.hword "
    temp = ""
    for i in lis:
        j += i +", "
    front.write(j)
front.close()
        

    

    
my_file.close();
right.close();
left.close();
back.close();
