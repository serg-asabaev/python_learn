import pytest

from src import proccessing


def test_filter_by_state_executed(dict_list_exec):
    test_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    assert proccessing.filter_by_state(test_list) == dict_list_exec
    assert proccessing.filter_by_state(test_list, 'EXECUTED') == dict_list_exec

def test_filter_by_state_canceled(dict_list_canceled):
    test_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    assert proccessing.filter_by_state(test_list, 'CANCELED') == dict_list_canceled

@pytest.mark.parametrize('input_list, state, output_list',[([], '', []),([], 'EXECUTED', []),([], None, []), ([], 'CANCELED', [])])
def test_filter_by_state_empty(input_list, state, output_list):
    assert proccessing.filter_by_state(input_list, state) == output_list
