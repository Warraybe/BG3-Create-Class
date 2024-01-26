import argparse

from CreateFiles import create_files
from CreateFolders import create_folders

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create a new class mod.",
    )

    parser.add_argument(
        "classname",
        help='Name for the class. i.e. "Cleric" or "Artificer". (Add quotes around classname.)',
    )

    parser.add_argument(
        "--hassubclass",
        action="store_true",
        help="Toggle for if this class features subclasses. (Default = False)",
    )

    parser.add_argument(
        "--allowmulticlass",
        action="store_true",
        help="Toggle for if this class allows multiclass. (Default = False)",
    )

    parser.add_argument(
        "--subclassnames",
        nargs="+",
        help='Name(s) for the subclass(es). i.e. "Monster Slayer" "Circle of Stars". (Add quotes around each classname. Can submit multiple with space between each.)',
    )

    parser.add_argument(
        "--subclasslevel",
        type=int,
        help="Level in which you get to choose a subclass.",
    )

    args = parser.parse_args()

    if args.hassubclass and (args.subclassnames is None or args.subclasslevel is None):
        parser.error("--hassubclass requires --subclassnames and --subclasslevel.")

    create_folders(args.classname)
    create_files(
        args.classname, args.allowmulticlass, args.subclassnames, args.subclasslevel
    )
