import csv  # imports csv module

import plotly.graph_objs as go  # import plotly graph objects module
import plotly.offline as py  # import offline version of plotly module

# default data
categoryData = {}
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


def import_supply():
    conf_data = open("HQ_SupplyData.csv", "rt")
    with conf_data as f:
        reader = csv.reader(f)
        for val in reader:
            if val[0] == "Medicines":
                medicines[val[1]] = (val[2], val[3])

            elif val[0] == "Anaesthetics":
                anaesthetics[val[1]] = (val[2], val[3])

            elif val[0] == "Analgesics":
                analgesics[val[1]] = (val[2], val[3])

            elif val[0] == "Anti-allergics":
                anti_allergics[val[1]] = (val[2], val[3])

            elif val[0] == "Anticonvulsants/antiepileptics":
                anticonvulsants[val[1]] = (val[2], val[3])

            elif val[0] == "Antidotes":
                diuretics[val[1]] = (val[2], val[3])

            elif val[0] == "Anti-infective medicines":
                anti_infective[val[1]] = (val[2], val[3])

            elif val[0] == "Cardiovascular medicines":
                cardiovascular[val[1]] = (val[2], val[3])

            elif val[0] == "Dermatological medicines":
                dermatological[val[1]] = (val[2], val[3])

            elif val[0] == "Disinfectants and antiseptics":
                disinfectants_and_antiseptics[val[1]] = (val[2], val[3])

            elif val[0] == "Diuretics":
                diuretics[val[1]] = (val[2], val[3])

            elif val[0] == "Gastrointestinal medicines":
                gastrointestinal[val[1]] = (val[2], val[3])

            elif val[0] == "Medical devices, renewable":
                renewable_medical_device[val[1]] = (val[2], val[3])

            elif val[0] == "Guidelines for IHEK 2011 users":
                guidelines[val[1]] = (val[2], val[3])

            elif val[0] == "Medical devices, equipment":
                equipment_medical_device[val[1]] = (val[2], val[3])

            elif val[0] == "Stationary":
                stationary[val[1]] = (val[2], val[3])


def import_category():
    conf_data = open("HQ_CategoryData.csv", "rt")
    with conf_data as f:
        reader = csv.reader(f)
        for val in reader:
            categoryData[val[0]] = (val[1], val[2], val[3])


def display_supply():
    trace1 = go.Bar(
        x=['dog', 'cat', 'mouse'],
        y=[3, 7, 8],
        name='SF Zoo'
    )
    trace2 = go.Bar(
        x=['dog', 'cat', 'mouse'],
        y=[7, 11, 12],
        name='LA Zoo'
    )
    trace3 = go.Bar(
        x=['dog', 'cat', 'mouse'],
        y=[5, 6, 9],
        name='SF Zoo'
    )
    data = [trace1, trace2, trace3]
    layout = go.Layout(
        barmode='stack'
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='SupplyData.html')


def display_category():
    catlst_weight = []
    catlst_value = []
    catlst_maxweight = []

    for i in categoryData.values():
        catlst_weight.append(i[0])
        catlst_value.append(i[1])
        catlst_maxweight.append(i[2])

    trace0 = go.Bar(
        x=['Medicines', 'Anaesthetics', 'Analgesics', 'Anti-Allergics', 'Anti-Convulsants', 'Antidotes',
           'Anti-Infective', 'Cardiovascular', 'Dermatological', 'Disinfectants & Anti-Septics', 'Diuretics',
           'Gastrointestinal', 'Renewable Device', 'Guidelines', 'Equipment', 'Stationary'],
        y=catlst_weight,
        name='Calculated'
    )

    trace1 = go.Bar(
        x=['Medicines', 'Anaesthetics', 'Analgesics', 'Anti-Allergics', 'Anti-Convulsants', 'Antidotes',
           'Anti-Infective', 'Cardiovascular', 'Dermatological', 'Disinfectants & Anti-Septics', 'Diuretics',
           'Gastrointestinal', 'Renewable Device', 'Guidelines', 'Equipment', 'Stationary'],
        y=catlst_maxweight,
        name='Maxinmum'
    )
    data = [trace0, trace1]
    layout = go.Layout(
        title='Individual Category Calculate Weight and Maximum Weight',
        barmode='group',
        width=1000,
        height=600
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='CategoryData.html')


import_supply()
import_category()
display_category()
#display_supply()
