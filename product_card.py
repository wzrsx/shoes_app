# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'product_card.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_ProductCard(object):
    def setupUi(self, ProductCard):
        if not ProductCard.objectName():
            ProductCard.setObjectName(u"ProductCard")
        ProductCard.resize(905, 341)
        self.horizontalLayout = QHBoxLayout(ProductCard)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_photo = QLabel(ProductCard)
        self.label_photo.setObjectName(u"label_photo")

        self.horizontalLayout.addWidget(self.label_photo)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_title = QLabel(ProductCard)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_title.setFont(font)

        self.verticalLayout.addWidget(self.label_title)

        self.label_desc = QLabel(ProductCard)
        self.label_desc.setObjectName(u"label_desc")

        self.verticalLayout.addWidget(self.label_desc)

        self.label_producer = QLabel(ProductCard)
        self.label_producer.setObjectName(u"label_producer")

        self.verticalLayout.addWidget(self.label_producer)

        self.label_supplier = QLabel(ProductCard)
        self.label_supplier.setObjectName(u"label_supplier")

        self.verticalLayout.addWidget(self.label_supplier)

        self.label_price = QLabel(ProductCard)
        self.label_price.setObjectName(u"label_price")

        self.verticalLayout.addWidget(self.label_price)

        self.label_measure = QLabel(ProductCard)
        self.label_measure.setObjectName(u"label_measure")

        self.verticalLayout.addWidget(self.label_measure)

        self.label_count = QLabel(ProductCard)
        self.label_count.setObjectName(u"label_count")

        self.verticalLayout.addWidget(self.label_count)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.widget_discount = QWidget(ProductCard)
        self.widget_discount.setObjectName(u"widget_discount")
        self.widget_discount.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.verticalLayout_2 = QVBoxLayout(self.widget_discount)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_discount = QLabel(self.widget_discount)
        self.label_discount.setObjectName(u"label_discount")
        self.label_discount.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_discount)


        self.horizontalLayout.addWidget(self.widget_discount)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 1)

        self.retranslateUi(ProductCard)

        QMetaObject.connectSlotsByName(ProductCard)
    # setupUi

    def retranslateUi(self, ProductCard):
        ProductCard.setWindowTitle(QCoreApplication.translate("ProductCard", u"Form", None))
        self.label_photo.setText(QCoreApplication.translate("ProductCard", u"\u0424\u043e\u0442\u043e", None))
        self.label_title.setText(QCoreApplication.translate("ProductCard", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f | \u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435:", None))
        self.label_desc.setText(QCoreApplication.translate("ProductCard", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435:", None))
        self.label_producer.setText(QCoreApplication.translate("ProductCard", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c:", None))
        self.label_supplier.setText(QCoreApplication.translate("ProductCard", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a:", None))
        self.label_price.setText(QCoreApplication.translate("ProductCard", u"\u0426\u0435\u043d\u0430:", None))
        self.label_measure.setText(QCoreApplication.translate("ProductCard", u"\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f:", None))
        self.label_count.setText(QCoreApplication.translate("ProductCard", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435:", None))
        self.label_discount.setText(QCoreApplication.translate("ProductCard", u"TextLabel", None))
    # retranslateUi

