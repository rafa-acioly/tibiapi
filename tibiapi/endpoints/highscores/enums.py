from enum import Enum, IntEnum, auto


class HighScoreCategory(str, Enum):
    ACHIEVEMENTS = "Achievements"
    AXE_FIGHTING = "Axe Fighting"
    CHARM_POINTS = "Charm Points"
    CLUB_FIGHTING = "Club Fighting"
    DISTANCE_FIGHTING = "Distance Fighting"
    EXPERIENCE_POINTS = "Experience Points"
    FISHING = "Fishing"
    FIST_FIGHTING = "Fist Fighting"
    GOSHNARS_TAINT = "Goshnar's Taint"
    LOYALTY_POINTS = "Loyalty Points"
    MAGIC_LEVEL = "Magic Level"
    SHIELDING = "Shielding"
    DROME_SCORE = "Drome Score"
    SWORD_FIGHTING = "Sword Fighting"
    BOSS_POINTS = "Boss Points"

    @classmethod
    def numericOf(cls, category_name: str) -> int | None:
        """
        Convert a category name to its numeric value. Tibia website accept
        only numbers as category, so we need to convert the category
        name to a number, the Enum is already ordered
        in the same order.
        """
        for i, category in enumerate(list(HighScoreCategory), start=1):
            if category_name == category.value:
                return i


class HighScoreVocation(str, Enum):
    NONE = "None"
    KNIGHTS = "Knight"
    PALADINS = "Paladin"
    SORCERERS = "Sorcerer"
    DRUIDS = "Druid"

    @classmethod
    def numericOf(cls, vocation_name: str) -> int | None:
        """
        Convert a category name to its numeric value. Tibia website accept
        only numbers as category, so we need to convert the category
        name to a number, the Enum is already ordered
        in the same order.
        """
        for i, vocation in enumerate(list(HighScoreVocation), start=1):
            if vocation_name == vocation.value:
                return i
