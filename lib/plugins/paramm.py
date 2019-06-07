from linker import *


"""

This module find and check posible parameter from site

"""

patterns = [
    {"start_with": "name=", "end_with": '"', "start_offset": 1, "end_offset": -1}
]


def param_miner(url):
    param_list = []
    get_example = requests.get(url=url).text
    for pattern in patterns:
        start_index = get_example.find(pattern["start_with"])
        end_index = -1
        while start_index != -1:
            offset_for_search = (
                start_index + len(pattern["start_with"]) + pattern["start_offset"]
            )
            end_index = get_example.find(pattern["end_with"], offset_for_search)
            param_list.append(
                get_example[
                    start_index
                    + len(pattern["start_with"])
                    + pattern["start_offset"] : end_index
                ]
            )
            start_index = get_example.find(pattern["start_with"], end_index)
    return [str(x) for x in param_list]


def diff_check(example, current):
    pass


def get_clear(url, type="get"):
    pass


def check_param(url, param_list):
    pass


def paramm(endpoint, timeout=30):
    url = helpers.urlify(endpoint)["URL_FILE"]
    result = param_miner(url)
    # print(url)
    return {"posible_name": result}
