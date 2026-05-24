# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(635, 326)
        self.verticalLayout = QVBoxLayout(LoginWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(LoginWindow)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.label = QLabel(LoginWindow)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(16)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout.addWidget(self.label)

        self.loginInput = QLineEdit(LoginWindow)
        self.loginInput.setObjectName(u"loginInput")

        self.verticalLayout.addWidget(self.loginInput)

        self.label_2 = QLabel(LoginWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout.addWidget(self.label_2)

        self.passInput = QLineEdit(LoginWindow)
        self.passInput.setObjectName(u"passInput")
        self.passInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.passInput)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.loginBtn = QPushButton(LoginWindow)
        self.loginBtn.setObjectName(u"loginBtn")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.loginBtn.setFont(font2)

        self.verticalLayout_2.addWidget(self.loginBtn)

        self.guestBtn = QPushButton(LoginWindow)
        self.guestBtn.setObjectName(u"guestBtn")
        font3 = QFont()
        font3.setPointSize(14)
        self.guestBtn.setFont(font3)

        self.verticalLayout_2.addWidget(self.guestBtn)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("LoginWindow", u"\u041c\u0430\u0433\u0430\u0437\u0438\u043d \u043e\u0431\u0443\u0432\u0438", None))
        self.label.setText(QCoreApplication.translate("LoginWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.loginInput.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d", None))
        self.label_2.setText(QCoreApplication.translate("LoginWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.passInput.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.loginBtn.setText(QCoreApplication.translate("LoginWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.guestBtn.setText(QCoreApplication.translate("LoginWindow", u"\u0413\u043e\u0441\u0442\u044c", None))
    # retranslateUi

