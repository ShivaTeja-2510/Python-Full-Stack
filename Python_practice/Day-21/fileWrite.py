#Step-1 Open the file
path = r"C:\Users\arvas\Downloads\filesIntro.txt"
f=open(path,'w')

#Step-2 Write the data to the file
f.write("Hi This is Shiva Teja\n")
f.write("I am from Hyderabad")

#Step-3 Close the File
f.close()
print("Written Completed")
