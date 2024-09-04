def write_file(file_name = "test_file", file_content="This is a test content."):
    with open(file_name, mode = 'w', encoding='utf-8') as test_file:
        test_file.write(file_content)

def append_file(file_name = "test_file", append_content="\nAppended content."):
    with open(file_name, mode = 'a', encoding='utf-8') as test_file:
        test_file.write(append_content)

def read_file(file_name = "test_file"):
    with open(file_name, encoding='utf-8') as test_file:
        return test_file.read()

write_file("files/test_file.txt")
append_file("files/test_file.txt")
content = read_file("files/test_file.txt")
print(content)