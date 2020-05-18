import pandas as pd


# AU=王长峰 AND FU=71271031

def get_data():
    data_list = pd.read_excel(r"科学基金.xls",

                              encoding='utf8')

    leaders = data_list.leader.values.tolist()

    codes = data_list.code.tolist()

    results = []

    for leader, code in zip(leaders, codes):
        result = "AU={} AND FU={}".format(leader, code)

        results.append(result)

    return results

# results = get_data()

# print(results)
