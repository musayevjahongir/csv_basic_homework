def get_first_row(data):  
    
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   from csv import reader
   f=open(data)
   f=reader(f)
   a=[]
   for i in f:
      a.append(i)
   return a[0]
print(get_first_row("data.csv"))

# Read the csv file