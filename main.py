import pandas as pd
import numpy as np
import lda

fields = ["Issue_ID", "Title/Description", "Importance/Type", "Creation_Date", "Resolve_Date"]
#df = pd.read_csv(raw_input("Enter the name of the dataset to import: "), low_memory=False, usecols=fields)

def get_year_count(year):
    return len(df[df["Creation_Date"] == str(year)])

def get_type_count(imp_type):
    return len(df[df["Importance/Type"] == imp_type])

def main():
    global df

    # Eliminate records with non-existent IDs
    df[df["Issue_ID"].apply(lambda x: str(x).isdigit())]

    # Remove rows with "null" entries
    df = df[df != "null"]

    # Format date to just contain the year
    df["Creation_Date"] = df["Creation_Date"].apply(lambda x: (str(x).split(' ')[0].split('/')[2] if isinstance(x, basestring) else ''))

    print "The imported dataset has " + str(len(df)) + " records."
    print "Normal: " + str(get_type_count("normal"))
    print "Enhancement: " + str(get_type_count("enhancement"))
    print "Critical: " + str(get_type_count("critical"))
    print "Minor: " + str(get_type_count("minor"))
    print "Major: " + str(get_type_count("major"))

    temp = int(raw_input("Enter a year: "))

    print str(temp) + " records: " + str(get_year_count(temp))
        
main()

