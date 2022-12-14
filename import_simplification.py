import csv



def bad_tier_choice(column_data):
    """checks if a column is relevant for model"""
    ratio = len(column_data) / len(set(column_data))

    #To close to being a tier 1
    if 1 < ratio < 1.2:
        return True

    #all values in column are same 
    if len(set(column_data)) == 1 or len(set(column_data)) > 20:
        return True
    return False

def read_file_and_organise_hierarchy(filename):
    with open(filename, encoding='utf-8-sig') as file:
        reader = list(csv.reader(file))
        number_of_columns = len(reader[0])
        number_of_rows = len(reader)
        dic = {}
        col_names = reader[0]
        candidates_tier1 = []
        candidates_n_tier = []
        
        for i in range(len(reader[0])):
            dic[i] = []
            
        # Map column number to a list of all corresponding values in CSV
        for i in range(1,number_of_rows):
            for j in range(number_of_columns):
                dic[j].append(reader[i][j])

    
    #sort dictionary by most universal fields first using set theory 
    dic = dict(sorted(dic.items(), key=lambda item: len(set(item[1])),reverse=True))

    for i in dic:
        column_data = dic[i]
        
        if len(column_data) == len(set(column_data)):
            #tier1
            candidates_tier1.append(col_names[i])
            continue

        #checks if tier is a good choice and is not numeric and is not a date
        if bad_tier_choice(column_data) or column_data[0].isnumeric() and int(column_data[0]) not in range(2000,2030):
            continue

        candidates_n_tier.append(col_names[i])

    return candidates_tier1, candidates_n_tier

def main():
    # Files to TEST algorithm 
    # filename = "covid-19 16-April.csv"
    # filename = "covid-19 20-April.csv"
    # filename = "ecan_data-17-sep-19.csv"
    # filename = "transport.csv"
    filename = "Christchurch NZ data.csv"
    # filename= "Gisborne Dc LTPB.csv"

    t1,other_tiers = read_file_and_organise_hierarchy(filename)
    if len(t1) == 0:
        print("No unique columns in csv try with another set of data")
        return None
    Max_number_of_levels = len(other_tiers) + 1
    number_of_levels = int(input(f"Please specify how many levels you would like in your application(Max num layers --> {Max_number_of_levels}) "))
    while number_of_levels < 1 or number_of_levels > Max_number_of_levels:
        print("Your chosen hierarchy is not valid\ntry again")
        number_of_levels = int(input(f"Please specify how many levels you would like in your application(Max num layers --> {Max_number_of_levels}) "))

    
    
    print(f"Available tier 1 subjects --->  {t1}")
    counter = 2
    other_tiers.reverse()
    for i in range(number_of_levels,1,-1):
        print(f"Recomended tier {counter} subject --->  {other_tiers[i-2]}")
        counter += 1
        

main()








