# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'orders_page.ui'
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
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_OrdersPage(object):
    def setupUi(self, OrdersPage):
        if not OrdersPage.objectName():
            OrdersPage.setObjectName(u"OrdersPage")
        OrdersPage.resize(800, 600)
        self.centralwidget = QWidget(OrdersPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.back_to_main_btn = QPushButton(self.centralwidget)
        self.back_to_main_btn.setObjectName(u"back_to_main_btn")

        self.horizontalLayout_4.addWidget(self.back_to_main_btn)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.fioUserLabel_2 = QLabel(self.centralwidget)
        self.fioUserLabel_2.setObjectName(u"fioUserLabel_2")
        self.fioUserLabel_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.fioUserLabel_2)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.scrollArea_orders = QScrollArea(self.centralwidget)
        self.scrollArea_orders.setObjectName(u"scrollArea_orders")
        self.scrollArea_orders.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 780, 481))
        self.scrollArea_orders.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout.addWidget(self.scrollArea_orders, 1, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.edit_order_btn = QPushButton(self.centralwidget)
        self.edit_order_btn.setObjectName(u"edit_order_btn")

        self.horizontalLayout_3.addWidget(self.edit_order_btn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.add_order_btn = QPushButton(self.centralwidget)
        self.add_order_btn.setObjectName(u"add_order_btn")

        self.horizontalLayout_3.addWidget(self.add_order_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.del_order_btn = QPushButton(self.centralwidget)
        self.del_order_btn.setObjectName(u"del_order_btn")

        self.horizontalLayout_3.addWidget(self.del_order_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_3.addWidget(self.pushButton_4)


        self.gridLayout.addLayout(self.verticalLayout_3, 2, 0, 1, 1)

        OrdersPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(OrdersPage)

        QMetaObject.connectSlotsByName(OrdersPage)
    # setupUi

    def retranslateUi(self, OrdersPage):
        OrdersPage.setWindowTitle(QCoreApplication.translate("OrdersPage", u"MainWindow", None))
        self.back_to_main_btn.setText(QCoreApplication.translate("OrdersPage", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.fioUserLabel_2.setText(QCoreApplication.translate("OrdersPage", u"\u0424\u0418\u041e", None))
        self.edit_order_btn.setText(QCoreApplication.translate("OrdersPage", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0437\u0430\u043a\u0430\u0437", None))
        self.add_order_btn.setText(QCoreApplication.translate("OrdersPage", u"+ \u0417\u0430\u043a\u0430\u0437", None))
        self.del_order_btn.setText(QCoreApplication.translate("OrdersPage", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437", None))
        self.pushButton_4.setText(QCoreApplication.translate("OrdersPage", u"\u0412\u044b\u0439\u0442\u0438", None))
    # retranslateUi

