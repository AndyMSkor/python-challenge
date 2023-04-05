import os
import csv

input_file = ('python-challenge', 'PyPoll', 'election_data.csv')

total_votes_casted = []
candidates_who_ran = { "CandidateOne" : "Charles Casper Stockham",
                       "CandidateTwo" : "Dianna Deggette",
                       "CandidateThree" : "Raymon Anthony Doane"}

csvpath = "./Resources/election_data.csv"

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader) 


