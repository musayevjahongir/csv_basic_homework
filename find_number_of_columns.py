def find_number_of_columns(data):
    from csv import reader
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    f=open(data)
    f=reader(f)
    a=[]
    for i in f:
        a.append(i)
    return len (a)
print(find_number_of_columns("data.csv"))

# Read the csv file