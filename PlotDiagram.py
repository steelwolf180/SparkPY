# coding=utf-8
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


def generate_category_data():
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
    weight = []
    max_weight = []

    x = sorted(categoryData)

    for index in x:
        weight.append(categoryData[index][0])
        max_weight.append(categoryData[index][2])

    trace0 = go.Bar(
        x=x,
        y=weight,
        name='Demand'
    )
    y = max_weight
    trace1 = go.Bar(
        x=x,
        y=max_weight,
        name='Supply'
    )
    data = [trace0, trace1]
    layout = go.Layout(
        title='HQ Supply vs Demand For Each Category',
        barmode='group',
        width=1000,
        height=600
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='CategoryData.html')


def display_total_value():
    catlst = []

    x = sorted(categoryData)

    for i in x:
        catlst.append(int(categoryData[i][1]))

    y = catlst
    trace = go.Bar(
        x=x,
        y=y,
        name='Total Value'
    )
    data = [trace]
    layout = go.Layout(
        title='Calculated Total Value Supplies Demand For Each Category From All IDP Camps in HQ',
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


def display_supply_value():
    label = sorted(categoryData)
    IDP1 = []
    IDP2 = []
    IDP3 = []
    IDP4 = []
    IDP5 = []

    for i in ['IDP1', 'IDP2', 'IDP3', 'IDP4', 'IDP5']:
        if i == 'IDP1':
            IDP1.append(anaesthetics[i][1])
            IDP1.append(analgesics[i][1])
            IDP1.append(anti_allergics[i][1])
            IDP1.append(anti_infective[i][1])
            IDP1.append(anticonvulsants[i][1])
            IDP1.append(antidotes[i][1])
            IDP1.append(cardiovascular[i][1])
            IDP1.append(dermatological[i][1])
            IDP1.append(disinfectants_and_antiseptics[i][1])
            IDP1.append(diuretics[i][1])
            IDP1.append(gastrointestinal[i][1])
            IDP1.append(guidelines[i][1])
            IDP1.append(equipment_medical_device[i][1])
            IDP1.append(renewable_medical_device[i][1])
            IDP1.append(medicines[i][1])
            IDP1.append(stationary[i][1])

        elif i == 'IDP2':
            IDP2.append(anaesthetics[i][1])
            IDP2.append(analgesics[i][1])
            IDP2.append(anti_allergics[i][1])
            IDP2.append(anti_infective[i][1])
            IDP2.append(anticonvulsants[i][1])
            IDP2.append(antidotes[i][1])
            IDP2.append(cardiovascular[i][1])
            IDP2.append(dermatological[i][1])
            IDP2.append(disinfectants_and_antiseptics[i][1])
            IDP2.append(diuretics[i][1])
            IDP2.append(gastrointestinal[i][1])
            IDP2.append(guidelines[i][1])
            IDP2.append(equipment_medical_device[i][1])
            IDP2.append(renewable_medical_device[i][1])
            IDP2.append(medicines[i][1])
            IDP2.append(stationary[i][1])

        elif i == 'IDP3':
            IDP3.append(anaesthetics[i][1])
            IDP3.append(analgesics[i][1])
            IDP3.append(anti_allergics[i][1])
            IDP3.append(anti_infective[i][1])
            IDP3.append(anticonvulsants[i][1])
            IDP3.append(antidotes[i][1])
            IDP3.append(cardiovascular[i][1])
            IDP3.append(dermatological[i][1])
            IDP3.append(disinfectants_and_antiseptics[i][1])
            IDP3.append(diuretics[i][1])
            IDP3.append(gastrointestinal[i][1])
            IDP3.append(guidelines[i][1])
            IDP3.append(equipment_medical_device[i][1])
            IDP3.append(renewable_medical_device[i][1])
            IDP3.append(medicines[i][1])
            IDP3.append(stationary[i][1])

        elif i == 'IDP4':
            IDP4.append(anaesthetics[i][1])
            IDP4.append(analgesics[i][1])
            IDP4.append(anti_allergics[i][1])
            IDP4.append(anti_infective[i][1])
            IDP4.append(anticonvulsants[i][1])
            IDP4.append(antidotes[i][1])
            IDP4.append(cardiovascular[i][1])
            IDP4.append(dermatological[i][1])
            IDP4.append(disinfectants_and_antiseptics[i][1])
            IDP4.append(diuretics[i][1])
            IDP4.append(gastrointestinal[i][1])
            IDP4.append(guidelines[i][1])
            IDP4.append(equipment_medical_device[i][1])
            IDP4.append(renewable_medical_device[i][1])
            IDP4.append(medicines[i][1])
            IDP4.append(stationary[i][1])

        elif i == 'IDP5':
            IDP5.append(anaesthetics[i][1])
            IDP5.append(analgesics[i][1])
            IDP5.append(anti_allergics[i][1])
            IDP5.append(anti_infective[i][1])
            IDP5.append(anticonvulsants[i][1])
            IDP5.append(antidotes[i][1])
            IDP5.append(cardiovascular[i][1])
            IDP5.append(dermatological[i][1])
            IDP5.append(disinfectants_and_antiseptics[i][1])
            IDP5.append(diuretics[i][1])
            IDP5.append(gastrointestinal[i][1])
            IDP5.append(guidelines[i][1])
            IDP5.append(equipment_medical_device[i][1])
            IDP5.append(renewable_medical_device[i][1])
            IDP5.append(medicines[i][1])
            IDP5.append(stationary[i][1])

    fig = {
        'data': [
            {
                'labels': label,
                'values': IDP1,
                'type': 'pie',
                'name': 'IDP Camp 1',
                'domain': {'x': [0, .48],
                           'y': [.51, 1]},
                'hoverinfo': 'label+percent+value+name',
                'textinfo': 'none'
            },
            {
                'labels': label,
                'values': IDP2,
                'type': 'pie',
                'name': 'IDP Camp 2',
                'domain': {'x': [0.3, 0.7],
                           'y': [0.51, 1]},
                'hoverinfo': 'label+percent+value+name',
                'textinfo': 'none'
            },
            {
                'labels': label,
                'values': IDP3,
                'type': 'pie',
                'name': 'IDP Camp 3',
                'domain': {'x': [.52, 1],
                           'y': [.51, 1]},
                'hoverinfo': 'label+percent+value+name',
                'textinfo': 'none'
            },
            {
                'labels': label,
                'values': IDP4,
                'type': 'pie',
                'name': 'IDP Camp 4',
                'domain': {'x': [0, .48],
                           'y': [0, .49]},
                'hoverinfo': 'label+percent+value+name',
                'textinfo': 'none'
            },
            {
                'labels': label,
                'values': IDP5,
                'type': 'pie',
                'name': 'IDP Camp 5',
                'domain': {'x': [.52, 1],
                           'y': [0, .49]},
                'hoverinfo': 'label+percent+value+name',
                'textinfo': 'none'

            }
        ],
        'layout': {'title': 'HQ Supply Value For Each Category In All IDP Camps ',
                   'showlegend': True}
    }
    plot_url = py.plot(fig, filename='SupplyValue.html')


def display_supply_weight():
    label = sorted(categoryData)
    IDP1 = []
    IDP2 = []
    IDP3 = []
    IDP4 = []
    IDP5 = []

    for i in ['IDP1', 'IDP2', 'IDP3', 'IDP4', 'IDP5']:
        if i == 'IDP1':
            IDP1.append(anaesthetics[i][0])
            IDP1.append(analgesics[i][0])
            IDP1.append(anti_allergics[i][0])
            IDP1.append(anti_infective[i][0])
            IDP1.append(anticonvulsants[i][0])
            IDP1.append(antidotes[i][0])
            IDP1.append(cardiovascular[i][0])
            IDP1.append(dermatological[i][0])
            IDP1.append(disinfectants_and_antiseptics[i][0])
            IDP1.append(diuretics[i][0])
            IDP1.append(gastrointestinal[i][0])
            IDP1.append(guidelines[i][0])
            IDP1.append(equipment_medical_device[i][0])
            IDP1.append(renewable_medical_device[i][0])
            IDP1.append(medicines[i][0])
            IDP1.append(stationary[i][0])

        elif i == 'IDP2':
            IDP2.append(anaesthetics[i][0])
            IDP2.append(analgesics[i][0])
            IDP2.append(anti_allergics[i][0])
            IDP2.append(anti_infective[i][0])
            IDP2.append(anticonvulsants[i][0])
            IDP2.append(antidotes[i][0])
            IDP2.append(cardiovascular[i][0])
            IDP2.append(dermatological[i][0])
            IDP2.append(disinfectants_and_antiseptics[i][0])
            IDP2.append(diuretics[i][0])
            IDP2.append(gastrointestinal[i][0])
            IDP2.append(guidelines[i][0])
            IDP2.append(equipment_medical_device[i][0])
            IDP2.append(renewable_medical_device[i][0])
            IDP2.append(medicines[i][0])
            IDP2.append(stationary[i][0])

        elif i == 'IDP3':
            IDP3.append(anaesthetics[i][0])
            IDP3.append(analgesics[i][0])
            IDP3.append(anti_allergics[i][0])
            IDP3.append(anti_infective[i][0])
            IDP3.append(anticonvulsants[i][0])
            IDP3.append(antidotes[i][0])
            IDP3.append(cardiovascular[i][0])
            IDP3.append(dermatological[i][0])
            IDP3.append(disinfectants_and_antiseptics[i][0])
            IDP3.append(diuretics[i][0])
            IDP3.append(gastrointestinal[i][0])
            IDP3.append(guidelines[i][0])
            IDP3.append(equipment_medical_device[i][0])
            IDP3.append(renewable_medical_device[i][0])
            IDP3.append(medicines[i][0])
            IDP3.append(stationary[i][0])

        elif i == 'IDP4':
            IDP4.append(anaesthetics[i][0])
            IDP4.append(analgesics[i][0])
            IDP4.append(anti_allergics[i][0])
            IDP4.append(anti_infective[i][0])
            IDP4.append(anticonvulsants[i][0])
            IDP4.append(antidotes[i][0])
            IDP4.append(cardiovascular[i][0])
            IDP4.append(dermatological[i][0])
            IDP4.append(disinfectants_and_antiseptics[i][0])
            IDP4.append(diuretics[i][0])
            IDP4.append(gastrointestinal[i][0])
            IDP4.append(guidelines[i][0])
            IDP4.append(equipment_medical_device[i][0])
            IDP4.append(renewable_medical_device[i][0])
            IDP4.append(medicines[i][0])
            IDP4.append(stationary[i][0])

        elif i == 'IDP5':
            IDP5.append(anaesthetics[i][0])
            IDP5.append(analgesics[i][0])
            IDP5.append(anti_allergics[i][0])
            IDP5.append(anti_infective[i][0])
            IDP5.append(anticonvulsants[i][0])
            IDP5.append(antidotes[i][0])
            IDP5.append(cardiovascular[i][0])
            IDP5.append(dermatological[i][0])
            IDP5.append(disinfectants_and_antiseptics[i][0])
            IDP5.append(diuretics[i][0])
            IDP5.append(gastrointestinal[i][0])
            IDP5.append(guidelines[i][0])
            IDP5.append(equipment_medical_device[i][0])
            IDP5.append(renewable_medical_device[i][0])
            IDP5.append(medicines[i][0])
            IDP5.append(stationary[i][0])

    fig = {
        'data': [
            {
                'labels': label,
                'values': IDP1,
                'type': 'pie',
                'name': 'IDP Camp 1',
                'domain': {'x': [0, .48],
                           'y': [.51, 1]},
                'hoverinfo': 'label+percent+value+name',
                'textinfo': 'none'
            },
            {
                'labels': label,
                'values': IDP2,
                'type': 'pie',
                'name': 'IDP Camp 2',
                'domain': {'x': [0.3, 0.7],
                           'y': [0.51, 1]},
                'hoverinfo': 'label+percent+value+name',
                'textinfo': 'none'
            },
            {
                'labels': label,
                'values': IDP3,
                'type': 'pie',
                'name': 'IDP Camp 3',
                'domain': {'x': [.52, 1],
                           'y': [.51, 1]},
                'hoverinfo': 'label+percent+value+name',
                'textinfo': 'none'
            },
            {
                'labels': label,
                'values': IDP4,
                'type': 'pie',
                'name': 'IDP Camp 4',
                'domain': {'x': [0, .48],
                           'y': [0, .49]},
                'hoverinfo': 'label+percent+value+name',
                'textinfo': 'none'
            },
            {
                'labels': label,
                'values': IDP5,
                'type': 'pie',
                'name': 'IDP Camp 5',
                'domain': {'x': [.52, 1],
                           'y': [0, .49]},
                'hoverinfo': 'label+percent+value+name',
                'textinfo': 'none'

            }
        ],
        'layout': {'title': 'HQ Demand For Each Category In All IDP Camps ',
                   'showlegend': True}
    }
    plot_url = py.plot(fig, filename='SupplyDemand.html')


def display_hq_demand():
    weight = []
    x = sorted(categoryData)

    for index in x:
        weight.append(categoryData[index][0])

    trace0 = go.Bar(
        x=x,
        y=weight,
        name='Demand'
    )
    data = [trace0]
    layout = go.Layout(
        title='Supplies Demand For Each Category From All IDP Camps In HQ',
        barmode='group',
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
            ) for xi, yi in zip(x, weight)]
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='HQDemandData.html')

def display_hq_supply():
    max_weight = []
    x = sorted(categoryData)

    for index in x:
        max_weight.append(categoryData[index][2])

    trace0 = go.Bar(
        x=x,
        y=max_weight,
        name='Supply'
    )
    data = [trace0]
    layout = go.Layout(
        title='Amount of Supplies For Each Category In HQ',
        barmode='group',
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
            ) for xi, yi in zip(x, max_weight)]
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='HQSupplyData.html')

generate_category_data()
import_supply()
import_category()
display_category()
display_total_value()
display_supply_value()
display_supply_weight()
display_hq_supply()
display_hq_demand()
