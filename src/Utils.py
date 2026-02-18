import json


def get_operations_list(file: str = '') -> list[dict]:

    if len(file) == 0:
        return []

    try:
        with open(file, 'r', encoding='utf-8') as f:
            json_obj = json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    except TypeError:
        return []
    except KeyError:
        return []
    except ValueError:
        return []

    return json_obj
