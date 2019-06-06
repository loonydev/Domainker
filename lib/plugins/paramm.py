from linker import *


'''

This module find and check posible parameter from site

'''

patterns = ["name="]
offset = 1

def param_miner(url):
    param_list = []
    get_example = requests.get(url = url).text
    for pattern in patterns:
        start_index = get_example.find(pattern)
        end_index = -1
        while start_index!=-1:
            end_index = get_example.find('"',start_index + len(pattern)+offset)
            param_list.append(get_example[start_index+len(pattern)+offset:end_index])
            start_index = get_example.find(pattern,end_index)
    return [str(x) for x in param_list]


def paramm(endpoint,timeout=30):
    url = helpers.urlify(endpoint)['URL_FILE']
    result = param_miner(url)
    # print(url)
    return {"posible_name" : result}
