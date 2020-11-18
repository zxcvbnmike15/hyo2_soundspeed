import unittest
import os
import shutil
import logging

from hyo2.soundspeed.atlas.argoonline import ArgoOnline
from hyo2.soundspeed.soundspeed import SoundSpeedLibrary

logger = logging.getLogger()


class TestSoundSpeedAtlasArgoOnline(unittest.TestCase):

    def setUp(self) -> None:
        self.cur_dir = os.path.abspath(os.path.dirname(__file__))

    def tearDown(self) -> None:
        dir_items = os.listdir(self.cur_dir)
        for item in dir_items:
            if item.split('.')[-1] == 'db':
                os.remove(os.path.join(self.cur_dir, item))
            if item == 'atlases':
                shutil.rmtree(os.path.join(self.cur_dir, item))

    def test_creation_of_Argo(self):
        prj = SoundSpeedLibrary(data_folder=self.cur_dir)
        argo = ArgoOnline(data_folder=prj.argo_folder, prj=prj)
        self.assertTrue('argo' in argo.data_folder)