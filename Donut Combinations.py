from itertools import combinations_with_replacement


def rSubset(array, r):
    # return list of all subsets of length r
    # to deal with duplicate subsets use
    # set(list)
    different_combo = list(combinations_with_replacement(array, r))
    return different_combo


if __name__ == "__main__":

    variety_of_donuts = ["glazed", "chocolate", "sprinkled", "yeast", "caked", "sugar", "powder", "crumb",
           "fruit filled", "cream filled", "jelly",
           "sour cream", "boston cream", "apple fritter", "cinnamon twist", "crullers",
           "cronuts", "spudnuts", "cocunut", "long john", "mapple bar"]

    #variety_of_donuts = ["glazed", "chocolate", "sprinkled"]

    number_of_donuts_selected = 12

    number_of_combos = len(rSubset(variety_of_donuts, number_of_donuts_selected))
    combos = rSubset(variety_of_donuts, number_of_donuts_selected)

    print("The number of different combinations one could choose is:", number_of_combos)

    print("Printing out the different combinations.")
    index = 0
    for combo in combos:
        index += 1
        print("Index:", index, end=' ')
        print(combo)
