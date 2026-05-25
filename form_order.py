# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_order.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_OrderForm(object):
    def setupUi(self, OrderForm):
        if not OrderForm.objectName():
            OrderForm.setObjectName(u"OrderForm")
        OrderForm.resize(873, 353)
        self.verticalLayout = QVBoxLayout(OrderForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(OrderForm)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.article_order = QLineEdit(OrderForm)
        self.article_order.setObjectName(u"article_order")

        self.verticalLayout.addWidget(self.article_order)

        self.label_2 = QLabel(OrderForm)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.status_combo = QComboBox(OrderForm)
        self.status_combo.setObjectName(u"status_combo")

        self.verticalLayout.addWidget(self.status_combo)

        self.label_3 = QLabel(OrderForm)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.address_pvz = QLineEdit(OrderForm)
        self.address_pvz.setObjectName(u"address_pvz")

        self.verticalLayout.addWidget(self.address_pvz)

        self.label_4 = QLabel(OrderForm)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.date_order = QLineEdit(OrderForm)
        self.date_order.setObjectName(u"date_order")

        self.verticalLayout.addWidget(self.date_order)

        self.label_5 = QLabel(OrderForm)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.date_delivery = QLineEdit(OrderForm)
        self.date_delivery.setObjectName(u"date_delivery")

        self.verticalLayout.addWidget(self.date_delivery)


        self.retranslateUi(OrderForm)

        QMetaObject.connectSlotsByName(OrderForm)
    # setupUi

    def retranslateUi(self, OrderForm):
        OrderForm.setWindowTitle(QCoreApplication.translate("OrderForm", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("OrderForm", u"\u0410\u0440\u0442\u0438\u043a\u0443\u043b \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.label_2.setText(QCoreApplication.translate("OrderForm", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.label_3.setText(QCoreApplication.translate("OrderForm", u"\u0410\u0434\u0440\u0435\u0441 \u041f\u0412\u0417", None))
        self.label_4.setText(QCoreApplication.translate("OrderForm", u"\u0414\u0430\u0442\u0430 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.label_5.setText(QCoreApplication.translate("OrderForm", u"\u0414\u0430\u0442\u0430 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438", None))
    # retranslateUi

