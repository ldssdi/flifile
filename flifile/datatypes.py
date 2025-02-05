from enum import Enum

import numpy as np


class Packing(Enum):
    LSB = 0
    MSB = 1
    UNKNOWN = 3


class Datatypes(Enum):
    UINT8 = (np.uint8, 8, Packing.UNKNOWN)
    UINT16 = (np.uint16, 16, Packing.UNKNOWN)
    UINT12 = (np.uint16, 12, Packing.UNKNOWN)
    UINT32 = (np.uint32, 32, Packing.UNKNOWN)
    INT8 = (np.int8, 8, Packing.UNKNOWN)
    INT16 = (np.int16, 16, Packing.UNKNOWN)
    INT32 = (np.int32, 32, Packing.UNKNOWN)
    REAL32 = (np.float32, 32, Packing.UNKNOWN)
    REAL64 = (np.float64, 64, Packing.UNKNOWN)
    BayerBG16 = (np.uint16, 16, Packing.UNKNOWN)
    BayerGB16 = (np.uint16, 16, Packing.UNKNOWN)
    BayerRG10 = (np.uint16, 16, Packing.UNKNOWN)
    BayerRG12 = (np.uint16, 16, Packing.UNKNOWN)
    BayerRG16 = (np.uint16, 16, Packing.UNKNOWN)
    Mono10 = (np.uint16, 16, Packing.UNKNOWN)
    Mono12 = (np.uint16, 16, Packing.UNKNOWN)
    Mono14 = (np.uint16, 16, Packing.UNKNOWN)
    Mono16 = (np.uint16, 16, Packing.UNKNOWN)
    Mono8 = (np.uint8, 8, Packing.UNKNOWN)
    Mono10p = (np.uint16, 10, Packing.LSB)
    Mono10pmsb = (np.uint16, 10, Packing.MSB)
    BayerBG12 = (np.uint16, 16, Packing.UNKNOWN)
    BayerBG12p = (np.uint16, 12, Packing.LSB)
    BayerBG12pmsb = (np.uint16, 12, Packing.MSB)
    BayerGB12 = (np.uint16, 16, Packing.UNKNOWN)
    BayerGB12p = (np.uint16, 12, Packing.LSB)
    BayerGB12pmsb = (np.uint16, 12, Packing.MSB)
    BayerRG12p = (np.uint16, 12, Packing.LSB)
    BayerRG12pmsb = (np.uint16, 12, Packing.MSB)
    BayerRG12Packed = (np.uint16, 12, Packing.UNKNOWN)
    Mono12p = (np.uint16, 12, Packing.LSB)
    Mono12pmsb = (np.uint16, 12, Packing.MSB)
    Mono12Packed = (np.uint16, 12, Packing.UNKNOWN)
    Mono14p = (np.uint16, 14, Packing.LSB)
    BayerBG8 = (np.uint8, 8, Packing.UNKNOWN)
    BayerGB8 = (np.uint8, 8, Packing.UNKNOWN)
    BGR8 = (np.uint8, 8, Packing.UNKNOWN)
    BGR8Packed = (np.uint8, 8, Packing.UNKNOWN)
    RGB8 = (np.uint8, 8, Packing.UNKNOWN)
    RGB8Packed = (np.uint8, 8, Packing.UNKNOWN)

    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    @property
    def nptype(self) -> np.dtype:
        return self.v1

    @property
    def bits(self) -> int:
        return self.v2

    @property
    def packing(self) -> Packing:
        return self.v3
