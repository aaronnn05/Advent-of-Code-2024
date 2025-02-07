class location:
    def __init__(self, ID):
        self.ID = int(ID)

def init_locations(input_file):
    locations_1 = []
    locations_2 = []
    with open("r", input_file) as fileref:
        for line in fileref:
            location_1, location_2 = line.strip().split()
            locations_1.append(location(location_1))
            locations_2.append(location(location_2))

    locations_1.sort(key = lambda location: location.ID)
    locations_2.sort(key = lambda location: location.ID)

    return locations_1, locations_2

