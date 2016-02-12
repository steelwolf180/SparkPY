import csv

# input data from supply kit list
input_data = {}

#input data from IDP configuration for each category and their weight for each category
input_category = {}

# store input data to each individual category
medicines = {}
anaesthetics = {}
analgesics = {}
anti_allergics = {}
anticonvulsants = {}
antidotes = {}
anti_infective = {}
cardiovascular = {}
dermatological = {}
disinfectants_and_antiseptics = {}
diuretics = {}
gastrointestinal = {}
renewable_medical_device = {}
guidelines = {}
equipment_medical_device = {}
stationary = {}

#various weight for various supply
total_weight = []

#data to HQ
supply_value = {}

# get data from csv files
def get_inputdata():
    read_confile()
    read_supplykitcsv()

# read from IDP camp the weight for each category
def read_confile():
    conf_data = open('IDPcon.csv', "rt", encoding="utf-8")
    with conf_data as f: #gets the list of weight from IDPcon.csv
        reader = csv.reader(f)

        for val in reader:
            input_category[str(val[0])] = int(val[1])

# read from IDP camp supply list
def read_supplykitcsv():
    # open csv file
    supply = open('SupplyKit.csv', "rt", encoding="utf-8")

    with supply as f:  #gets the list of supplies from IDP supply list
        reader = csv.reader(f)
        for val in reader:
            input_data[str(val[0])] = (str(val[1]), str(val[2]), float(val[3]), float(val[4]), float(val[5]))


# categories the supply list data
def category_data():
    for val in input_data:
        if input_data[val][1] == "Medicines":
            medicines[val] = (input_data[val][0], input_data[val][2], input_data[val][3], input_data[val][4])

        elif input_data[val][1] == "Anaesthetics":
            anaesthetics[val] = (input_data[val][0], input_data[val][2], input_data[val][3], input_data[val][4])

        elif input_data[val][1] == "Analgesics":
            analgesics[val] = (input_data[val][0], input_data[val][2], input_data[val][3], input_data[val][4])

        elif input_data[val][1] == "Anti-allergics":
            anti_allergics[val] = (input_data[val][0], input_data[val][2], input_data[val][3], input_data[val][4])

        elif input_data[val][1] == "Anticonvulsants/antiepileptics":
            anticonvulsants[val] = (input_data[val][0], input_data[val][2], input_data[val][3], input_data[val][4])

        elif input_data[val][1] == "Antidotes":
            antidotes[val] = (input_data[val][0], input_data[val][2], input_data[val][3], input_data[val][4])

        elif input_data[val][1] == "Anti-infective medicines":
            anti_infective[val] = (input_data[val][0], input_data[val][2], input_data[val][3], input_data[val][4])

        elif input_data[val][1] == "Cardiovascular medicines":
            cardiovascular[val] = (input_data[val][0], input_data[val][2], input_data[val][3], input_data[val][4])

        elif input_data[val][1] == "Dermatological medicines":
            dermatological[val] = (input_data[val][0], input_data[val][2], input_data[val][3], input_data[val][4])

        elif input_data[val][1] == "Disinfectants and antiseptics":
            disinfectants_and_antiseptics[val] = (
            input_data[val][0], input_data[val][2], input_data[val][3], input_data[val][4])

        elif input_data[val][1] == "Diuretics":
            diuretics[val] = (input_data[val][0], input_data[val][2], input_data[val][3], input_data[val][4])

        elif input_data[val][1] == "Gastrointestinal medicines":
            gastrointestinal[val] = (input_data[val][0], input_data[val][2], input_data[val][3], input_data[val][4])

        elif input_data[val][1] == "Medical devices, renewable":
            renewable_medical_device[val] = (
            input_data[val][0], input_data[val][2], input_data[val][3], input_data[val][4])

        elif input_data[val][1] == "Guidelines for IHEK 2011 users":
            guidelines[val] = (input_data[val][0], input_data[val][2], input_data[val][3], input_data[val][4])

        elif input_data[val][1] == "Medical devices, equipment":
            equipment_medical_device[val] = (
            input_data[val][0], input_data[val][2], input_data[val][3], input_data[val][4])

        elif input_data[val][1] == "Stationary":
            stationary[val] = (input_data[val][0], input_data[val][2], input_data[val][3], input_data[val][4])

    return

#knapsack algo
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


#displays demand for each category of the supply list
def display_demand():
    for i in range(len(input_category)):
        if i == 0:
            numbers = len(medicines)
            print(input_category[i], knapSack(input_category[i][0], cat1_weight, cat1_value, numbers))


'''
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
'''
get_inputdata()
category_data()
display_demand()
