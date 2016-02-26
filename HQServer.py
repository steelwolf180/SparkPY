import csv  # imports csv module
import sys  # import system module

# from pyspark import SparkContext  # spark import context
# from pyspark import SparkConf  # spark import configuration

IDP_Cat = {}
# conf = SparkConf().setMaster("local")
# sc = SparkContext(conf=conf)

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
    IDP1 = sys.argv[2]
    IDP2 = sys.argv[3]
    IDP3 = sys.argv[4]
    IDP4 = sys.argv[5]
    IDP5 = sys.argv[6]

    read_confile(IDP1)
    read_confile(IDP2)
    read_confile(IDP3)
    read_confile(IDP4)
    read_confile(IDP5)


def catgory_data():
    for val in (IDP_Cat):
        if IDP_Cat[val][0] == "Medicines":
            medicines[val] = (val, input_data[val][1], input_data[val][2])

        elif IDP_Cat[val][0] == "Anaesthetics":
            anaesthetics[val] = (val, input_data[val][1], input_data[val][2])

        elif IDP_Cat[val][0] == "Analgesics":
            analgesics[val] = (val, input_data[val][1], input_data[val][2])

        elif IDP_Cat[val][0] == "Anti-allergics":
            anti_allergics[val] = (val, input_data[val][1], input_data[val][2])

        elif IDP_Cat[val][0] == "Anticonvulsants/antiepileptics":
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

# test_spark()
read_HQ_confile()
read_IDP_data()
