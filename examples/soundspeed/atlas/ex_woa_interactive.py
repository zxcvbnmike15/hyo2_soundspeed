from datetime import datetime
import logging

from PySide2 import QtWidgets

from hyo2.abc.app.qt_progress import QtProgress
from hyo2.soundspeedmanager import app_info
from hyo2.soundspeed.soundspeed import SoundSpeedLibrary
from hyo2.soundspeedmanager.qt_callbacks import QtCallbacks


logging.basicConfig(level=logging.DEBUG,
                    format="%(levelname)-9s %(name)s.%(funcName)s:%(lineno)d > %(message)s")
logger = logging.getLogger(__name__)

# examples of test position:
# - offshore Portsmouth: 43.026480, -70.318824
# - Indian Ocean: -19.1, 74.16
# - middle of Africa (in land): 18.2648113, 16.1761115

switch = "WOA13"  # WOA09 or WOA13

app = QtWidgets.QApplication([])  # PySide stuff (start)
mw = QtWidgets.QMainWindow()
mw.show()

lib = SoundSpeedLibrary(progress=QtProgress(parent=mw), callbacks=QtCallbacks(parent=mw))

if switch == "WOA09":

    # download the woa09 if not present
    if not lib.has_woa09():
        success = lib.download_woa09()
        if not success:
            raise RuntimeError("unable to download")
    logger.info("has WOA09: %s" % lib.has_woa09())

    # ask user for location and timestamp
    lib.retrieve_woa09()
    logger.info("retrieved WOA09 profiles: %s" % lib.ssp)

elif switch == "WOA13":

    # download the woa09 if not present
    if not lib.has_woa13():
        success = lib.download_woa13()
        if not success:
            raise RuntimeError("unable to download")
    logger.info("has WOA13: %s" % lib.has_woa13())

    # ask user for location and timestamp
    lib.retrieve_woa13()
    logger.info("retrieved WOA13 profiles: %s" % lib.ssp)

else:
    raise RuntimeError("invalid switch value: %s" % switch)

app.exec_()
