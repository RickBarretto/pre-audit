def flatten_list(arr: list):
    """Returns a flatten list from a nested list"""
    return [item for sub_arr in arr for item in sub_arr]
