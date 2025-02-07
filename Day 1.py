def load_locations(file_path):
    with open(file_path, "r") as fileref:
        locations_1, locations_2 = zip(*[map(int, line.strip().split()) for line in fileref])
    return sorted(locations_1), sorted(locations_2)

def calculate_total_distance(locations_1, locations_2):
    return sum(abs(locations_1[i] - locations_2[i]) for i in range(len(locations_1)))

def calculate_similarity_score(locations_1, locations_2):
    return sum(loc1 * sum(1 for loc2 in locations_2 if loc2 == loc1) for loc1 in locations_1)

def main():
    locations_1, locations_2 = load_locations("Day 1 Input.txt")
    total_distance = calculate_total_distance(locations_1, locations_2)
    similarity_score = calculate_similarity_score(locations_1, locations_2)
    print(f"Total distance: {total_distance}")
    print(f"Similarity score: {similarity_score}")    

if __name__ == "__main__":
    main()