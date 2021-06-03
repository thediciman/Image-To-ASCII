import cv2

def build_character_map_by_brightness():

    def add_character(character, interval, character_map):
        left, right = interval
        for brightness_value in range(left, right):
            character_map[brightness_value] = character

    character_map = {}

    add_character('@', (0, 40), character_map)
    add_character('#', (40, 80), character_map)
    add_character('O', (80, 120), character_map)
    add_character('+', (120, 160), character_map)
    add_character(':', (160, 200), character_map)
    add_character('.', (200, 240), character_map)
    add_character(' ', (240, 256), character_map)

    return character_map

if __name__ == '__main__':
    image_filename = input("Path to image file: ")

    image = cv2.imread(image_filename)

    if image is None:
        print("Invalid image path.")
        exit()

    pixels_per_character = int(input("Number of pixels per character: "))
    
    if pixels_per_character < 1:
        print("The number of pixels per character should be positive.")
        exit()

    percentage_scale = 100 // pixels_per_character

    height = len(image)
    width = len(image[0])

    new_dimensions = (width * percentage_scale // 100, height * percentage_scale // 100 // 2)

    image = cv2.resize(image, new_dimensions)

    output_filename = input("Path to output file: ")

    character_map = build_character_map_by_brightness()

    with open(output_filename, "w") as output_file:
        for row in image:
            for pixel in row:
                output_file.write(character_map[sum(pixel) // 3])
            output_file.write('\n')