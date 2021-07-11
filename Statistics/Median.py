def median(median_list):
    try:
        median_list.sort()
        mid = len(median_list) // 2
        res = (median_list[mid] + median_list[~mid]) / 2
        return res
    except (IndexError) or (ValueError):
        # Index Error : throws exception if the list is empty
        # Value Error : throws exception if the list contains string values
        return None