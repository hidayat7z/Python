#OPENING A FILE

fileObject = open("trytwo.txt","w")

#writing/editing a file

fileObject.write("Hello World! Sup?")


#adding multiple lines

file_list = ["I am Hidayat\nHow are you?","Ok hello bye\nGoodnight"]

fileObject.writelines(file_list)


# APPENDING INFO TO ONE FILE FROM OTHER

#open first file in append mode
fileObject1 = open("first.txt",'a')

#open second file in read mode
fileObject2 = open("second.txt",'r')

#read from second file   ((READING A FILE))
info= fileObject2.read()

#append into first file
fileObject1.write(info)


#CLOSING A FILE

fileObject1.close()
fileObject2.close()


