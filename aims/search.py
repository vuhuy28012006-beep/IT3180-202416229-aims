def search_by_title(items, title):
    result = []

    for dvd in items:
        if title.casefold() in dvd.title.casefold():
            result.append(dvd)

    return result
