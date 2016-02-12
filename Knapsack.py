import csv

# input data from supply kit list
input_name = []
input_unit = []
input_category = []
input_weight = []
input_valPerQty = []
input_total_value = []

#input data from IDP configuration for each category and their weight for each category
config_category = {}

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
            config_category[str(val[0])] = int(val[1])


# read from IDP camp supply list
def read_supplykitcsv():
    # open csv file
    supply = open('SupplyKit.csv', "rt", encoding="utf-8")

    with supply as f:  #gets the list of supplies from IDP supply list
        reader = csv.reader(f)
        for val in reader:
            input_name.append(str(val[0]))
            input_unit.append(str(val[1]))
            input_category.append(str(val[2]))
            input_weight.append(float(val[3]))
            input_valPerQty.append(float(val[4]))
            input_total_value.append(float(val[5]))


# categories the supply list data
def category_data():
    for val in range(len(input_category)):
        if input_category[val] == "Medicines":
            medicines[input_name[val]] = (input_weight[val], input_valPerQty[val])

        elif input_category[val] == "Anaesthetics":
            anaesthetics[input_name[val]] = (input_weight[val], input_valPerQty[val])

        elif input_category[val] == "Analgesics":
            analgesics[input_name[val]] = (input_weight[val], input_valPerQty[val])

        elif input_category[val] == "Anti-allergics":
            anti_allergics[input_name[val]] = (input_weight[val], input_valPerQty[val])

        elif input_category[val] == "Anticonvulsants/antiepileptics":
            anticonvulsants[input_name[val]] = (input_weight[val], input_valPerQty[val])

        elif input_category[val] == "Antidotes":
            antidotes[input_name[val]] = (input_weight[val], input_valPerQty[val])

        elif input_category[val] == "Anti-infective medicines":
            anti_infective[input_name[val]] = (input_weight[val], input_valPerQty[val])

        elif input_category[val] == "Cardiovascular medicines":
            cardiovascular[input_name[val]] = (input_weight[val], input_valPerQty[val])

        elif input_category[val] == "Dermatological medicines":
            dermatological[input_name[val]] = (input_weight[val], input_valPerQty[val])

        elif input_category[val] == "Disinfectants and antiseptics":
            disinfectants_and_antiseptics[input_name[val]] = (input_weight[val], input_valPerQty[val])

        elif input_category[val] == "Diuretics":
            diuretics[input_name[val]] = (input_weight[val], input_valPerQty[val])

        elif input_category[val] == "Gastrointestinal medicines":
            gastrointestinal[input_name[val]] = (input_weight[val], input_valPerQty[val])

        elif input_category[val] == "Medical devices, renewable":
            renewable_medical_device[input_name[val]] = (input_weight[val], input_valPerQty[val])

        elif input_category[val] == "Guidelines for IHEK 2011 users":
            guidelines[input_name[val]] = (input_weight[val], input_valPerQty[val])

        elif input_category[val] == "Medical devices, equipment":
            equipment_medical_device[input_name[val]] = (input_weight[val], input_valPerQty[val])

        elif input_category[val] == "Stationary":
            stationary[input_name[val]] = (input_weight[val], input_valPerQty[val])


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
#display_demand()
