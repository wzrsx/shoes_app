# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'order_card.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_OrderCard(object):
    def setupUi(self, OrderCard):
        if not OrderCard.objectName():
            OrderCard.setObjectName(u"OrderCard")
        OrderCard.resize(855, 348)
        self.gridLayout = QGridLayout(OrderCard)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.article_order = QLabel(OrderCard)
        self.article_order.setObjectName(u"article_order")
        font = QFont()
        font.setBold(True)
        self.article_order.setFont(font)

        self.verticalLayout.addWidget(self.article_order)

        self.status_order = QLabel(OrderCard)
        self.status_order.setObjectName(u"status_order")

        self.verticalLayout.addWidget(self.status_order)

        self.address_pvz = QLabel(OrderCard)
        self.address_pvz.setObjectName(u"address_pvz")

        self.verticalLayout.addWidget(self.address_pvz)

        self.date_order = QLabel(OrderCard)
        self.date_order.setObjectName(u"date_order")

        self.verticalLayout.addWidget(self.date_order)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.date_delivery = QLabel(OrderCard)
        self.date_delivery.setObjectName(u"date_delivery")

        self.horizontalLayout.addWidget(self.date_delivery)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 1)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.retranslateUi(OrderCard)

        QMetaObject.connectSlotsByName(OrderCard)
    # setupUi

    def retranslateUi(self, OrderCard):
        OrderCard.setWindowTitle(QCoreApplication.translate("OrderCard", u"Form", None))
        self.article_order.setText(QCoreApplication.translate("OrderCard", u"TextLabel", None))
        self.status_order.setText(QCoreApplication.translate("OrderCard", u"TextLabel", None))
        self.address_pvz.setText(QCoreApplication.translate("OrderCard", u"TextLabel", None))
        self.date_order.setText(QCoreApplication.translate("OrderCard", u"TextLabel", None))
        self.date_delivery.setText(QCoreApplication.translate("OrderCard", u"TextLabel", None))
    # retranslateUi

