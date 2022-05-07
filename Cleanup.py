# Writing to a file
file1 = open('mylist1.txt', 'w')

# Using readline()
file = open('wordlist.txt', 'r')
count = 0
 
while True:
    count += 1
 
    # Get next line from file
    line = file.readline()
 
    # if line is empty
    # end of file is reached
    if not line:
        break
    else:
        words=line.split()
        #print(words)
        try:
            a=words[1]
        except:
            pass
        file1.write(a)
        file1.write("\n")
    
file.close()
file1.close()
