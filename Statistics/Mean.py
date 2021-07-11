def mean(mean_list):
    try:
        c = sum(mean_list) / len(mean_list)
        return c
    except (IndexError) or (ValueError):
        # Index Error : throws exception if the list is empty
        # Value Error : throws exception if the list contains string values
        return None

