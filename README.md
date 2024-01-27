# Baldur's Gate 3 - Create New Class Mod script  

This is a simple script that will create the folder and file structure for a new class mod. Optional settings for multiclass and subclasses. Generates folder structure along with basic starting template files. Names, UUID, Handles are generated to create a working class if exported as is.

## Usage  

CreateClass.py classname [--hassubclass] [--allowmulticlass] [--hassubclass] [--subclassnames SUBCLASSNAMES] [--subclasslevel SUBCLASSLEVEL]

## Arguments  

**classname (Required)** - Name of the base class in quotes. Spaces are allowed in names. No need to preface call
#### Usage
CreateClass.py "Artificer"  
CreateClass.py "Alternate Fighter"
___
 
**\--allowmulticlass (Optional)** - Toggle for if class can be used in multiclass. Default = False.
#### Usage
CreateClass.py "Artificer"  --allowmulticlass
___

**\--hassubclass (Optional)** - Toggle for if class features subclass. Default = False.
#### Usage
CreateClass.py "Artificer"  --hassubclass
___

**\--subclassnames (Required if --hassubclass)** - Names of the subclass(es) in quotes. Spaces are allowed in names. Space between each subclass. 
#### Usage
CreateClass.py "Artificer"  --hassubclass --subclassnames "Alchemist" "Armorer" "Artillerist" "Battle Smith"
___

**\--subclasslevel (Required if --hassubclass)** - Level at which main class can choose a subclass.
#### Usage
CreateClass.py "Artificer"  --hassubclass --subclassnames "Alchemist" "Armorer" "Artillerist" "Battle Smith" --subclasslevel 3
___

## Folder and File structure
- Classname  
  - Localization  
    - English  
      - Classname.xml  
  - Mods  
    - Classname  
      - meta.lsx  
  - Public  
    - Classname  
      - ActionResourceDefinitions
        - ActionResourceDefinitions.lsx 
      - Assets  
        - Textures  
          - Icons  
      - CharacterCreationPresets  
        - AbilityDistributionPresets.lsx  
      - ClassDescriptions  
        - ClassDescriptions.lsx  
      - Content  
        - UI  
          - [PAK]_UI  
      - GUI  
      - Lists  
        - PassiveLists.lsx  
        - SkillLists.lsx  
        - SpellLists.lsx  
      - Progressions  
        - Progressions.lsx  
      - Stats
        - Data  
        - Generated  
          - Equipment.txt  
