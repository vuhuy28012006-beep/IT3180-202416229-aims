def search_by_title(items, title):
    result = []

    for dvd in items:
        if title.lower() in dvd.title.lower():
            result.append(dvd)

    return result