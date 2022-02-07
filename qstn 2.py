f= open('sample.txt','r+')

condition = True


print("Line which starting with capital letter and have more than five words are:")

while condition:
    line = f.readline()
    words = line.split(" ")
    if(len(words)>5):
        x = words[0]
        if(x[0].isupper()):
            print(line)
    
