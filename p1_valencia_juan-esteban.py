
def line_number(filename1,filename2):
    f1 = open(filename1,"r+")
    f2 = open(filename2,"w")

    lines = f1.readlines()
    for index, line in enumerate(lines):
        f2.write(f"{index+1}.{line}")

def parse_functions(filename1):
    f1 = open(filename1, "r")
    lines = f1.readlines()
    functions=[]
    func=[]
    for i, line in enumerate(lines):

        if "#" in line:  #This line checks if there are any comments 
            line=line[0:line.find("#")]+"\n"  #If there are any it slices of whatever is after the # and then re adds the new line operator

        if "def" in line:
            func=[]
            func.append(line[line.find(" ")+1:line.find("(")]) #This grabs the function name by substringing the text in between def and (
            func.append(i+1)
            func.append(line)
            continue

        if "  " in line:
            if line == "    \n" :    #clears comment cleared lines
                pass
            else:
                func[2]+=line
                print(func[2])

            if lines[i+1] == "\n":
                functions.append(tuple(func))
    functions=sorted(functions)
    return tuple(functions)



print(parse_functions("q2test.py"))


