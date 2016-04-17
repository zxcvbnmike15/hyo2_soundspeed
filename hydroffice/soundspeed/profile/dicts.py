from __future__ import absolute_import, division, print_function, unicode_literals

from collections import OrderedDict
import logging

logger = logging.getLogger(__name__)


class Dicts(object):

    @classmethod
    def first_match(cls, dct, val):
        # print(dct, val)
        values = [key for key, value in dct.items() if value == val]
        if len(values) != 0:
            return values[0]
        else:
            raise RuntimeError("unknown value %s in dict: %s" % (val, dct))

    probe_types = OrderedDict([
        ('Unknown', 0),
        ('RTOFS', 1),
        ('WOA09', 2),
        ('WOA13', 3),
        ('SIS', 4),
        ('SVP', 5),
        ('Castaway', 6),
        ('Idronaut', 7),
        ('S2', 8),
        ('SBE', 9),
        ('XBT', 10),
        ('Deep Blue', 11),
        ('T-10', 12),
        ('T-11 (Fine Structure)', 13),
        ('T-4', 14),
        ('T-5', 15),
        ('T-5/20', 16),
        ('T-7', 17),
        ('XSV-01', 18),
        ('XSV-02', 19),
        ('XCTD-1', 20),
        ('XCTD-2', 21),
        ('MONITOR SVP 500', 22),
        ('MIDAS SVP 6000', 23),
        ('MIDAS SVX2 1000', 24),
        ('MIDAS SVX2 3000', 25),
        ('MiniSVP', 26),
        ('MVP', 27),
        ('Sonardyne', 28),
        ('Elac', 29),
    ])

    sensor_types = OrderedDict([
        ('Unknown', 0),
        ('Synthetic', 1),
        ('SVP', 2),
        ('CTD', 3),
        ('XBT', 4),
        ('XSV', 5),
        ('XCTD', 6),
        ('SVPT', 7),
        ('MVP', 8),
    ])

    ssp_directions = OrderedDict([
        ('up', 0),
        ('down', 1)
    ])

    flags = OrderedDict([
        ('valid', 0),
        ('direction', 1),
        ('user', 2),
        ('thin', 3),
    ])

    sources = OrderedDict([
        ('raw', 0),
        ('user', 1),
        ('tss', 2),
        ('woa09_ext', 3),
        ('woa13_ext', 4),
        ('rtofs_ext', 5),
        ('ref_ext', 6),
        ('interp', 7),
    ])

    booleans = OrderedDict([
        (True, 0),
        (False, 1)
    ])

    clients = OrderedDict([
        ("SIS", 0),
        ("HYPACK", 1),
        ("PDS2000", 2),
        ("QINSY", 3)
    ])

    atlases = OrderedDict([
        ("WOA09", 0),
        ("WOA13", 1),
        ("RTOFS", 2),
        ("ref", 3),
    ])

    mvp_protocols = OrderedDict([
        ("NAVO_ISS60", 0),
        ("UNDEFINED", 1),
    ])

    mvp_formats = OrderedDict([
        ("S12", 0),
        ("CALC", 1),
        ("ASVP", 2)
    ])

    mvp_instruments = OrderedDict([
        ("AML_uSVP", 0),
        ("AML_uSVPT", 1),
        ("AML_Smart_SVP", 2),
        ("AML_uCTD", 3),
        ("AML_uCTD+", 4),
        ("Valeport_SVPT", 5),
        ("SBE_911+", 6),
        ("SBE_49", 7),
    ])

    kng_formats = OrderedDict([
        ('ASVP', 0),
        ('S00', 1),
        ('S01', 2),
        ('S10', 3),
        ('S11', 4),
        ('S02', 5),
        ('S12', 6),
        ('S22', 7),
    ])


