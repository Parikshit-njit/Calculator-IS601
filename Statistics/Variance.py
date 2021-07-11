import statistics as stats


def variance(variance_list):
    try:
        c = stats.variance(variance_list)
        return c
    except (IndexError) or (ValueError):
        return None