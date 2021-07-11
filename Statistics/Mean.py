def mean(mean_list):
    try:
        c = sum(mean_list) / len(mean_list)
        return c
    except (IndexError) or (ValueError):
        return None

