
def line_number(filename1,filename2):
    f1 = open(filename1,"r+")
    f2 = open(filename2,"w")

    lines = f1.readlines()
    for index, line in enumerate(lines):
        f2.write(f"{index+1}.{line}")


line_number("test.py","test.txt")