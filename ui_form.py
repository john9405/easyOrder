# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QTextBrowser, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(Widget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(Widget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_7)

        self.issuerId = QLineEdit(Widget)
        self.issuerId.setObjectName(u"issuerId")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.issuerId)

        self.keyId = QLineEdit(Widget)
        self.keyId.setObjectName(u"keyId")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.keyId)

        self.bundleId = QLineEdit(Widget)
        self.bundleId.setObjectName(u"bundleId")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.bundleId)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filePath = QLineEdit(Widget)
        self.filePath.setObjectName(u"filePath")

        self.horizontalLayout.addWidget(self.filePath)

        self.sel_btn = QPushButton(Widget)
        self.sel_btn.setObjectName(u"sel_btn")

        self.horizontalLayout.addWidget(self.sel_btn)


        self.formLayout_2.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.PRODUCTION = QRadioButton(Widget)
        self.PRODUCTION.setObjectName(u"PRODUCTION")
        self.PRODUCTION.setChecked(True)

        self.horizontalLayout_2.addWidget(self.PRODUCTION)

        self.SANDBOX = QRadioButton(Widget)
        self.SANDBOX.setObjectName(u"SANDBOX")

        self.horizontalLayout_2.addWidget(self.SANDBOX)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.formLayout_2.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.orderId = QLineEdit(Widget)
        self.orderId.setObjectName(u"orderId")

        self.horizontalLayout_3.addWidget(self.orderId)

        self.sub_btn = QPushButton(Widget)
        self.sub_btn.setObjectName(u"sub_btn")

        self.horizontalLayout_3.addWidget(self.sub_btn)


        self.formLayout_2.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(Widget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.clr_btn = QPushButton(Widget)
        self.clr_btn.setObjectName(u"clr_btn")

        self.horizontalLayout_4.addWidget(self.clr_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.formLayout_2.setLayout(6, QFormLayout.FieldRole, self.verticalLayout)


        self.verticalLayout_2.addLayout(self.formLayout_2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"easy order", None))
        self.label.setText(QCoreApplication.translate("Widget", u"issuer id", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"key id", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"bundle id", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"encoded key", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"environment", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"order id", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"result", None))
        self.filePath.setText(QCoreApplication.translate("Widget", u"/path/to/SubscriptionKey_xxx.p8", None))
        self.sel_btn.setText(QCoreApplication.translate("Widget", u"Select", None))
        self.PRODUCTION.setText(QCoreApplication.translate("Widget", u"PRODUCTION", None))
        self.SANDBOX.setText(QCoreApplication.translate("Widget", u"SANDBOX", None))
        self.sub_btn.setText(QCoreApplication.translate("Widget", u"Search", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu Sans'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.clr_btn.setText(QCoreApplication.translate("Widget", u"Clear", None))
    # retranslateUi

