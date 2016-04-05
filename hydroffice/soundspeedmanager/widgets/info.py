from __future__ import absolute_import, division, print_function, unicode_literals

import os
import logging

from PySide import QtCore
from PySide import QtGui
from PySide import QtWebKit

logger = logging.getLogger(__name__)


class Info(QtGui.QMainWindow):

    here = os.path.abspath(os.path.join(os.path.dirname(__file__)))  # to be overloaded
    media = os.path.join(here, os.pardir, 'media')

    def __init__(self, default_url="http://www.hydroffice.org"):
        QtGui.QMainWindow.__init__(self)
        self.default_url = default_url

        self.toolbar = self.addToolBar('Shortcuts')
        self.toolbar.setIconSize(QtCore.QSize(65, 65))
        # default
        homeAction = QtGui.QAction(QtGui.QIcon(os.path.join(self.media, 'home.png')), 'Home page', self)
        homeAction.setShortcut('Alt+H')
        homeAction.triggered.connect(self.load_default)
        self.toolbar.addAction(homeAction)
        # HydrOffice.org
        hyoAction = QtGui.QAction(QtGui.QIcon(os.path.join(self.media, 'hyo.png')), 'HydrOffice.org', self)
        hyoAction.setShortcut('Ctrl+H')
        hyoAction.triggered.connect(self.load_hydroffice_org)
        self.toolbar.addAction(hyoAction)
        # ccom.unh.edu
        ccomAction = QtGui.QAction(QtGui.QIcon(os.path.join(self.media, 'ccom.png')), 'ccom.unh.edu', self)
        ccomAction.setShortcut('Alt+C')
        ccomAction.triggered.connect(self.load_ccom_unh_edu)
        self.toolbar.addAction(ccomAction)
        # unh.edu
        unhAction = QtGui.QAction(QtGui.QIcon(os.path.join(self.media, 'unh.png')), 'unh.edu', self)
        unhAction.setShortcut('Alt+U')
        unhAction.triggered.connect(self.load_unh_edu)
        self.toolbar.addAction(unhAction)

        # create the layout
        frame = QtGui.QFrame()
        self.setCentralWidget(frame)
        grid = QtGui.QGridLayout()

        # Create the web widget and the url field
        self.web = QtWebKit.QWebView(self)
        hbox = QtGui.QHBoxLayout()
        go_to_label = QtGui.QLabel('Go to:')
        hbox.addWidget(go_to_label)
        self.url_input = UrlInput(self.web, default_url)
        hbox.addWidget(self.url_input)
        grid.addLayout(hbox, 1, 0)
        grid.addWidget(self.web, 2, 0)
        frame.setLayout(grid)

        # load default
        self.load_default()

    def load_default(self):
        self.url_input.setText(self.default_url)
        self.web.load(QtCore.QUrl(self.default_url))

    def load_hydroffice_org(self):
        url = 'http://www.hydroffice.org'
        self.url_input.setText(url)
        self.web.load(QtCore.QUrl(url))

    def load_ccom_unh_edu(self):
        url = 'http://ccom.unh.edu'
        self.url_input.setText(url)
        self.web.load(QtCore.QUrl(url))

    def load_unh_edu(self):
        url = 'http://www.unh.edu'
        self.url_input.setText(url)
        self.web.load(QtCore.QUrl(url))



class UrlInput(QtGui.QLineEdit):
    def __init__(self, browser, default_url):
        super(UrlInput, self).__init__()
        self.browser = browser
        self.setText(default_url)
        self.returnPressed.connect(self.return_pressed)

    def return_pressed(self):
        url = QtCore.QUrl(self.text())
        # load url into browser frame
        self.browser.load(url)