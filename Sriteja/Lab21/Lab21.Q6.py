"""function called cell_metabolism that takes the number of glucose and oxy-
gen molcules, that contains an inner function energy_output() to calculate ATP yield
(assume 1 glucose+6 oxygen gives 38 ATP) and the function returns the total ATP
produced"""

def cell_metabolism(glucose, oxygen):
    def energy_output():
        reaction = min(glucose, oxygen // 6)
        return reaction * 38

    return energy_output()
print("Total ATP:",cell_metabolism(10,40))
