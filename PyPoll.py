# Add out dependencies.
import csv
import os


# Assign a variable for the file to load and the path.

# file_to_load = 'Resources/election_results.csv'

# or use the following code when unsure of exact filename path.
# os.path allows up toe access files on different operating systems,
# like macOS and Windows. The join() function joins ourt file path 
# components together when they are provide as separate strings; then,
# it returns a direct path with the appropriate operating system separator,
# forward slash for macOS backward slash for Windows.

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.

    # Read the file object with the reader function.
    # The variable, file_reader, is referencing the file object,
    # which is stored in memory. To "pull" the data out of the file
    # object, we can iterate through the file_reader variable and
    # print each row, including the headers, or column names.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)
    