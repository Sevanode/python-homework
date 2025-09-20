def line_number(filename1, filename2):
    """
    Copies all lines from filename1 to filename2, numbering each line.
    
    Args:
        filename1 (str): Path to the input file.
        filename2 (str): Path to the output file.
    """
    try:
        with open(filename1, "r") as f1, open(filename2, "w") as f2:
            lines = f1.readlines()
            for index, line in enumerate(lines):
                f2.write(f"{index + 1}.{line}")  # Write line number and content
    except FileNotFoundError:
        print(f"Error: File '{filename1}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def parse_functions(filename1):
    """
    Parses the given Python file and extracts function definitions.
    Removes comments and returns a tuple of functions with their name, line number, and code.
    
    Args:
        filename1 (str): Path to the Python source file.
    
    Returns:
        tuple: Each element is a tuple (function_name, line_number, function_code).
    """
    functions = []
    try:
        with open(filename1, "r") as f1:
            lines = f1.readlines()
            func = []
            for i, line in enumerate(lines):
                # Remove comments from the line
                if "#" in line:
                    line = line[:line.find("#")] + "\n"

                # Detect function definition
                if "def" in line:
                    func = []
                    # Extract function name
                    func.append(line[line.find(" ") + 1:line.find("(")])
                    func.append(i + 1)  # Line number
                    func.append(line)    # Function definition line
                    continue

                # Detect indented lines (function body)
                if "  " in line:
                    if line == "    \n":  # Skip empty indented lines
                        pass
                    else:
                        func[2] += line  # Append to function code
                        # print(func[2])  # Debug print

                    # Check if next line is not indented (end of function)
                    if "   " not in lines[i + 1] :
                        functions.append(tuple(func))
        functions = sorted(functions)
        return tuple(functions)
    except FileNotFoundError:
        print(f"Error: File '{filename1}' not found.")
        return ()
    except Exception as e:
        print(f"An error occurred: {e}")
        return ()

# Example usage
print(parse_functions("q2test.py"))
line_number("test2.py", "test232.txt")
