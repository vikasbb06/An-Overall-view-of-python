import csv
def read_csv_file(filename):
    with open(filename,"r",newline="") as f:
        load=csv.DictReader(f)
        data=[row for row in load]
        return data
def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return value
def summarize(data,column,operation):
    values=[convert_to_float(row[column]) for row in data if convert_to_float(row[column]) is not None]
    if not values:
        return None
    if operation=="max":
        return max(values)
    elif operation=="min":
        return min(values)
    elif operation=="average":
        return sum(values)/len(values)
    elif operation=="sum":
        return sum(values)
    else:
        raise ValueError("Invalid operation. Supported operations: max, min, average, sum.")  
filename=input("Enter the CSV file name(with extension):")
try:
    data=read_csv_file(filename)
    if not data:
        print("\nThe CSV file is empty.")
    else:
        try:
            print("\nColumns available:", list(data[0].keys())) 
            column=input("Enter the column name to summarize:")
            if column.lower()=="exit":
                print("Exiting the program.")
                exit()
            operation=input("Enter the operation (max, min, average, sum):")
            result=summarize(data,column,operation)
            print(f"\nThis is the {operation} of the {column}:{result}")
        except ValueError as e:
            print(f"\nError:{e}")
except FileNotFoundError:
    print(f"\nError: The file '{filename}' was not found.")