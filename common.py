def read_file_to_list(filename):
    if (filename == None):
        raise TypeError("filename not given")
    
    print(f"Reading file {filename}")
    content = []
    try:
        with open(filename, "r") as f:
            for line in f:
                content.append(line.strip())
    except FileNotFoundError:
        raise FileNotFoundError("File not found")

    if (len(content) <= 1):
        raise AssertionError("Reading file fail: Data List too short")
    return content
