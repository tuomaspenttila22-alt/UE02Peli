import os
images = {}
    
def load_pngs(folder_path, pygame):
    
    #Loads all .png files in a folder into a dictionary.
    global images
    images = {}

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".png"):
            key = os.path.splitext(filename)[0]
            full_path = os.path.join(folder_path, filename)

            image = pygame.image.load(full_path).convert_alpha()
            images[key] = image

    print(f"Loaded {len(images)} images.")
    print(images)