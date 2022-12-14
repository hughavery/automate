import csv
from colorama import Fore, Style


def good_tier_choice(column_data,col_name):
    """checks if a column is relevant for model"""
    ratio = len(column_data) / len(set(column_data))

    #Too close to being a tier 1 or all values in column are same
    #I chose 1.2 as works ok but could increase to 1.3 or 1.4 
    if 1 < ratio < 1.2 or len(set(column_data)) == 1:
        return False

    # allow numbers to be tier choices if used as a unique indicator or is a date within ther range 2000-2030
    if column_data[0].isnumeric() and column_data[0] not in range(2000,2030):
        tier1_indicator = ["unique","id","distinct","identifier"]
        for j in tier1_indicator:
            if j in col_name:
                return True
        return False
    return True

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
        
        #checks if tier is a good choice and is not numeric and is not a date
        if good_tier_choice(column_data,col_names[i].lower()):
            #tier1
            if len(column_data) == len(set(column_data)):
                candidates_tier1.append(col_names[i])
                continue
            else:
                candidates_n_tier.append(col_names[i])

    return candidates_tier1, candidates_n_tier

def main():
    # Files to TEST algorithm 
    # filename = "covid-19 16-April.csv"
    filename = "covid-19 20-April.csv"
    # filename = "ecan_data-17-sep-19.csv"
    # filename = "transport.csv"
    # filename = "Christchurch NZ data.csv"
    # filename= "Gisborne Dc LTPB.csv"

    t1,other_tiers = read_file_and_organise_hierarchy(filename)
    if len(t1) == 0:
        print("No unique columns in csv try with another set of data")
        return None
    Max_number_of_levels = len(other_tiers) + 1
    number_of_levels = int(input(f"How many levels you would like in your application(Max num layers --> {Max_number_of_levels}) "))
    while number_of_levels < 1 or number_of_levels > Max_number_of_levels:
        print("Your chosen hierarchy is not valid\ntry again")
        number_of_levels = int(input(f"How many levels you would like in your application(Max num layers --> {Max_number_of_levels}) "))


    
    print(Fore.RED + f"Available tier 1 subjects --->  {t1}")
    counter = 2
    other_tiers.reverse()
    for i in range(number_of_levels,1,-1):
        print(Fore.BLUE + f"Recomended tier {counter} subject --->  {other_tiers[i-2]}")
        counter += 1
        

    print(Style.RESET_ALL)
main()








