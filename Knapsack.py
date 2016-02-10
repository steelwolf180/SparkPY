import csv

input_snum = []
input_name = []
input_MHS = []
input_value = []
input_weight=[]

cat1_weight = []
cat1_value = []

cat2_weight = []
cat2_value = []

cat3_weight = []
cat3_value = []

cat4_weight = []
cat4_value = []

cat5_weight = []
cat5_value = []

#various weight for various supply
total_weight = []

#data to HQ
supply_value = {}

def get_inputdata(): #read from csv
    read_confile()
    read_nepalcsv()

def read_confile(): #read from IDP camp the weight for each category
    conf_data = open('IDPcon.csv', "rt", encoding="utf-8")
    with conf_data as f: #gets the list of weight from IDPcon.csv
        reader = csv.reader(f)

        for val in reader:
            total_weight.append(int(val[0]))
            total_weight.append(int(val[1]))
            total_weight.append(int(val[2]))
            total_weight.append(int(val[3]))
            total_weight.append(int(val[4]))

def read_nepalcsv(): #read from IDP camp supply list
    # open csv file
    Nepal_data = open('Nepal.csv', "rt", encoding="utf-8")

    with Nepal_data as f: #gets the list of supplies from IDP supply list
        reader = csv.reader(f)
        for val in reader:
            input_snum.append(int(val[0]))
            input_name.append(val[1])
            input_MHS.append(int(val[2]))
            input_value.append(int(val[5]))
            input_weight.append(int(val[8]))

def category_data(): #categories the supply list data

    for i in range(len(input_snum)):
        if input_MHS[i] == 20:#check if this is category A
            cat1_value.append(input_value[i])
            cat1_weight.append(input_weight[i])

        elif input_MHS[i] == 16:#check if this is category B
            cat2_value.append(input_value[i])
            cat2_weight.append(input_weight[i])

        elif input_MHS[i] == 12:#check if this is category C
            cat3_value.append(input_value[i])
            cat3_weight.append(input_weight[i])

        elif input_MHS[i] == 8:#check if this is category D
            cat4_value.append(input_value[i])
            cat4_weight.append(input_weight[i])

        elif input_MHS[i] == 4:#check if this is category E
            cat5_value.append(input_value[i])
            cat5_weight.append(input_weight[i])

def knapSack(temp_tw, weight, value, numbers):
    K = [[0 for x in range(temp_tw+1)] for x in range(numbers+1)]

    #Build table K[][] in bottom up manner
    for i in range(numbers+1):
        for w in range(temp_tw+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif weight[i-1] <= w:
                K[i][w] = max(value[i-1] + K[i-1][w-weight[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[numbers][temp_tw]

def display_demand():


    for i in range(5):
        if i == 0:
            numbers = len(cat1_value)
            print("Category A:", knapSack(total_weight[i], cat1_weight, cat1_value, numbers))

        elif i == 1:
            numbers = len(cat2_value)
            print("Category B:",knapSack(total_weight[i], cat2_weight, cat2_value, numbers))

        elif i == 2:
            numbers = len(cat3_value)
            print("Category C:",knapSack(total_weight[i], cat3_weight, cat3_value, numbers))

        elif i== 3:
            numbers = len(cat4_value)
            print("Category D:",knapSack(total_weight[i], cat4_weight, cat4_value, numbers))

        elif i == 4:
            numbers = len(cat5_value)
            print("Category E:",knapSack(total_weight[i], cat5_weight, cat5_value, numbers))

get_inputdata()
category_data()
display_demand()