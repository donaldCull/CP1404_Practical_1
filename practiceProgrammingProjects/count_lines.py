__author__ = 'Donald Cull'
def main():
    print(count_lines_in_file("names.txt"))
    print(count_nonblank_lines_in_file("names.txt"))


def count_lines_in_file(filename):
    file_object = open(filename, 'r')
    lines = file_object.readlines()
    file_object.close()
    number_of_lines = len(lines)
    return number_of_lines

def count_nonblank_lines_in_file(filename):
    file_object = open(filename , 'r')
    lines = file_object.readlines()
    file_object.close()
    number_of_lines = len(lines)
    return number_of_lines

main()