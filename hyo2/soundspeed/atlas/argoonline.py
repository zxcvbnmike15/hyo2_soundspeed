from datetime import datetime as dt, date, timedelta
from ftplib import FTP
import logging
import socket
from typing import Optional, Union
from urllib import parse

from netCDF4 import Dataset, num2date
import numpy as np

from hyo2.soundspeed.atlas.abstract import AbstractAtlas
from hyo2.abc.lib.progress.cli_progress import CliProgress
logger = logging.getLogger(__name__)


class ArgoOnline(AbstractAtlas):
    """Argo Floats Profile - Online Retrieval"""

    def __init__(self, data_folder: str, prj: 'hyo2.soundspeed.soundspeed import SoundSpeedLibrary') -> None:
        super().__init__(data_folder=data_folder, prj=prj)
        self.name = self.__class__.__name__
        self.desc = "Argo float profile"

        # How far are we willing to accept
        self._min_profile_distance = 6      # nautical miles
        self._max_profile_distance = 300    # nautical miles

        self._has_data_downloaded = False
        self._last_loaded_day = dt(1900, 1, 1)  # Old date to trigger query
        self._file = None
        self._lat = None
        self._lon = None

    def is_present(self):
        """check data already downloaded"""
        return self._has_data_downloaded
        pass

    def download_db(self) -> bool:
        pass

    def query(self, lat: Optional[float], lon: Optional[float], dtstamp: Union[dt,None]=None,
              server_mode: bool = False):
        """Query Argos database for passed timestamp and location"""

        original_datestamp = dtstamp
        if dtstamp is None:
            dtstamp = dt.utcnow()
        if not isinstance(dtstamp, dt):
            raise RuntimeError("Invalid date passed: %s" % type(dtstamp))
        logger.debug("Query: %s @ (%.6f, %.6f)" & (dtstamp, lon, lat))

        if (lat is None) or (lon is None):
            logger.error("invalid location query: %s @ (%s, %s)" % (dtstamp.strftime("%Y/%m/%d %H:%M:%S"), lon, lat))
            return None
        
        pass
    # ### private methods ###

    @staticmethod
    def _check_ftp_comm(url: str) -> bool:
        try:
            # Check connection to ftp server
            p = parse.urlparse(url)
            ftp = FTP(p.hostname)
            ftp.login()
            resp = ftp.voidcmd("NOOP")
            resp_code = int(resp.split(' ')[0])
            logger.debug("connected to ftp server: %s -> %s" % (url, resp))
            ftp.close()

        except socket.error as e:
            logger.warning("While checking %s, %s" % (url, e))
            return False

        return resp_code < 400

    def _build_ftp_url(self, input_date: dt) -> str:
        """make up the url to download latest_data profiles"""
        # Valid servers are:
        #       ftp://usgodae.org/pub/outgoing/argo
        #       ftp://ftp.ifremer.fr/ifremer/argo

    def _download_files(self, dtstamp: dt):
        pass
