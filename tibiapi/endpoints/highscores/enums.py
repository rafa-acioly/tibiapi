from enum import Enum, IntEnum, auto


class HighScoreCategory(str, Enum):
    ACHIEVEMENTS = "Achievements"
    AXE_FIGHTING = "Axe Fighting"
    BOSS_POINTS = "Boss Points"
    CHARM_POINTS = "Charm Points"
    CLUB_FIGHTING = "Club Fighting"
    DISTANCE_FIGHTING = "Distance Fighting"
    DROME_SCORE = "Drome Score"
    EXPERIENCE_POINTS = "Experience Points"
    FISHING = "Fishing"
    FIST_FIGHTING = "Fist Fighting"
    GOSHNARS_TAINT = "Goshnar's Taint"
    LOYALTY_POINTS = "Loyalty Points"
    MAGIC_LEVEL = "Magic Level"
    SHIELDING = "Shielding"
    SWORD_FIGHTING = "Sword Fighting"

    @classmethod
    def numericOf(cls, category_name: str) -> int | None:
        """
        Convert a category name to its numeric value. Tibia website accept
        only numbers as category, so we need to convert the category
        name to a number, the Enum is already ordered
        in the same order.
        """
        for i, category in enumerate(list(HighScoreCategory)):
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
        for i, vocation in enumerate(list(HighScoreVocation)):
            if vocation_name == vocation.value:
                # The count starts from 1, the 0 value is for "ALL"
                # None represents characters without vocation (rookers)
                return i + 1


class HighScoreWorld(str, Enum):
    ANTICA = "Antica"
    ASTERA = "Astera"
    AXERA = "Axera"
    BELOBRA = "Belobra"
    BOMBRA = "Bombra"
    BONA = "Bona"
    CALMERA = "Calmera"
    CASTELA = "Castela"
    CELEBRA = "Celebra"
    CELESTA = "Celesta"
    COLLABRA = "Collabra"
    DAMORA = "Damora"
    DESCUBRA = "Descubra"
    DIA = "Dia"
    EPOCA = "Epoca"
    ESMERA = "Esmera"
    ETEBRA = "Etebra"
    FEROBRA = "Ferobra"
    FIRMERA = "Firmera"
    FLAMERA = "Flamera"
    GENTEBRA = "Gentebra"
    GLADERA = "Gladera"
    GRAVITERA = "Gravitera"
    GUERRIBRA = "Guerribra"
    HARMONIA = "Harmonia"
    HAVERA = "Havera"
    HONBRA = "Honbra"
    IMPULSA = "Impulsa"
    INABRA = "Inabra"
    ISSOBRA = "Issobra"
    JACABRA = "Jacabra"
    JADEBRA = "Jadebra"
    JAGUNA = "Jaguna"
    KALIBRA = "Kalibra"
    KARDERA = "Kardera"
    KENDRIA = "Kendria"
    LOBERA = "Lobera"
    LUMINERA = "Luminera"
    LUTABRA = "Lutabra"
    MENERA = "Menera"
    MONZA = "Monza"
    MYKERA = "Mykera"
    NADORA = "Nadora"
    NEFERA = "Nefera"
    NEVIA = "Nevia"
    OBSCUBRA = "Obscubra"
    OCEANIS = "Oceanis"
    OMBRA = "Ombra"
    OUSABRA = "Ousabra"
    PACERA = "Pacera"
    PELORIA = "Peloria"
    PREMIA = "Premia"
    PULSERA = "Pulsera"
    QUELIBRA = "Quelibra"
    QUINTERA = "Quintera"
    RASTEIBRA = "Rasteibra"
    REFUGIA = "Refugia"
    RETALIA = "Retalia"
    RUNERA = "Runera"
    SECURA = "Secura"
    SERDEBRA = "Serdebra"
    SOLIDERA = "Solidera"
    STRALIS = "Stralis"
    SYRENA = "Syrena"
    TALERA = "Talera"
    THYRIA = "Thyria"
    TORNABRA = "Tornabra"
    ULERA = "Ulera"
    UNEBRA = "Unebra"
    USTEBRA = "Ustebra"
    UTOBRA = "Utobra"
    VANDERA = "Vandera"
    VENEBRA = "Venebra"
    VICTORIS = "Victoris"
    VITERA = "Vitera"
    VUNIRA = "Vunira"
    WADIRA = "Wadira"
    WILDERA = "Wildera"
    WINTERA = "Wintera"
    YARA = "Yara"
    YONABRA = "Yonabra"
    YOVERA = "Yovera"
    YUBRA = "Yubra"
    ZEPHYRA = "Zephyra"
    ZUNA = "Zuna"
    Zunera = "Zunera"
