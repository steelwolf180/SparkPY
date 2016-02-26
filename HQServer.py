import csv  # imports csv module
import os  # imports os module
import sys  # imports system module

# from pyspark import SparkContext  # spark import context
# from pyspark import SparkConf  # spark import configuration

IDP_Cat = {}
# conf = SparkConf().setMaster("local")
# sc = SparkContext(conf=conf)

# HQ supply data for processing
HQ_supply_data = {}
HQ_cat_data = {}

# used for knapsack algo
cache = {}

# input IDP camp list
IDP_camp1 = {}
IDP_camp2 = {}
IDP_camp3 = {}
IDP_camp4 = {}
IDP_camp5 = {}

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

# tests if the spark module is working
def test_spark():
    try:
        from pyspark import SparkContext
        from pyspark import SparkConf
        print("Successfully imported Spark Modules")

    except ImportError as e:
        print ("Can not import Spark Modules", e)
        sys.exit(1)


def read_confile(input_file):
    conf_data = open(input_file, "rt")
    # gets the list of weight from HQcon.csv

    if input_file != sys.argv[1]:
        if input_file == "IDP_Supply_List1.csv":
            with conf_data as f:
                reader = csv.reader(f)
                for val in reader:
                    # input category and total weight limit for the category
                    IDP_camp1[str(val[0])] = (int(val[1]), int(val[2]), int(val[3]))
        elif input_file == "IDP_Supply_List2.csv":
            with conf_data as f:
                reader = csv.reader(f)
                for val in reader:
                    # input category and total weight limit for the category
                    IDP_camp2[str(val[0])] = (int(val[1]), int(val[2]), int(val[3]))
        elif input_file == "IDP_Supply_List3.csv":
            with conf_data as f:
                reader = csv.reader(f)
                for val in reader:
                    # input category and total weight limit for the category
                    IDP_camp3[str(val[0])] = (int(val[1]), int(val[2]), int(val[3]))
        elif input_file == "IDP_Supply_List4.csv":
            with conf_data as f:
                reader = csv.reader(f)
                for val in reader:
                    # input category and total weight limit for the category
                    IDP_camp4[str(val[0])] = (int(val[1]), int(val[2]), int(val[3]))
        elif input_file == "IDP_Supply_List5.csv":
            with conf_data as f:
                reader = csv.reader(f)
                for val in reader:
                    # input category and total weight limit for the category
                    IDP_camp5[str(val[0])] = (int(val[1]), int(val[2]), int(val[3]))
    else:
        with conf_data as f:
            reader = csv.reader(f)
            for val in reader:
                # input category and total weight limit for the category
                IDP_Cat[str(val[0])] = int(val[1])


# reads settings of HQ supply list
def read_HQ_confile():
    filename = sys.argv[1]
    read_confile(filename)


# setup read from various idp supply list file
def read_IDP_data():
    IDP1 = sys.argv[4]
    IDP2 = sys.argv[5]
    IDP3 = sys.argv[6]
    IDP4 = sys.argv[7]
    IDP5 = sys.argv[8]

    read_confile(IDP1)
    read_confile(IDP2)
    read_confile(IDP3)
    read_confile(IDP4)
    read_confile(IDP5)


def catgory_data():
    for val in (IDP_Cat):
        if val == "Medicines":
            medicines['IDP1'] = ('IDP1', IDP_camp1[val][0], IDP_camp1[val][1], IDP_camp1[val][2])
            medicines['IDP2'] = ('IDP2', IDP_camp2[val][0], IDP_camp2[val][1], IDP_camp2[val][2])
            medicines['IDP3'] = ('IDP3', IDP_camp3[val][0], IDP_camp3[val][1], IDP_camp3[val][2])
            medicines['IDP4'] = ('IDP4', IDP_camp4[val][0], IDP_camp4[val][1], IDP_camp4[val][2])
            medicines['IDP5'] = ('IDP5', IDP_camp5[val][0], IDP_camp5[val][1], IDP_camp5[val][2])

        elif val == "Anaesthetics":
            anaesthetics['IDP1'] = ('IDP1', IDP_camp1[val][0], IDP_camp1[val][1], IDP_camp1[val][2])
            anaesthetics['IDP2'] = ('IDP2', IDP_camp2[val][0], IDP_camp2[val][1], IDP_camp2[val][2])
            anaesthetics['IDP3'] = ('IDP3', IDP_camp3[val][0], IDP_camp3[val][1], IDP_camp3[val][2])
            anaesthetics['IDP4'] = ('IDP4', IDP_camp4[val][0], IDP_camp4[val][1], IDP_camp4[val][2])
            anaesthetics['IDP5'] = ('IDP5', IDP_camp5[val][0], IDP_camp5[val][1], IDP_camp5[val][2])


        elif val == "Analgesics":
            analgesics['IDP1'] = ('IDP1', IDP_camp1[val][0], IDP_camp1[val][1], IDP_camp1[val][2])
            analgesics['IDP2'] = ('IDP2', IDP_camp2[val][0], IDP_camp2[val][1], IDP_camp2[val][2])
            analgesics['IDP3'] = ('IDP3', IDP_camp3[val][0], IDP_camp3[val][1], IDP_camp3[val][2])
            analgesics['IDP4'] = ('IDP4', IDP_camp4[val][0], IDP_camp4[val][1], IDP_camp4[val][2])
            analgesics['IDP5'] = ('IDP5', IDP_camp5[val][0], IDP_camp5[val][1], IDP_camp5[val][2])

        elif val == "Anti-allergics":
            anti_allergics['IDP1'] = ('IDP1', IDP_camp1[val][0], IDP_camp1[val][1], IDP_camp1[val][2])
            anti_allergics['IDP2'] = ('IDP2', IDP_camp2[val][0], IDP_camp2[val][1], IDP_camp2[val][2])
            anti_allergics['IDP3'] = ('IDP3', IDP_camp3[val][0], IDP_camp3[val][1], IDP_camp3[val][2])
            anti_allergics['IDP4'] = ('IDP4', IDP_camp4[val][0], IDP_camp4[val][1], IDP_camp4[val][2])
            anti_allergics['IDP5'] = ('IDP5', IDP_camp5[val][0], IDP_camp5[val][1], IDP_camp5[val][2])


        elif val == "Anticonvulsants/antiepileptics":
            anticonvulsants['IDP1'] = ('IDP1', IDP_camp1[val][0], IDP_camp1[val][1], IDP_camp1[val][2])
            anticonvulsants['IDP2'] = ('IDP2', IDP_camp2[val][0], IDP_camp2[val][1], IDP_camp2[val][2])
            anticonvulsants['IDP3'] = ('IDP3', IDP_camp3[val][0], IDP_camp3[val][1], IDP_camp3[val][2])
            anticonvulsants['IDP4'] = ('IDP4', IDP_camp4[val][0], IDP_camp4[val][1], IDP_camp4[val][2])
            anticonvulsants['IDP5'] = ('IDP5', IDP_camp5[val][0], IDP_camp5[val][1], IDP_camp5[val][2])

        elif val == "Antidotes":
            antidotes['IDP1'] = ('IDP1', IDP_camp1[val][0], IDP_camp1[val][1], IDP_camp1[val][2])
            antidotes['IDP2'] = ('IDP2', IDP_camp2[val][0], IDP_camp2[val][1], IDP_camp2[val][2])
            antidotes['IDP3'] = ('IDP3', IDP_camp3[val][0], IDP_camp3[val][1], IDP_camp3[val][2])
            antidotes['IDP4'] = ('IDP4', IDP_camp4[val][0], IDP_camp4[val][1], IDP_camp4[val][2])
            antidotes['IDP5'] = ('IDP5', IDP_camp5[val][0], IDP_camp5[val][1], IDP_camp5[val][2])

        elif val == "Anti-infective medicines":
            anti_infective['IDP1'] = ('IDP1', IDP_camp1[val][0], IDP_camp1[val][1], IDP_camp1[val][2])
            anti_infective['IDP2'] = ('IDP2', IDP_camp2[val][0], IDP_camp2[val][1], IDP_camp2[val][2])
            anti_infective['IDP3'] = ('IDP3', IDP_camp3[val][0], IDP_camp3[val][1], IDP_camp3[val][2])
            anti_infective['IDP4'] = ('IDP4', IDP_camp4[val][0], IDP_camp4[val][1], IDP_camp4[val][2])
            anti_infective['IDP5'] = ('IDP5', IDP_camp5[val][0], IDP_camp5[val][1], IDP_camp5[val][2])

        elif val == "Cardiovascular medicines":
            cardiovascular['IDP1'] = ('IDP1', IDP_camp1[val][0], IDP_camp1[val][1], IDP_camp1[val][2])
            cardiovascular['IDP2'] = ('IDP2', IDP_camp2[val][0], IDP_camp2[val][1], IDP_camp2[val][2])
            cardiovascular['IDP3'] = ('IDP3', IDP_camp3[val][0], IDP_camp3[val][1], IDP_camp3[val][2])
            cardiovascular['IDP4'] = ('IDP4', IDP_camp4[val][0], IDP_camp4[val][1], IDP_camp4[val][2])
            cardiovascular['IDP5'] = ('IDP5', IDP_camp5[val][0], IDP_camp5[val][1], IDP_camp5[val][2])

        elif val == "Dermatological medicines":
            dermatological['IDP1'] = ('IDP1', IDP_camp1[val][0], IDP_camp1[val][1], IDP_camp1[val][2])
            dermatological['IDP2'] = ('IDP2', IDP_camp2[val][0], IDP_camp2[val][1], IDP_camp2[val][2])
            dermatological['IDP3'] = ('IDP3', IDP_camp3[val][0], IDP_camp3[val][1], IDP_camp3[val][2])
            dermatological['IDP4'] = ('IDP4', IDP_camp4[val][0], IDP_camp4[val][1], IDP_camp4[val][2])
            dermatological['IDP5'] = ('IDP5', IDP_camp5[val][0], IDP_camp5[val][1], IDP_camp5[val][2])

        elif val == "Disinfectants and antiseptics":
            disinfectants_and_antiseptics['IDP1'] = ('IDP1', IDP_camp1[val][0], IDP_camp1[val][1], IDP_camp1[val][2])
            disinfectants_and_antiseptics['IDP2'] = ('IDP2', IDP_camp2[val][0], IDP_camp2[val][1], IDP_camp2[val][2])
            disinfectants_and_antiseptics['IDP3'] = ('IDP3', IDP_camp3[val][0], IDP_camp3[val][1], IDP_camp3[val][2])
            disinfectants_and_antiseptics['IDP4'] = ('IDP4', IDP_camp4[val][0], IDP_camp4[val][1], IDP_camp4[val][2])
            disinfectants_and_antiseptics['IDP5'] = ('IDP5', IDP_camp5[val][0], IDP_camp5[val][1], IDP_camp5[val][2])

        elif val == "Diuretics":
            diuretics['IDP1'] = ('IDP1', IDP_camp1[val][0], IDP_camp1[val][1], IDP_camp1[val][2])
            diuretics['IDP2'] = ('IDP2', IDP_camp2[val][0], IDP_camp2[val][1], IDP_camp2[val][2])
            diuretics['IDP3'] = ('IDP3', IDP_camp3[val][0], IDP_camp3[val][1], IDP_camp3[val][2])
            diuretics['IDP4'] = ('IDP4', IDP_camp4[val][0], IDP_camp4[val][1], IDP_camp4[val][2])
            diuretics['IDP5'] = ('IDP5', IDP_camp5[val][0], IDP_camp5[val][1], IDP_camp5[val][2])

        elif val == "Gastrointestinal medicines":
            gastrointestinal['IDP1'] = ('IDP1', IDP_camp1[val][0], IDP_camp1[val][1], IDP_camp1[val][2])
            gastrointestinal['IDP2'] = ('IDP2', IDP_camp2[val][0], IDP_camp2[val][1], IDP_camp2[val][2])
            gastrointestinal['IDP3'] = ('IDP3', IDP_camp3[val][0], IDP_camp3[val][1], IDP_camp3[val][2])
            gastrointestinal['IDP4'] = ('IDP4', IDP_camp4[val][0], IDP_camp4[val][1], IDP_camp4[val][2])
            gastrointestinal['IDP5'] = ('IDP5', IDP_camp5[val][0], IDP_camp5[val][1], IDP_camp5[val][2])

        elif val == "Medical devices, renewable":
            renewable_medical_device['IDP1'] = ('IDP1', IDP_camp1[val][0], IDP_camp1[val][1], IDP_camp1[val][2])
            renewable_medical_device['IDP2'] = ('IDP2', IDP_camp2[val][0], IDP_camp2[val][1], IDP_camp2[val][2])
            renewable_medical_device['IDP3'] = ('IDP3', IDP_camp3[val][0], IDP_camp3[val][1], IDP_camp3[val][2])
            renewable_medical_device['IDP4'] = ('IDP4', IDP_camp4[val][0], IDP_camp4[val][1], IDP_camp4[val][2])
            renewable_medical_device['IDP5'] = ('IDP5', IDP_camp5[val][0], IDP_camp5[val][1], IDP_camp5[val][2])

        elif val == "Guidelines for IHEK 2011 users":
            guidelines['IDP1'] = ('IDP1', IDP_camp1[val][0], IDP_camp1[val][1], IDP_camp1[val][2])
            guidelines['IDP2'] = ('IDP2', IDP_camp2[val][0], IDP_camp2[val][1], IDP_camp2[val][2])
            guidelines['IDP3'] = ('IDP3', IDP_camp3[val][0], IDP_camp3[val][1], IDP_camp3[val][2])
            guidelines['IDP4'] = ('IDP4', IDP_camp4[val][0], IDP_camp4[val][1], IDP_camp4[val][2])
            guidelines['IDP5'] = ('IDP5', IDP_camp5[val][0], IDP_camp5[val][1], IDP_camp5[val][2])

        elif val == "Medical devices, equipment":
            equipment_medical_device['IDP1'] = ('IDP1', IDP_camp1[val][0], IDP_camp1[val][1], IDP_camp1[val][2])
            equipment_medical_device['IDP2'] = ('IDP2', IDP_camp2[val][0], IDP_camp2[val][1], IDP_camp2[val][2])
            equipment_medical_device['IDP3'] = ('IDP3', IDP_camp3[val][0], IDP_camp3[val][1], IDP_camp3[val][2])
            equipment_medical_device['IDP4'] = ('IDP4', IDP_camp4[val][0], IDP_camp4[val][1], IDP_camp4[val][2])
            equipment_medical_device['IDP5'] = ('IDP5', IDP_camp5[val][0], IDP_camp5[val][1], IDP_camp5[val][2])
        elif val == "Stationary":
            stationary['IDP1'] = ('IDP1', IDP_camp1[val][0], IDP_camp1[val][1], IDP_camp1[val][2])
            stationary['IDP2'] = ('IDP2', IDP_camp2[val][0], IDP_camp2[val][1], IDP_camp2[val][2])
            stationary['IDP3'] = ('IDP3', IDP_camp3[val][0], IDP_camp3[val][1], IDP_camp3[val][2])
            stationary['IDP4'] = ('IDP4', IDP_camp4[val][0], IDP_camp4[val][1], IDP_camp4[val][2])
            stationary['IDP5'] = ('IDP5', IDP_camp5[val][0], IDP_camp5[val][1], IDP_camp5[val][2])


def create_tuple_list(lst):
    tuple_lst = ()
    for i in lst:
        tuple_lst += (lst[i],)
    return tuple_lst


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


def process_category():
    temp_tpl = ()
    for i in IDP_Cat:
        if i == "Medicines":
            temp_tpl = create_tuple_list(medicines)
            display_IDP_Camps(temp_tpl, IDP_Cat[i], i)
            temp_tpl = ()

        elif i == "Anaesthetics":
            temp_tpl = create_tuple_list(anaesthetics)
            display_IDP_Camps(temp_tpl, IDP_Cat[i], i)
            temp_tpl = ()
        elif i == "Analgesics":
            temp_tpl = create_tuple_list(analgesics)
            display_IDP_Camps(temp_tpl, IDP_Cat[i], i)
            temp_tpl = ()
        elif i == "Anti-allergics":
            temp_tpl = create_tuple_list(anti_allergics)
            display_IDP_Camps(temp_tpl, IDP_Cat[i], i)
            temp_tpl = ()
        elif i == "Anticonvulsants/antiepileptics":
            temp_tpl = create_tuple_list(anticonvulsants)
            display_IDP_Camps(temp_tpl, IDP_Cat[i], i)
            temp_tpl = ()
        elif i == "Antidotes":
            temp_tpl = create_tuple_list(antidotes)
            display_IDP_Camps(temp_tpl, IDP_Cat[i], i)
            temp_tpl = ()
        elif i == "Anti-infective medicines":
            temp_tpl = create_tuple_list(anti_infective)
            display_IDP_Camps(temp_tpl, IDP_Cat[i], i)
            temp_tpl = ()
        elif i == "Cardiovascular medicines":
            temp_tpl = create_tuple_list(cardiovascular)
            display_IDP_Camps(temp_tpl, IDP_Cat[i], i)
            temp_tpl = ()
        elif i == "Dermatological medicines":
            temp_tpl = create_tuple_list(dermatological)
            display_IDP_Camps(temp_tpl, IDP_Cat[i], i)
            temp_tpl = ()
        elif i == "Disinfectants and antiseptics":
            temp_tpl = create_tuple_list(disinfectants_and_antiseptics)
            display_IDP_Camps(temp_tpl, IDP_Cat[i], i)
            temp_tpl = ()
        elif i == "Diuretics":
            temp_tpl = create_tuple_list(diuretics)
            display_IDP_Camps(temp_tpl, IDP_Cat[i], i)
            temp_tpl = ()
        elif i == "Gastrointestinal medicines":
            temp_tpl = create_tuple_list(gastrointestinal)
            display_IDP_Camps(temp_tpl, IDP_Cat[i], i)
            temp_tpl = ()
        elif i == "Medical devices, renewable":
            temp_tpl = create_tuple_list(renewable_medical_device)
            display_IDP_Camps(temp_tpl, IDP_Cat[i], i)
            temp_tpl = ()
        elif i == "Guidelines for IHEK 2011 users":
            temp_tpl = create_tuple_list(guidelines)
            display_IDP_Camps(temp_tpl, IDP_Cat[i], i)
            temp_tpl = ()
        elif i == "Medical devices, equipment":
            temp_tpl = create_tuple_list(equipment_medical_device)
            display_IDP_Camps(temp_tpl, IDP_Cat[i], i)
            temp_tpl = ()
        elif i == "Stationary":
            temp_tpl = create_tuple_list(stationary)
            display_IDP_Camps(temp_tpl, IDP_Cat[i], i)
            temp_tpl = ()


def display_IDP_Camps(tuple_lst, maxweight, cat_name):
    solution = solve(tuple_lst, maxweight)
    cat_weight = sum([x[1] for x in solution])
    cat_value = total_value(solution, maxweight)

    print("Category", cat_name)
    print("items:")
    for x in solution:
        print(x[0], "weight:", str(x[1]), "value:", str(x[2]))
        HQ_cat_data[cat_name, x[0]] = (x[0], str(x[1]), str(x[2]))
    print("Calculated value:", cat_value)
    print("Calculated weight:", cat_weight)
    print("Max weight for category:", maxweight)
    print('===================================================================================================')

    HQ_supply_data[cat_name] = (cat_weight, cat_value, maxweight)


def export_category():
    output_file = sys.argv[2]
    output_file2 = sys.argv[3]
    # file location to write to csv file
    currentPath = os.getcwd()
    csv_file = currentPath + "/" + output_file
    csv_file2 = currentPath + "/" + output_file2

    # write file to csv
    with open(csv_file, 'w') as f:
        writer = csv.writer(f)
        for i in sorted(HQ_supply_data):
            writer.writerow((i, HQ_supply_data[i][0], HQ_supply_data[i][1], HQ_supply_data[i][2]))

    with open(csv_file2, 'w') as f:
        writer = csv.writer(f)
        for k, v in sorted(HQ_cat_data):
            writer.writerow((k, v, HQ_cat_data[k, v][1], HQ_cat_data[k, v][2]))
# test_spark()
read_HQ_confile()
read_IDP_data()
catgory_data()
process_category()
export_category()
