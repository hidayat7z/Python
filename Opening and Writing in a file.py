#opening a file

fileObject = open("trytwo.txt","w")

#writing/editing a file

fileObject.write("Hello World! Sup?")


#adding multiple lines

file_list = ["I am Hidayat\nHow are you?","Ok hello bye\nGoodnight"]

fileObject.writelines(file_list)
