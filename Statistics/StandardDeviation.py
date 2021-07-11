import statistics as stats


def standard_deviation(std_list):
    try:
        c = stats.stdev(std_list)
        return c
    except (IndexError) or (ValueError):
        # Index Error : throws exception if the list is empty
        # Value Error : throws exception if the list contains string values
        return None