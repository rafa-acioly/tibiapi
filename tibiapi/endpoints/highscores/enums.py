from enum import Enum, IntEnum, auto


class HighScoreCategory(str, Enum):
    ACHIEVEMENTE = "ACHIEVEMENTE"
    AXE_FIGHTING = "AXE_FIGHTING"
    BOSS_POINTS = "BOSS_POINTS"
    CHARM_POINTS = "CHARM_POINTS"
    CLUB_FIGHTING = "CLUB_FIGHTING"
    DISTANCE_FIGHTING = "DISTANCE_FIGHTING"
    DROME_SCORE = "DROME_SCORE"
    EXPERIENCE_POINTS = "EXPERIENCE_POINTS"
    FISHING = "FISHING"
    FIST_FIGHTING = "FIST_FIGHTING"
    GOSHNARS_TAINT = "GOSHNARS_TAINT"
    LOYALTY_POINTS = "LOYALTY_POINTS"
    MAGIC_LEVEL = "MAGIC_LEVEL"
    SHIELDING = "SHIELDING"
    SWORD_FIGHTING = "SWORD_FIGHTING"

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
    NONE = "NONE"
    KNIGHTS = "KNIGHTS"
    PALADINS = "PALADINS"
    SORCERERS = "SORCERERS"
    DRUIDS = "DRUIDS"

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
                return i


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
