import os


def create_folders(classname):
    cwd = os.getcwd()
    class_dir = classname.title().replace(" ", "")

    folders = [
        os.path.join(cwd, class_dir),
        os.path.join("Localization", "English"),
        os.path.join("Mods", class_dir),
        os.path.join("Public", class_dir),
    ]
    public_folders = [
        "ActionResourceDefinitions",
        ["Assets", "Textures", "Icons"],
        "CharacterCreationPresets",
        "ClassDescriptions",
        ["Content", "UI", "[PAK]_UI"],
        "GUI",
        "Lists",
        "Progressions",
        ["Stats", "Generated", "Data"],
    ]

    for folder in folders:
        os.makedirs(os.path.join(folders[0], folder), exist_ok=True)
        if "Public" in folder:
            for sub_folder in public_folders:
                if isinstance(sub_folder, list):
                    os.makedirs(
                        os.path.join(os.path.join(folders[0], folder), *sub_folder),
                        exist_ok=True,
                    )
                else:
                    os.makedirs(
                        os.path.join(os.path.join(folders[0], folder), sub_folder),
                        exist_ok=True,
                    )


