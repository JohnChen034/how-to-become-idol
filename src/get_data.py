import json

# Function to generate ordered positions for circles in a column-like layout
def generate_ordered_positions(num_objects, start_x, start_y, gap, max_per_column):
    positions = []
    for i in range(num_objects):
        x = start_x + (i // max_per_column) * gap
        y = start_y + (i % max_per_column) * gap
        positions.append((x, y))
    return positions

# Configuration for the positions
num_objects = 5000
start_x = 10  # starting x position
start_y = 10  # starting y position
gap = 10      # gap between circles
max_per_column = 50  # max number of circles per column

# Generate the positions
ordered_positions = generate_ordered_positions(num_objects, start_x, start_y, gap, max_per_column)

# Create the list of people with the ordered positions
people = [
    {
        "id": i + 1,
        "x": position[0],
        "y": position[1],
        "radius": 5,  # fixed radius for each circle
        "color": "#0000ff"  # blue color for each circle
    }
    for i, position in enumerate(ordered_positions)
]

# Save the generated data to a JSON file
output_path = '../static/people.json'
with open(output_path, 'w') as f:
    json.dump(people, f)

output_path
