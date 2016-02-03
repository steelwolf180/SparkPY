from collections import defaultdict
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

'''
#various category for supply
cat1_weight = [11,1,42,21]
cat1_value = [120,23,60,80]

cat2_weight = [20,5,13,30]
cat2_value = [8,42,23,61]

cat3_weight = [9,10,21,30]
cat3_value = [18,27,8,12]

cat4_weight = [12,9,32,18]
cat4_value = [15,27,18,28]

cat5_weight = [32,11,21,35]
cat5_value = [89,36,79,50]

#various weight for various supply
total_weight = [90,20,70,89,90]
'''

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
            total_weight.append(val)

def read_nepalcsv(): #read from IDP camp supply list
    # open csv file
    Nepal_data = open('Nepal.csv', "rt", encoding="utf-8")

    with Nepal_data as f: #gets the list of supplies from IDP supply list
        reader = csv.reader(f)
        for val in reader:
            input_snum.append(val[0])
            input_name.append(val[1])
            input_MHS.append(val[2])
            input_value.append(val[5])
            input_weight.append(val[8])

def category_data(): #categories the supply list data
    temp_cat = [int(i) for i in input_MHS] #tempoarary category list of the MHS
    temp_tv = [int(i) for i in input_value] #temporary total value for each item from supply list
    temp_wt = [int(i) for i in input_weight] #temporary weight for each item from supply list

    for i in range(len(input_snum)):
        if temp_cat[i] == 20:#check if this is category A
            cat1_value.append(temp_tv[i])
            cat1_weight.append(temp_wt[i])

        elif temp_cat[i] == 16:#check if this is category B
            cat2_value.append(temp_tv[i])
            cat2_weight.append(temp_wt[i])

        elif temp_cat[i] == 12:#check if this is category C
            cat3_value.append(temp_tv[i])
            cat3_weight.append(temp_wt[i])

        elif temp_cat[i] == 8:#check if this is category D
            cat4_value.append(temp_tv[i])
            cat4_weight.append(temp_wt[i])

        elif temp_cat[i] == 4:#check if this is category E
            cat5_value.append(temp_tv[i])
            cat5_weight.append(temp_wt[i])

def knapSack(TW, weight, value, numbers):
	temp = [int(i) for i in TW]

	K = [[0 for x in range(len(temp)+1)] for x in range(numbers+1)]

	# Build table K[][] in bottom up manner
	for i in range(numbers+1):
		for w in range(len(temp)+1):
			if i==0 or w==0:
				K[i][w] = 0
			elif weight[i-1] <= w:
				K[i][w] = max(value[i-1] + K[i-1][w-weight[i-1]], K[i-1][w])
			else:
				K[i][w] = K[i-1][w]


def display_demand():
    for i in range(5):
        if i == 0:
            numbers = len(cat1_value)
            print(knapSack(total_weight[0], cat1_weight, cat1_value, numbers))

        elif i == 1:
            numbers = len(cat2_value)
            print(knapSack(total_weight[1], cat2_weight, cat2_value, numbers))

        elif i == 2:
            numbers = len(cat3_value)
            print(knapSack(total_weight[2], cat3_weight, cat3_value, numbers))

        elif i== 3:
            numbers = len(cat4_value)
            print(knapSack(total_weight[3], cat4_weight, cat4_value, numbers))

        elif i == 4:
            numbers = len(cat5_value)
            print(knapSack(total_weight[4], cat5_weight, cat5_value, numbers))

get_inputdata()
category_data()
display_demand()