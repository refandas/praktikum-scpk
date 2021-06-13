import pandas as pd

data = pd.DataFrame([
    {
        'name': 'Laptop A',
        'clockspeed': 2.6,
        'core_processor': 2,
        'ram': 4,
        'storage': 256,
        'price': 4199000
    },
    {
        'name': 'Laptop B',
        'clockspeed': 3.8,
        'core_processor': 4,
        'ram': 8,
        'storage': 256,
        'price': 8799000
    },
    {
        'name': 'Laptop C',
        'clockspeed': 4.0,
        'core_processor': 8,
        'ram': 8,
        'storage': 512,
        'price': 14999000
    },
    {
        'name': 'Laptop D',
        'clockspeed': 2.8,
        'core_processor': 2,
        'ram': 4,
        'storage': 256,
        'price': 4849000
    },
    {
        'name': 'Laptop E',
        'clockspeed': 4.2,
        'core_processor': 4,
        'ram': 8,
        'storage': 512,
        'price': 11499000
    },
    {
        'name': 'Laptop F',
        'clockspeed': 3.7,
        'core_processor': 4,
        'ram': 8,
        'storage': 512,
        'price': 7500000
    }
])

data_converted = pd.DataFrame([
    {
        'name': 'Laptop A',
        'clockspeed': 2,
        'core_processor': 1,
        'ram': 1,
        'storage': 1,
        'price': 1,
    },
    {
        'name': 'Laptop B',
        'clockspeed': 3,
        'core_processor': 2,
        'ram': 2,
        'storage': 1,
        'price': 2,
    },
    {
        'name': 'Laptop C',
        'clockspeed': 4,
        'core_processor': 4,
        'ram': 2,
        'storage': 2,
        'price': 3,
    },
    {
        'name': 'Laptop D',
        'clockspeed': 2,
        'core_processor': 1,
        'ram': 1,
        'storage': 1,
        'price': 1,
    },
    {
        'name': 'Laptop E',
        'clockspeed': 4,
        'core_processor': 2,
        'ram': 2,
        'storage': 2,
        'price': 3,
    },
    {
        'name': 'Laptop F',
        'clockspeed': 3,
        'core_processor': 2,
        'ram': 2,
        'storage': 2,
        'price': 2,
    }
])

decision_matrix = pd.DataFrame([
    [2, 1, 1, 1, 1],
    [3, 2, 2, 1, 2],
    [4, 4, 2, 2, 3],
    [2, 1, 1, 1, 1],
    [4, 2, 2, 2, 3],
    [3, 2, 2, 2, 2]
])