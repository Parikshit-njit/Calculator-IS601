import statistics as stats


def variance(variance_list):
    try:
        c = stats.variance(variance_list)
        return c
    except (IndexError) or (ValueError):
        # Index Error : throws exception if the list is empty
        # Value Error : throws exception if the list contains string values
        return None