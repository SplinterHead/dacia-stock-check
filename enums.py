from enum import Enum


class Model(Enum):
    # Filter: model.code=DU3
    # Multiple: model.code=DU3%2CBD1
    Bigster = "BD1"
    Duster = "DU3"
    Jogger = "RI1"
    Sandero = "BI1"
    Spring = "S1E"


class Fuel(Enum):
    # Filter: energy.group=HEV
    # Multiple: energy.group=HEV%2CMILDHYBRID
    BiFuel = "ICEBIFUELLPG"
    Electric = "ELECTRIC"
    Hybrid = "HEV"
    Mild = "MILDHYBRID"
    Petrol = "ESS"


class Gearbox(Enum):
    # Filter: transmission.group=AUTOMATIC
    # Multiple: transmission.group=AUTOMATIC%2CMANUAL
    Automatic = "AUTOMATIC"
    Manual = "MANUAL"


class Colour(Enum):
    # Filter: colorMarketing.hexaCode=000000
    # Multiple: colorMarketing.hexaCode=000000%2C008000
    Black = "000000"
    Blue = "4348E0"
    Green = "008000"
    Grey = "CFCFCF"
    Orange = "EB700C"
    Red = "FF0000"
    Sandstone = "996216"
    White = "FFFFFF"


class Extras(Enum):
    Sunroof = "Panoramic opening sunroof"
    TwoTone = "Two tone Black roof"
