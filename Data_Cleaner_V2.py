import os
import csv

#Author : Abdulmalik Hawsawi
# find the file paths so it works on any machine using os ( operating system)
file_path = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(file_path , 'dirty_data.csv')
output_file = os.path.join(file_path , 'clean_data.csv')

# defing the functions
#Read the whole file and store the data
def load_data(input_file):
  all_data = []
  #open the file
  with open( input_file , "r" , encoding='utf8') as file_data:
    data = csv.reader(file_data)
    next(data)
    # break eack row and turn it into a list
    for row in data:
      id = row[0].strip()
      name = row[1].strip()
      age = row[2].strip()
      email = row[3].strip()
      salary = row[4].strip()
      all_data.append([id, name, age, email, salary])
  
  return all_data

#Check values for each row. if the value for the row is not correct make the value empty
def fix_types(all_data):
  fixed_data_type = []
  for row in all_data:
    #checks id is integer
    try:
      row[0] = int(row[0])
    except ValueError:
      row[0] = None
    # checks name is string
    try:
      row[1] = str(row[1])
    except ValueError:
      row[1] = None
    #checks age is integer
    try:
      row[2] = int(row[2])
    except ValueError:
      row[2] = None
    #checks email is string
    try:
      row[3] = str(row[3])
    except ValueError:
      row[3] = None
    #checks salary is integer
    try:
      row[4] = int(row[4])
    except ValueError:
      row[4] = None
    
    fixed_data_type.append(row)
  return fixed_data_type



# removes any row with missing data or empty fields

def remove_missing(fixed_data_type):
  no_missing_data = []

  for row in fixed_data_type:
    if len(row) < 5 :
      continue
    
    if not row[0] or not row[1] or not row[2] or not row[3] or not row[4]:
      continue
    
    no_missing_data.append(row)

  
  return no_missing_data



# makes all the strings cleaner and lower case for duplicate check 
def normalize_text(no_missing_data):
  fixed_text = []
  for row in no_missing_data:
    row[1] = row[1].strip().lower()
    row[3] = row[3].strip().lower()
    fixed_text.append(row)
  return fixed_text

# checks for any duplicates and removes them
def remove_duplicates(fixed_text):
  no_duplicate = []
  for row in fixed_text:
    if row not in no_duplicate:
      no_duplicate.append(row)
    else:
      continue
  return no_duplicate

# creates a new output file and writes the data inside it.
def save_clean_data(no_duplicate, output_file):
  with open(output_file, 'w' ,newline="", encoding='utf8') as output:
    writer = csv.writer(output)
    writer.writerow(["ID", "Name" , "Age" , "Email" , "Salary"])
    writer.writerows(no_duplicate)


load = load_data(input_file)
type = fix_types(load)
missing = remove_missing(type)
normal = normalize_text(missing)
data = remove_duplicates(normal)

save_clean_data(data , output_file)
