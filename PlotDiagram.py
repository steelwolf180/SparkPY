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

for i in ['IDP1', 'IDP2', 'IDP3', 'IDP4', 'IDP5']:
    medicines[i] = (0, 0)
    anaesthetics[i] = (0, 0)
    analgesics[i] = (0, 0)
    anti_allergics[i] = (0, 0)
    anticonvulsants[i] = (0, 0)
    antidotes[i] = (0, 0)
    anti_infective[i] = (0, 0)
    cardiovascular[i] = (0, 0)
    dermatological[i] = (0, 0)
    disinfectants_and_antiseptics[i] = (0, 0)
    diuretics[i] = (0, 0)
    gastrointestinal[i] = (0, 0)
    renewable_medical_device[i] = (0, 0)
    guidelines[i] = (0, 0)
    equipment_medical_device[i] = (0, 0)
    stationary[i] = (0, 0)

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


def display_category():
    catlst_weight = []
    catlst_value = []
    catlst_maxweight = []
    x = ['Medicines', 'Anaesthetics', 'Analgesics', 'Anti-Allergics', 'Anti-Convulsants', 'Antidotes',
         'Anti-Infective', 'Cardiovascular', 'Dermatological', 'Disinfectants & Anti-Septics', 'Diuretics',
         'Gastrointestinal', 'Renewable Device', 'Guidelines', 'Equipment', 'Stationary']

    for i in categoryData.values():
        catlst_weight.append(i[0])
        catlst_maxweight.append(i[2])

    trace0 = go.Bar(
        x=x,
        y=catlst_weight,
        name='Calculated'
    )
    y = catlst_maxweight
    trace1 = go.Bar(
        x=x,
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


def display_totalvalue():
    catlst_value = []
    x = ['Medicines', 'Anaesthetics', 'Analgesics', 'Anti-Allergics', 'Anti-Convulsants', 'Antidotes',
         'Anti-Infective', 'Cardiovascular', 'Dermatological', 'Disinfectants & Anti-Septics', 'Diuretics',
         'Gastrointestinal', 'Renewable Device', 'Guidelines', 'Equipment', 'Stationary']
    for i in categoryData:
        catlst_value.append(int(categoryData[i][1]))

    y = catlst_value
    trace = go.Bar(
        x=x,
        y=y,
        name='Total Value'
    )
    data = [trace]
    layout = go.Layout(
        title='Calculate Total Value For Each Category',
        width=1000,
        height=600,
        annotations=[
            dict(
                x=xi,
                y=yi,
                text=str(yi),
                xanchor='center',
                yanchor='bottom',
                showarrow=False,
            ) for xi, yi in zip(x, y)]
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='CategoryTotalValue.html')

import_supply()
import_category()
display_category()
display_totalvalue()
