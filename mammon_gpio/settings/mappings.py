import orangepi.lite
import orangepi.lite2
import orangepi.one
import orangepi.oneplus
import orangepi.pc
import orangepi.pc2
import orangepi.pcplus
import orangepi.pi3
import orangepi.pi4
import orangepi.pi4B
import orangepi.plus2e
import orangepi.prime
import orangepi.r1
import orangepi.winplus
import orangepi.zero
import orangepi.zeroplus
import orangepi.zeroplus2
import nanopi.duo
import nanopi.m4
import nanopi.neocore2
import rockpi.s

raspberry = {
    3: 2,
    5: 3,
    7: 4,
    8: 14,
    29: 5,
    31: 6,
    26: 7,
    24: 8,
    21: 9,
    19: 10,
    23: 11,
    32: 12,
    33: 13,
    10: 15,
    36: 16,
    11: 17,
    12: 18,
    35: 19,
    38: 20,
    40: 21,
    15: 22,
    16: 23,
    18: 24,
    22: 25,
    37: 26,
}

mappers = {
    "raspberry_pi": {
        "all": raspberry
    },
    "orange_pi": {
        "lite": orangepi.lite.BOARD,
        "lite2": orangepi.lite2.BOARD,
        "one": orangepi.one.BOARD,
        "oneplus": orangepi.oneplus.BOARD,
        "pc": orangepi.pc.BOARD,
        "pc2": orangepi.pc2.BOARD,
        "pcplus": orangepi.pcplus.BOARD,
        "pi3": orangepi.pi3.BOARD,
        "pi4": orangepi.pi4.BOARD,
        "pi4B": orangepi.pi4B.BOARD,
        "plus2e": orangepi.plus2e.BOARD,
        "prime": orangepi.prime.BOARD,
        "r1": orangepi.r1.BOARD,
        "winplus": orangepi.winplus.BOARD,
        "zero": orangepi.zero.BOARD,
        "zeroplus": orangepi.zeroplus.BOARD,
        "zeroplus2": orangepi.zeroplus.BOARD
    },
    "nano_pi": {
        "duo": nanopi.duo.BOARD,
        "m4": nanopi.m4.BOARD,
        "neocore2": nanopi.neocore2.BOARD
    },
    "rock_pi": {
        "s": rockpi.s.BOARD
    }
}
