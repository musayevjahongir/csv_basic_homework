def find_number_of_rows(data):
    from csv import reader
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    f=open(data)
    f=reader(f)
    a=[]
    for i in f:
        a.append(i)
    return len (a)
print(find_number_of_rows("data.csv"))

# Read the csv file
