import csv


def read_file_and_organise_hierarchy(filename):
    with open(filename) as file:
        reader = list(csv.reader(file))
        number_of_columns = len(reader[0])
        number_of_rows = len(reader[0])
        dic = {}
        col_names = reader[0]
        candidates_tier1 = []
        candidates_tier_2_and_3 = []
        
        for i in range(len(reader[0])):
            dic[i] = []
    
        #Map column number to a list of all corresponding values in CSV
        for i in range(1,number_of_rows):
            for j in range(number_of_columns):
                dic[j].append(reader[i][j])

    
    #sort dictionary by most universal fields first
    dic2 = dict(sorted(dic.items(), key=lambda item: len(set(item[1]))))
    for i in dic2:
        #check to see if col is numeric 
        if dic[i][0].isnumeric() == False:
            candidates_tier_2_and_3.append(col_names[i])
            #checks to see if all values in a col are unique
            if len(dic[i]) == len(set(dic[i])):
                candidates_tier1.append(col_names[i])
    return candidates_tier1,candidates_tier_2_and_3


def main():
    filename = "ecan_data-17-sep-19 (2).csv"

    T1,T2_3 = read_file_and_organise_hierarchy(filename)
    print(f"Recomended tier 3 subject --->  {T2_3[0]}")
    print(f"Recomended tier 2 subject --->  {T2_3[1]}")
    print(f"Available tier 1 subjects --->  {T1}")
    


main()








