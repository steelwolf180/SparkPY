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

# used for knapsack algo
cache = {}

# data to send to HQ processing
IDP_CampID = {}

# get data from csv files
def get_inputdata():
    read_confile()
    read_supplykit()

# read from IDP camp the weight for each category
def read_confile():
    conf_data = open('IDPcon.csv', "rt", encoding="utf-8")
    # gets the list of weight from IDPcon.csv
    with conf_data as f:
        reader = csv.reader(f)
        for val in reader:
            #input category and total weight limit for the category
            input_category[str(val[0])] = int(val[1])

# read from IDP camp supply list
def read_supplykit():
    # open csv file
    supply = open('SupplyKit.csv', "rt", encoding="utf-8")
    item_weight = 0
    item_value = 0
    with supply as f:  #gets the list of supplies from IDP supply list
        reader = csv.reader(f)
        for val in reader:
            # check max weight and item value for the item
            item_weight = check_max_weight(int(val[4]), int(val[5]))
            item_value = calculate_total_value(int(val[3]), int(val[4]))

            # check both the max weight & item value is more than 0
            if item_weight > 0 and item_value != 0:
                input_data[str(val[0])] = [str(val[2]), item_weight, item_value, int(val[5])]

            # reset max weight and item value
            item_weight = 0
            item_value = 0

# checks input weight for each item
def check_max_weight(inputweight, maxweight):
    if inputweight <= 0:
        return (0)
    elif inputweight <= maxweight:
        return (inputweight)
    else:
        return (inputweight)

# calculates the total value for each item
def calculate_total_value(value, weight):
    return (value * weight)

# categories the supply list data
def category_data():
    for val in input_data:
        if input_data[val][0] == "Medicines":
            medicines[val] = (input_data[val][1], input_data[val][2], input_data[val][3])

        elif input_data[val][0] == "Anaesthetics":
            anaesthetics[val] = (input_data[val][1], input_data[val][2], input_data[val][3])

        elif input_data[val][0] == "Analgesics":
            analgesics[val] = (input_data[val][1], input_data[val][2], input_data[val][3])

        elif input_data[val][0] == "Anti-allergics":
            anti_allergics[val] = (input_data[val][1], input_data[val][2], input_data[val][3])

        elif input_data[val][0] == "Anticonvulsants/antiepileptics":
            anticonvulsants[val] = (input_data[val][1], input_data[val][2], input_data[val][3])

        elif input_data[val][0] == "Antidotes":
            antidotes[val] = (input_data[val][1], input_data[val][2], input_data[val][3])

        elif input_data[val][0] == "Anti-infective medicines":
            anti_infective[val] = (input_data[val][1], input_data[val][2], input_data[val][3])

        elif input_data[val][0] == "Cardiovascular medicines":
            cardiovascular[val] = (input_data[val][1], input_data[val][2], input_data[val][3])

        elif input_data[val][0] == "Dermatological medicines":
            dermatological[val] = (input_data[val][1], input_data[val][2], input_data[val][3])

        elif input_data[val][0] == "Disinfectants and antiseptics":
            disinfectants_and_antiseptics[val] = (input_data[val][1], input_data[val][2], input_data[val][3])

        elif input_data[val][0] == "Diuretics":
            diuretics[val] = (input_data[val][1], input_data[val][2], input_data[val][3])

        elif input_data[val][0] == "Gastrointestinal medicines":
            gastrointestinal[val] = (input_data[val][1], input_data[val][2], input_data[val][3])

        elif input_data[val][0] == "Medical devices, renewable":
            renewable_medical_device[val] = (input_data[val][1], input_data[val][2], input_data[val][3])

        elif input_data[val][0] == "Guidelines for IHEK 2011 users":
            guidelines[val] = (input_data[val][1], input_data[val][2], input_data[val][3])

        elif input_data[val][0] == "Medical devices, equipment":
            equipment_medical_device[val] = (input_data[val][1], input_data[val][2], input_data[val][3])

        elif input_data[val][0] == "Stationary":
            stationary[val] = (input_data[val][1], input_data[val][2], input_data[val][3])

def total_value(items, max_weight):
    return sum([x[2] for x in items]) if sum([x[1] for x in items]) < max_weight else 0

def solve(items, max_weight):
    if not items:
        return ()
    if (items, max_weight) not in cache:
        head = items[0]
        tail = items[1:]
        include = (head,) + solve(tail, max_weight - head[1])
        dont_include = solve(tail, max_weight)
        if total_value(include, max_weight) > total_value(dont_include, max_weight):
            answer = include
        else:
            answer = dont_include
        cache[(items, max_weight)] = answer
    return cache[(items, max_weight)]


get_inputdata()
category_data()
for i in stationary:
    solution = solve(stationary, input_category['Stationary'])
    print("items:")
    for x in solution:
        print(x[0], "weight:", str(x[1]), "value:", str(x[2]))
    print("value:", total_value(solution, input_category[i]))
    print("weight:", sum([x[1] for x in solution]))
