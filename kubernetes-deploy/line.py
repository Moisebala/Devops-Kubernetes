
#filepath = 'test.yml'
#with open(filepath) as fp:
#   line = fp.readline()
#   cnt = 1
#   while line:
#       print("Line {}: {}".format(cnt, line.strip()))
#       line = fp.readline()
#       cnt += 1

def check_if_string_in_file(file_name, string_to_search):
    """ Check if any line in the file contains given string """
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if string_to_search in line:
                return True
    return False
def search_string_in_file(file_name, string_to_search):
    """Search for the given string in file and return lines containing that string,
    along with line numbers"""
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if string_to_search in line:
                # If yes, then add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))
    # Return list of tuples containing line numbers and lines where string is found
    return list_of_results

def main():
    print('*** Check if a string exists in a file *** ')
    # Check if string 'is' is found in file 'sample.txt'
    if check_if_string_in_file('test.yml', 'slurp:'):
        print('Yes, string found in file')
    else:
        print('String not found in file')
    print('*** Search for a string in file & get all lines containing the string along with line numbers ****')
    matched_lines = search_string_in_file('test.yml', 'slurp:')
    print('Total Matched lines : ', len(matched_lines))
    for elem in matched_lines:
        print('Line Number = ', elem[0], ' :: Line = ', elem[1])
    print('*** Search for multiple strings in a file and get lines containing string along with line numbers ***')
if __name__ == '__main__':
    main()

