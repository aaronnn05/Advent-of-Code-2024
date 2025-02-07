class location:
    def __init__(self, ID):
        self.ID = int(ID)

def init_locations(input_file):
    locations_1 = []
    locations_2 = []
    with open(input_file, "r") as fileref:
        for line in fileref:
            location_1, location_2 = line.strip().split()
            locations_1.append(location(location_1))
            locations_2.append(location(location_2))

    locations_1.sort(key = lambda location: location.ID)
    locations_2.sort(key = lambda location: location.ID)

    return locations_1, locations_2

def calculate_total_distance(locations_1, locations_2):
    total_distance = 0
    for num in range(len(locations_1)):
        pair_distance = abs(locations_1[num].ID - locations_2[num].ID)
        total_distance += pair_distance
    
    return total_distance

def calculate_similarity_score(locations_1, locations_2):
    similarity_score = 0
    for location_1 in locations_1:
        similarity_score += location_1.ID * \
            sum(1 for location_2 in locations_2 if location_2.ID == location_1.ID)

    return similarity_score

def main():
    locations_1, locations_2 = init_locations("Day 1 Input.txt")
    total_distance = calculate_total_distance(locations_1, locations_2)
    similarity_score = calculate_similarity_score(locations_1, locations_2)
    print(f"Total distance: {total_distance}")
    print(f"Similarity score: {similarity_score}")    

if __name__ == "__main__":
    main()