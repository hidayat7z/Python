# RENAMING A FILE/FOLDER

# syntax:
# os.rename("path_of_file_with_oldname","path_of_file_with_newname")

os.rename("/home/hidayat7z/first.txt","/home/hidayat7z/phaast.txt")

# RENAMING MULTIPLE FILES

##for 2nd Sem_res.jpeg and 3rd Sem_res.jpeg RENAME it to 2nd Semester Result.jpeg & 3rd Semester Result.jpeg
## we need to make
	# Sem_res.jpeg   ->   Semester Result.jpeg
##that means we need to make
	# /home/hidayat7z/2nd Sem_res.jpeg   ->   /home/hidayat7z/2nd Semester Result.jpeg

#creating a list of the files
re_files=["/home/hidayat7z/2nd Sem_res.jpeg","/home/hidayat7z/3rd Sem_res.jpeg"]

for i in re_files:
	j=i.split(" ")#splitting across a space
	new_path=j[0]+' Semester Result.jpeg' # concatenating to get the new path
	
	os.rename(i,new_path)
