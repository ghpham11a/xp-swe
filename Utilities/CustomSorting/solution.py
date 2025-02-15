import functools

RANKS = {"2LT": 1, "1LT": 2, "CPT": 3, "MAJ": 4, "LTC": 5, "COL": 6}

class Officer:

    def __init__(self, rank):
        self.rank = rank

    def __repr__(self):
        return self.rank

def compare(x, y):
    return RANKS[x.rank] - RANKS[y.rank]

objects = [Officer("CPT"), Officer("MAJ"), Officer("2LT"), Officer("COL"), Officer("LTC"), Officer("1LT")]


sorted_objects = sorted(objects, key=functools.cmp_to_key(compare))
sorted_objects = sorted(objects, key=lambda x: RANKS[x.rank])

print(sorted_objects)

# [2LT, 1LT, CPT, MAJ, LTC, COL]