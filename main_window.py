# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(882, 690)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.fioUserLabel = QLabel(self.centralwidget)
        self.fioUserLabel.setObjectName(u"fioUserLabel")
        font = QFont()
        font.setPointSize(14)
        self.fioUserLabel.setFont(font)
        self.fioUserLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.fioUserLabel)

        self.searchLayout = QHBoxLayout()
        self.searchLayout.setObjectName(u"searchLayout")
        self.searchInput = QLineEdit(self.centralwidget)
        self.searchInput.setObjectName(u"searchInput")
        self.searchInput.setFont(font)

        self.searchLayout.addWidget(self.searchInput)

        self.supplierLabel = QLabel(self.centralwidget)
        self.supplierLabel.setObjectName(u"supplierLabel")
        self.supplierLabel.setFont(font)

        self.searchLayout.addWidget(self.supplierLabel)

        self.suppliersCombo = QComboBox(self.centralwidget)
        self.suppliersCombo.setObjectName(u"suppliersCombo")
        self.suppliersCombo.setFont(font)

        self.searchLayout.addWidget(self.suppliersCombo)

        self.searchLayout.setStretch(0, 4)
        self.searchLayout.setStretch(1, 1)
        self.searchLayout.setStretch(2, 2)

        self.verticalLayout_2.addLayout(self.searchLayout)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 862, 532))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.adminBtns = QHBoxLayout()
        self.adminBtns.setObjectName(u"adminBtns")
        self.editProductBtn = QPushButton(self.centralwidget)
        self.editProductBtn.setObjectName(u"editProductBtn")
        self.editProductBtn.setFont(font)

        self.adminBtns.addWidget(self.editProductBtn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.adminBtns.addItem(self.horizontalSpacer_2)

        self.addProductBtn = QPushButton(self.centralwidget)
        self.addProductBtn.setObjectName(u"addProductBtn")
        self.addProductBtn.setFont(font)

        self.adminBtns.addWidget(self.addProductBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.adminBtns.addItem(self.horizontalSpacer)

        self.deleteProductBtn = QPushButton(self.centralwidget)
        self.deleteProductBtn.setObjectName(u"deleteProductBtn")
        self.deleteProductBtn.setFont(font)

        self.adminBtns.addWidget(self.deleteProductBtn)

        self.adminBtns.setStretch(0, 2)
        self.adminBtns.setStretch(1, 1)
        self.adminBtns.setStretch(2, 2)
        self.adminBtns.setStretch(3, 1)
        self.adminBtns.setStretch(4, 2)

        self.verticalLayout.addLayout(self.adminBtns)

        self.logoutBtn = QPushButton(self.centralwidget)
        self.logoutBtn.setObjectName(u"logoutBtn")
        font1 = QFont()
        font1.setPointSize(12)
        self.logoutBtn.setFont(font1)

        self.verticalLayout.addWidget(self.logoutBtn)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.fioUserLabel.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f \u0418\u043c\u044f \u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.searchInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.supplierLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a:", None))
        self.editProductBtn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0442\u043e\u0432\u0430\u0440", None))
        self.addProductBtn.setText(QCoreApplication.translate("MainWindow", u"+ \u0422\u043e\u0432\u0430\u0440", None))
        self.deleteProductBtn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0442\u043e\u0432\u0430\u0440", None))
        self.logoutBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
    # retranslateUi

