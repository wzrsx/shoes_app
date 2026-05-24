# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_ProductForm(object):
    def setupUi(self, ProductForm):
        if not ProductForm.objectName():
            ProductForm.setObjectName(u"ProductForm")
        ProductForm.resize(859, 531)
        self.verticalLayout = QVBoxLayout(ProductForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_10 = QLabel(ProductForm)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout.addWidget(self.label_10)

        self.articleProduct = QLineEdit(ProductForm)
        self.articleProduct.setObjectName(u"articleProduct")

        self.verticalLayout.addWidget(self.articleProduct)

        self.label = QLabel(ProductForm)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.nameProduct = QLineEdit(ProductForm)
        self.nameProduct.setObjectName(u"nameProduct")

        self.verticalLayout.addWidget(self.nameProduct)

        self.label_2 = QLabel(ProductForm)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.comboCategory = QComboBox(ProductForm)
        self.comboCategory.setObjectName(u"comboCategory")

        self.verticalLayout.addWidget(self.comboCategory)

        self.label_3 = QLabel(ProductForm)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.descProduct = QLineEdit(ProductForm)
        self.descProduct.setObjectName(u"descProduct")

        self.verticalLayout.addWidget(self.descProduct)

        self.label_4 = QLabel(ProductForm)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.comboProducer = QComboBox(ProductForm)
        self.comboProducer.setObjectName(u"comboProducer")

        self.verticalLayout.addWidget(self.comboProducer)

        self.label_5 = QLabel(ProductForm)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.supplierProduct = QLineEdit(ProductForm)
        self.supplierProduct.setObjectName(u"supplierProduct")

        self.verticalLayout.addWidget(self.supplierProduct)

        self.label_6 = QLabel(ProductForm)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.priceProduct = QLineEdit(ProductForm)
        self.priceProduct.setObjectName(u"priceProduct")

        self.verticalLayout.addWidget(self.priceProduct)

        self.label_7 = QLabel(ProductForm)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.comboUnit = QComboBox(ProductForm)
        self.comboUnit.setObjectName(u"comboUnit")

        self.verticalLayout.addWidget(self.comboUnit)

        self.label_8 = QLabel(ProductForm)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.countProduct = QLineEdit(ProductForm)
        self.countProduct.setObjectName(u"countProduct")

        self.verticalLayout.addWidget(self.countProduct)

        self.label_9 = QLabel(ProductForm)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout.addWidget(self.label_9)

        self.discountProduct = QLineEdit(ProductForm)
        self.discountProduct.setObjectName(u"discountProduct")

        self.verticalLayout.addWidget(self.discountProduct)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancelBtn = QPushButton(ProductForm)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)

        self.saveBtn = QPushButton(ProductForm)
        self.saveBtn.setObjectName(u"saveBtn")

        self.horizontalLayout.addWidget(self.saveBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ProductForm)

        QMetaObject.connectSlotsByName(ProductForm)
    # setupUi

    def retranslateUi(self, ProductForm):
        ProductForm.setWindowTitle(QCoreApplication.translate("ProductForm", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435/\u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.label_10.setText(QCoreApplication.translate("ProductForm", u"\u0410\u0440\u0442\u0438\u043a\u0443\u043b", None))
        self.label.setText(QCoreApplication.translate("ProductForm", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.label_2.setText(QCoreApplication.translate("ProductForm", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.label_3.setText(QCoreApplication.translate("ProductForm", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435\u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.label_4.setText(QCoreApplication.translate("ProductForm", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c", None))
        self.label_5.setText(QCoreApplication.translate("ProductForm", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a", None))
        self.label_6.setText(QCoreApplication.translate("ProductForm", u"\u0426\u0435\u043d\u0430", None))
        self.label_7.setText(QCoreApplication.translate("ProductForm", u"\u0415\u0434\u0438\u043d\u0438\u0446\u0430\u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None))
        self.label_8.setText(QCoreApplication.translate("ProductForm", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435", None))
        self.label_9.setText(QCoreApplication.translate("ProductForm", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0443\u044e\u0449\u0430\u044f \u0441\u043a\u0438\u0434\u043a\u0430", None))
        self.cancelBtn.setText(QCoreApplication.translate("ProductForm", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.saveBtn.setText(QCoreApplication.translate("ProductForm", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

