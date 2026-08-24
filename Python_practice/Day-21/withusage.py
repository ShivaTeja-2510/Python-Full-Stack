#Step-1 Open the file
path = r"C:\Users\arvas\Downloads\filesIntro.txt"
with open(path,'r') as f:
    print(f.read())