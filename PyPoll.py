
# The Data we need to retrieve
#1.The total numnber of votes cast
#2.A complete list of candidates who recieved votes
#3.The percentage of votes each candidate won
#4.The total number of votes each candidate won
#5.The winner of the election based on popular vote

#add our dependencies
import csv
import os
#Assign a variable for the file to load and the path

file_to_load = os.path.join("Election_Analysis","Resources","election_results.csv")

# print(os.listdir())

# open(file_to_load)


#create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis","election_analysis.txt" )
#open the election results and read the file.
with open(file_to_load) as election_data:
# Read the file object with the reader function
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

# #print each row in the csv file
    #for row in file_reader:
        #print(row)
    
    
# #Close the file
    election_data.close()
