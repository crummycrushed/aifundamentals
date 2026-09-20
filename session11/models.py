import csv


with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "Grade"])
    writer.writerow(["Alice", 14, "8th"])
    writer.writerow(["Bob", 15, "9th"])
    writer.writerow(["Shubhendu", 13, "7th"])


# with : a safety wrapper  - gurantees the files get properly closed when u are done
# open("students.csv", "w", newline="") --> function actuall opens the file : first argument
# is the fule name , second = write mode
# students.csv : checks if u have a file or not , if not it creates one
# as f : short nickname
# csv.writer(f) : Wraps the open file with the tool csv which knows how to write 
# data into the csv mode

# write.writerow() : Wrties one single row --- the list values value become one comma-seperate line


with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for i in reader:
        print(i)