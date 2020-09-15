NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

def dedup_and_title_case_names(names):
    """ Using Set to dedupe and Title() to title case"""
    return list(set(name.title() for name in names))

def sort_by_surname_desc(names):
    names = dedup_and_title_case_names(names)
    return [" ".join(x) for x in sorted([name.split() for name in names], 
                                        key=lambda x: x[1], reverse=True)]

def shortest_first_name(names):
    names = dedup_and_title_case_names(names)
    return sorted([name.split()[0] for name in names], key=len)[0]

def shortest_last_name(names):
    names = dedup_and_title_case_names(names)
    return sorted([name.split()[1] for name in names], key=len)[0]

dedup_and_title_case_names(NAMES)
sort_by_surname_desc(NAMES)
shortest_first_name(NAMES)
shortest_last_name(NAMES)
