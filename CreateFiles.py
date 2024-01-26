import os
import uuid


# from Builtindata import class_uuid, class_progression


def create_uuids(main_class, subclasses=None):
    uuid_list = {
        "mod_uuid": uuid.uuid4(),
        "main_class_uuid": uuid.uuid4(),
        "main_class_name": os.urandom(19).hex()[:37],
        "main_class_description": os.urandom(19).hex()[:37],
        "main_class_progression": uuid.uuid4(),
    }

    if subclasses:
        for subclass in subclasses:
            subclass_formatted = subclass.replace(" ", "_")
            uuid_list[f"{subclass_formatted + '_uuid'}"] = uuid.uuid4()
            uuid_list[f"{subclass_formatted + '_name'}"] = os.urandom(19).hex()[:37]
            uuid_list[f"{subclass_formatted + '_description'}"] = os.urandom(19).hex()[
                :37
            ]
            uuid_list[f"{subclass_formatted + '_progression'}"] = uuid.uuid4()
            uuid_list[f"{subclass_formatted + '_level_one'}"] = uuid.uuid4()

    return uuid_list


def generate_localization(main_class, uuids, subclasses=None):
    localization_content = f"""<?xml version = "1.0" encoding = "utf-8"?>
        <contentList>
            <content contentuid = "{uuids['main_class_name']}" version = "1" >{main_class.title()}</content>
            <content contentuid = "{uuids['main_class_description']}" version = "1" >{main_class.title()} Description</content>"""

    if subclasses:
        for subclass in subclasses:
            subclass_formatted = subclass.replace(" ", "_")
            localization_content += f"""
                <content contentuid = "{uuids[subclass_formatted + '_name']}" version = "1" >{subclass.title()}</content>
                <content contentuid = "{uuids[subclass_formatted + '_description']}" version = "1" >{subclass.title()} Description</content>"""

    localization_content += """
            </contentList>"""

    localization_file = os.path.join(
        os.path.abspath(
            f"{main_class.title().replace(' ', '')}\\Localization\\English"
        ),
        main_class.title().replace(" ", "") + ".xml",
    )
    with open(localization_file, "w") as f:
        f.write(localization_content)


def generate_class_descriptions(main_class, uuids, subclasses=None):
    description_content = f"""<?xml version="1.0" encoding="UTF-8"?>
        <save>
            <version major="4" minor="0" revision="7" build="406"/>
                <region id="ClassDescriptions">
                    <node id="root">
                        <children>
                            <node id="ClassDescription">
                                <attribute id="BaseHp" type="int32" value="8"/> Hit Die
                                <attribute id="CanLearnSpells" type="bool" value="true"/>
                                <attribute id="CharacterCreationPose" type="guid" value="0f07ec6e-4ef0-434e-9a51-1353260ccff8"/>
                                <attribute id="DisplayName" type="TranslatedString" handle="{uuids['main_class_name']}" version="1"/>
                                <attribute id="Description" type="TranslatedString" handle="{uuids['main_class_description']}" version="1"/>
                                <attribute id="ClassEquipment" type="FixedString" value="{'EQP_CC_' + main_class.title().replace(' ', '')}"/>
                                <attribute id="ClassHotbarColumns" type="int32" value="5"/>                
                                <attribute id="ItemsHotbarColumns" type="int32" value="2"/>
                                <attribute id="CommonHotbarColumns" type="int32" value="9"/>
                                <attribute id="HpPerLevel" type="int32" value="5"/> Half Hit Die + 1
                                <attribute id="LearningStrategy" type="uint8" value="1"/>
                                <attribute id="MustPrepareSpells" type="bool" value="true"/> Have this as false if you don't need to prepare them
                                <attribute id="Name" type="FixedString" value="{main_class.title().replace(' ', '')}"/>
                                <attribute id="PrimaryAbility" type="uint8" value="4"/> 4 is for int. order goes from Str, Dex, Con, Int, Wis, and Cha.
                                <attribute id="ProgressionTableUUID" type="guid" value="{uuids['main_class_progression']}"/>
                                <attribute id="SoundClassType" type="FixedString" value="Wizard"/> Pick a class that your class would be the most similar to
                                <attribute id="SpellCastingAbility" type="uint8" value="4"/> 4 is for int. order goes from Str, Dex, Con, Int, Wis, and Cha.
                                <attribute id="SpellList" type="guid" value="beb9389e-24f8-49b0-86a5-e8d08b6fdc2e"/> This is used for learning spells from scrolls
                                <attribute id="UUID" type="guid" value="{uuids['main_class_uuid']}"/>
                                <children>
                                    <node id="Tags">
                                        <attribute id="Object" type="guid" value="1ae7017c-4884-4a43-bc4a-742fa0d201c0"/> Dialogue tag Fighter (You can have multiple dialogue tags)
                                    </node>
                                </children>
                            </node>"""
    if subclasses:
        for subclass in subclasses:
            subclass_formatted = subclass.replace(" ", "_")
            description_content += f"""
                <node id="ClassDescription">
                    <attribute id="CharacterCreationPose" type="guid" value="0f07ec6e-4ef0-434e-9a51-1353260ccff8"/>
                    <attribute id="Description" type="TranslatedString" handle="{uuids[subclass_formatted + '_description']}" version="9"/>
                    <attribute id="DisplayName" type="TranslatedString" handle="{uuids[subclass_formatted + '_name']}" version="1"/>
                    <attribute id="LearningStrategy" type="uint8" value="1"/>
                    <attribute id="Name" type="FixedString" value="{subclass.title().replace(' ', '')}"/>
                    <attribute id="ParentGuid" type="guid" value="{uuids['main_class_uuid']}"/>
                    <attribute id="PrimaryAbility" type="uint8" value="1"/>
                    <attribute id="ProgressionTableUUID" type="guid" value="{uuids[subclass_formatted + '_progression']}"/>
                    <attribute id="SoundClassType" type="FixedString" value="Fighter"/> Pick a class that your class would be the most similar to
                    <attribute id="SpellCastingAbility" type="uint8" value="6"/>
                    <attribute id="UUID" type="guid" value="{uuids[subclass_formatted + '_uuid']}"/>
                </node>"""

    description_content += """
                    </children>
                </node>
            </region>
        </save>"""

    description_file = os.path.join(
        os.path.abspath(
            f"{main_class.title().replace(' ', '')}\\Public\\{main_class.title().replace(' ', '')}\\ClassDescriptions"
        ),
        "ClassDescriptions.lsx",
    )

    with open(description_file, "w") as f:
        f.write(description_content)


def generate_progression(
    main_class, uuids, allowmulticlass, subclasses=None, subclasslevel=None
):
    progression_content = """<?xml version="1.0" encoding="UTF-8"?>
    <save>
        <version major="4" minor="0" revision="6" build="5"/>
        <region id="Progressions">
            <node id="root">
                <children>"""

    if allowmulticlass:
        progression_content += f"""
                    <node id="Progression">
                    <attribute id="AllowImprovement" type="bool" value="false"/>
                    <attribute id="Boosts" type="LSString" value="ProficiencyBonus(Skill,SleightOfHand);Proficiency(LightArmor);Proficiency(MediumArmor);Proficiency(Shields);Proficiency(Firearms);Proficiency(Slings)"/>
                    <attribute id="IsMulticlass" type="bool" value="true"/>
                    <attribute id="Level" type="uint8" value="1"/>
                    <attribute id="Name" type="LSString" value="{main_class.title().replace(' ', '')}"/>
                    <attribute id="PassivesAdded" type="LSString" value="UnlockedSpellSlotLevel1;Passive_ArtificerExtraSlots;MagicalTinkering;ExperimentalAlchemy;AuraOfArtificer_Technical;AuraOfArtificer_Passive_Technical_Self;AuraOfArtificer_Passive_Technical_Self_2;AuraOfArtificer_Passive_Technical_Self_3;AuraOfArtificer_Passive_Technical_Self_4;AuraOfArtificer_Passive_Technical_Self_5"/>
                    <attribute id="ProgressionType" type="uint8" value="0"/> 
                    <attribute id="Selectors" type="LSString" value="AddSpells(c9808849-c41b-444a-83aa-9748e03e9e16,MagicalTinkering,,,AlwaysPrepared);SelectSpells(b9808849-c41b-444a-83aa-9748e03e9e16,2,0,,,,AlwaysPrepared);AddSpells(ef3aa11f-cc98-412f-a85e-7fae4561a4d4)"/>
                    <attribute id="TableUUID" type="guid" value="{uuids['main_class_progression']}"/>
                    <attribute id="UUID" type="guid" value="{uuid.uuid4()}"/>
                </node>"""

    for level in range(1, 13):
        progression_content += f"""        
            <node id="Progression">
                <attribute id="AllowImprovement" type="bool" value="false"/>
                <attribute id="Boosts" type="LSString" value="ActionResource(ExampleResource,5,0);ProficiencyBonus(SavingThrow,Intelligence);ProficiencyBonus(SavingThrow,Constitution);Proficiency(SimpleWeapons);Proficiency(MartialWeapons);Proficiency(LightArmor)"/> Adds resource, proficiency, etc.
                <attribute id="Level" type="uint8" value="{level}"/>
                <attribute id="Name" type="LSString" value="{main_class.title().replace(' ', '')}"/>
                <attribute id="PassivesAdded" type="LSString" value="Passive1"/> most class features usually can be done with passives
                <attribute id="PassivesRemoved" type="LSString" value=""/>
                <attribute id="ProgressionType" type="uint8" value="0"/>
                <attribute id="Selectors" type="LSString" value="SelectAbilityBonus(b9149c8e-52c8-46e5-9cb6-fc39301c05fe,AbilityBonus,2,1);SelectPassives(PASSIVE_LIST_UUID,1);SelectSkills(SKILL_LIST_UUID,3);SelectSpells(SPELL_LIST_UUID,3,0,,,,AlwaysPrepared);SelectSpells(SPELL_LIST_UUID,4,0)"/> this is where you can have your class select spells from spell list, passive from passive list, and skill from skill list. Select ability bonus let you get the +2/+1 at CC
                <attribute id="TableUUID" type="guid" value="{uuids['main_class_progression']}"/>
                <attribute id="UUID" type="guid" value="{uuid.uuid4()}"/>"""

        if level == subclasslevel:
            progression_content += """
            <children>
                <node id="SubClasses">
                    <children>"""
            for subclass in subclasses:
                subclass_formatted = subclass.replace(" ", "_")
                progression_content += f"""
                    <node id="SubClass">
                        <attribute id="Object" type="guid" value="{uuids[subclass_formatted + '_uuid']}"/>
                    </node>"""
            progression_content += """
                        </children>
                    </node>
                </children>"""
            for subclass in subclasses:
                subclass_formatted = subclass.replace(" ", "_")
                progression_content += f"""
                    <node id="Progression">
                        <attribute id="Level" type="uint8" value="1"/>
                        <attribute id="Name" type="LSString" value="{subclass.title().replace(' ', '')}"/>
                        <attribute id="ProgressionType" type="uint8" value="1"/> 
                        <attribute id="PassivesAdded" type="LSString" value=""/>
                        <attribute id="TableUUID" type="guid" value="{uuids[subclass_formatted + '_uuid']}"/>
                        <attribute id="UUID" type="guid" value="{uuids[subclass_formatted + '_progression']}"/>
                    </node>"""
        progression_content += """
        </node>"""

    progression_content += """
                </children>
            </node>
        </region>
    </save>"""

    progression_file = os.path.join(
        os.path.abspath(
            f"{main_class.title().replace(' ', '')}\\Public\\{main_class.title().replace(' ', '')}\\Progressions"
        ),
        "Progressions.lsx",
    )

    with open(progression_file, "w") as f:
        f.write(progression_content)


def generate_meta(main_class, uuids):
    classname_cleaned = main_class.title().replace(" ", "")
    meta_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<save>
    <version major="4" minor="0" revision="6" build="5" />
    <region id="Config">
        <node id="root">
            <children>
                <node id="Dependencies"/>
                <node id="ModuleInfo">
                    <attribute id="Author" type="LSWString" value="Example"/> Your name here
                    <attribute id="CharacterCreationLevelName" type="FixedString" value=""/>
                    <attribute id="Description" type="LSWString" value="Example"/> Description of your mod which will show up in the Mod Manager, dont need to be too detailed
                    <attribute id="Folder" type="LSWString" value="{classname_cleaned}"/>
                    <attribute id="GMTemplate" type="FixedString" value=""/>
                    <attribute id="LobbyLevelName" type="FixedString" value=""/>
                    <attribute id="MD5" type="LSWString" value=""/>
                    <attribute id="MainMenuBackgroundVideo" type="FixedString" value=""/>
                    <attribute id="MenuLevelName" type="FixedString" value=""/>
                    <attribute id="Name" type="FixedString" value="{main_class.title()}"/>
                    <attribute id="NumPlayers" type="uint8" value="4"/>
                    <attribute id="PhotoBooth" type="FixedString" value=""/>
                    <attribute id="StartupLevelName" type="FixedString" value=""/>
                    <attribute id="Tags" type="LSWString" value=""/>
                    <attribute id="Type" type="FixedString" value="Add-on"/>
                    <attribute id="UUID" type="FixedString" value="{uuids['mod_uuid']}"/>
                    <attribute id="Version64" type="int64" value="36028816346316888"/>
                    <children>
                        <node id="PublishVersion">
                            <attribute id="Version64" type="int64" value="1"/> 
                        </node>
                        <node id="Scripts"/>
                            <node id="TargetModes">
                                <children>
                                    <node id="Target">
                                        <attribute id="Object" type="FixedString" value="Story"/>
                                    </node>
                                </children>
                            </node>
                    </children>
                </node>
            </children>
        </node>
    </region>
</save>"""

    meta_file = os.path.join(
        os.path.abspath(f"{classname_cleaned}\\Mods\\{classname_cleaned}"),
        "meta.lsx",
    )

    with open(meta_file, "w") as f:
        f.write(meta_content)


def generate_ability_distribution(main_class, uuids):
    ability_distribution_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<save>
    <version major="4" minor="0" revision="0" build="60"/>
    <region id="AbilityDistributionPresets">
        <node id="root">
            <children>
                <node id="AbilityDistributionPreset">
                    <attribute id="ClassUUID" type="guid" value="{uuids['main_class_uuid']}"/>
                    <attribute id="Charisma" type="int32" value="8"/>
                    <attribute id="Constitution" type="int32" value="8"/>
                    <attribute id="Dexterity" type="int32" value="8"/>
                    <attribute id="Intelligence" type="int32" value="8"/>
                    <attribute id="Strength" type="int32" value="8"/>
                    <attribute id="Wisdom" type="int32" value="8"/>
                    <attribute id="UUID" type="guid" value="{uuid.uuid4()}"/>
                </node>
            </children>
        </node>
    </region>
</save>"""

    ability_distribution_file = os.path.join(
        os.path.abspath(
            f"{main_class.title().replace(' ', '')}\\Public\\{main_class.title().replace(' ', '')}\\CharacterCreationPresets"
        ),
        "AbilityDistributionPresets.lsx",
    )

    with open(ability_distribution_file, "w") as f:
        f.write(ability_distribution_content)


def generate_lists_and_equipment(main_class):
    lists = [
        "PassiveLists.lsx",
        "SkillLists.lsx",
        "SpellLists.lsx",
    ]

    for list in lists:
        list_file = os.path.join(
            os.path.abspath(
                f"{main_class.title().replace(' ', '')}\\Public\\{main_class.title().replace(' ', '')}\\Lists"
            ),
            list,
        )

        with open(list_file, "w") as f:
            f.write(
                f"""<?xml version="1.0" encoding="UTF-8"?>
<save>
    <version major="4" minor="0" revision="4" build="206"/>
    <region id="{list[:-4]}">
        <node id="root">
            <children>
                <node id="{list[:-5]}">
                    <attribute id="{list[:-9] + 's'}" type="LSString" value=""/> a list of {list[:-9] + 's'} separated with a comma
                    <attribute id="UUID" type="guid" value="{uuid.uuid4()}"/>
                </node>
            </children>
        </node>
    </region>
</save>"""
            )

    list_file = os.path.join(
        os.path.abspath(
            f"{main_class.title().replace(' ', '')}\\Public\\{main_class.title().replace(' ', '')}\\Stats\\Generated"
        ),
        "Equipment.txt",
    )

    with open(list_file, "w") as f:
        f.write(
            f'''new equipment "{'EQP_CC_' + main_class.title().replace(' ', '')}"
add initialweaponset "Melee"
add equipmentgroup
add equipment entry "WPN_Longsword"
add equipmentgroup
add equipment entry "WPN_Shortbow"
add equipmentgroup
add equipment entry "ARM_Boots_Leather"
add equipmentgroup
add equipment entry "OBJ_Potion_Healing"
add equipmentgroup
add equipment entry "OBJ_Potion_Healing"
add equipmentgroup
add equipment entry "ARM_ScaleMail_Body"
add equipmentgroup
add equipment entry "OBJ_Scroll_Revivify"
add equipmentgroup
add equipment entry "OBJ_Keychain"
add equipmentgroup
add equipment entry "OBJ_Bag_AlchemyPouch"
add equipmentgroup
add equipment entry "ARM_Camp_Body"
add equipmentgroup
add equipment entry "ARM_Camp_Shoes"
add equipmentgroup
add equipment entry "OBJ_Backpack_CampSupplies"'''
        )


def create_files(
    main_class,
    allowmulticlass,
    subclasses=None,
    subclasslevel=None,
):
    uuids = create_uuids(main_class, subclasses)
    generate_localization(main_class, uuids, subclasses)
    generate_meta(main_class, uuids)
    generate_class_descriptions(main_class, uuids, subclasses)
    generate_progression(main_class, uuids, allowmulticlass, subclasses, subclasslevel)
    generate_ability_distribution(main_class, uuids)
    generate_lists_and_equipment(main_class)
