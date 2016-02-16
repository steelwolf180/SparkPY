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
            medicines[val] = (val, input_data[val][1], input_data[val][2])

        elif input_data[val][0] == "Anaesthetics":
            anaesthetics[val] = (val, input_data[val][1], input_data[val][2])

        elif input_data[val][0] == "Analgesics":
            analgesics[val] = (val, input_data[val][1], input_data[val][2])

        elif input_data[val][0] == "Anti-allergics":
            anti_allergics[val] = (val, input_data[val][1], input_data[val][2])

        elif input_data[val][0] == "Anticonvulsants/antiepileptics":
            anticonvulsants[val] = (val, input_data[val][1], input_data[val][2])

        elif input_data[val][0] == "Antidotes":
            antidotes[val] = (val, input_data[val][1], input_data[val][2])

        elif input_data[val][0] == "Anti-infective medicines":
            anti_infective[val] = (val, input_data[val][1], input_data[val][2])

        elif input_data[val][0] == "Cardiovascular medicines":
            cardiovascular[val] = (val, input_data[val][1], input_data[val][2])

        elif input_data[val][0] == "Dermatological medicines":
            dermatological[val] = (val, input_data[val][1], input_data[val][2])

        elif input_data[val][0] == "Disinfectants and antiseptics":
            disinfectants_and_antiseptics[val] = (val, input_data[val][1], input_data[val][2])

        elif input_data[val][0] == "Diuretics":
            diuretics[val] = (val, input_data[val][1], input_data[val][2])

        elif input_data[val][0] == "Gastrointestinal medicines":
            gastrointestinal[val] = (val, input_data[val][1], input_data[val][2])

        elif input_data[val][0] == "Medical devices, renewable":
            renewable_medical_device[val] = (val, input_data[val][1], input_data[val][2])

        elif input_data[val][0] == "Guidelines for IHEK 2011 users":
            guidelines[val] = (val, input_data[val][1], input_data[val][2])

        elif input_data[val][0] == "Medical devices, equipment":
            equipment_medical_device[val] = (val, input_data[val][1], input_data[val][2])

        elif input_data[val][0] == "Stationary":
            stationary[val] = (val, input_data[val][1], input_data[val][2])


# convert into tuple list from each individual category dictionary for processing
def create_tuple_list(lst):
    tuple_lst = ()
    for i in lst:
        tuple_lst += (lst[i],)
    return tuple_lst


# sending each category for processing
def process_category():
    temp_tpl = ()

    for i in input_category:
        if i == "Medicines":
            temp_tpl = create_tuple_list(medicines)
            temp_tpl = ()
        elif i == "Anaesthetics":
            temp_tpl = create_tuple_list(anaesthetics)
            temp_tpl = ()
        elif i == "Analgesics":
            temp_tpl = create_tuple_list(analgesics)
            temp_tpl = ()
        elif i == "Anti-allergics":
            temp_tpl = create_tuple_list(anti_allergics)
            temp_tpl = ()
        elif i == "Anticonvulsants/antiepileptics":
            temp_tpl = create_tuple_list(anticonvulsants)
            temp_tpl = ()
        elif i == "Antidotes":
            temp_tpl = create_tuple_list(antidotes)
            temp_tpl = ()
        elif i == "Anti-infective medicines":
            temp_tpl = create_tuple_list(anti_infective)
            temp_tpl = ()
        elif i == "Cardiovascular medicines":
            temp_tpl = create_tuple_list(cardiovascular)
            temp_tpl = ()
        elif i == "Dermatological medicines":
            temp_tpl = create_tuple_list(dermatological)
            temp_tpl = ()
        elif i == "Disinfectants and antiseptics":
            temp_tpl = create_tuple_list(disinfectants_and_antiseptics)
            temp_tpl = ()
        elif i == "Diuretics":
            temp_tpl = create_tuple_list(diuretics)
            temp_tpl = ()
        elif i == "Gastrointestinal medicines":
            temp_tpl = create_tuple_list(gastrointestinal)
            temp_tpl = ()
        elif i == "Medical devices, renewable":
            temp_tpl = create_tuple_list(renewable_medical_device)
            temp_tpl = ()
        elif i == "Guidelines for IHEK 2011 users":
            temp_tpl = create_tuple_list(guidelines)
            temp_tpl = ()
        elif i == "Medical devices, equipment":
            temp_tpl = create_tuple_list(equipment_medical_device)
            temp_tpl = ()
        elif i == "Stationary":
            temp_tpl = create_tuple_list(stationary)
            temp_tpl = ()


# gets total value for the category
def total_value(items, max_weight):
    return sum([x[2] for x in items]) if sum([x[1] for x in items]) < max_weight else 0


# knapsack algo for each category
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
create_tuple_list(stationary)
process_category()
