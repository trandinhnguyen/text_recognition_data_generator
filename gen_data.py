import os
from trdg.generators import GeneratorFromDict
from tqdm import tqdm

# The generators use the same arguments as the CLI, only as parameters
generator = GeneratorFromDict(
    count=50_000,
    length=10,
    allow_variable=True,
    language="vi",
    size=32,
    skewing_angle=5,
    random_skew=True,
    blur=2,
    random_blur=True,
    background_type=3,
    image_dir="trdg/images",
    distorsion_type=1,
    distorsion_orientation=2,
    text_color="#000000,#ffffff",
    path="trdg/dicts/vi.txt",
    margins=(0, 0, 0, 0),
    fit=True,
)

count = 0
for img, lbl in tqdm(generator):
    # Do something with the pillow images here.
    if img is not None:
        img_name = f"distorted_{count}.jpg"
        img.save(os.path.join("generated_datasets_v2/distorted", img_name))
        with open("generated_datasets_v2/distorted_labels.txt", "a") as f:
            f.write(f"{img_name}\t{lbl.lower()}\n")
        count += 1
