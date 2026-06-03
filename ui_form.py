# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.x
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 750)
        Widget.setMinimumSize(QSize(600, 650))
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setSpacing(16)
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        # Configuration Group
        self.configGroup = QGroupBox(Widget)
        self.configGroup.setObjectName(u"configGroup")
        self.formLayout_2 = QFormLayout(self.configGroup)
        self.formLayout_2.setHorizontalSpacing(16)
        self.formLayout_2.setVerticalSpacing(12)
        self.formLayout_2.setObjectName(u"formLayout_2")

        self.label = QLabel(self.configGroup)
        self.label.setObjectName(u"label")
        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.configGroup)
        self.label_2.setObjectName(u"label_2")
        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.configGroup)
        self.label_3.setObjectName(u"label_3")
        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.configGroup)
        self.label_4.setObjectName(u"label_4")
        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.configGroup)
        self.label_5.setObjectName(u"label_5")
        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.issuerId = QLineEdit(self.configGroup)
        self.issuerId.setObjectName(u"issuerId")
        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.issuerId)

        self.keyId = QLineEdit(self.configGroup)
        self.keyId.setObjectName(u"keyId")
        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.keyId)

        self.bundleId = QLineEdit(self.configGroup)
        self.bundleId.setObjectName(u"bundleId")
        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.bundleId)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filePath = QLineEdit(self.configGroup)
        self.filePath.setObjectName(u"filePath")
        self.horizontalLayout.addWidget(self.filePath)

        self.sel_btn = QPushButton(self.configGroup)
        self.sel_btn.setObjectName(u"sel_btn")
        self.horizontalLayout.addWidget(self.sel_btn)

        self.formLayout_2.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.PRODUCTION = QRadioButton(self.configGroup)
        self.PRODUCTION.setObjectName(u"PRODUCTION")
        self.PRODUCTION.setChecked(True)
        self.horizontalLayout_2.addWidget(self.PRODUCTION)

        self.SANDBOX = QRadioButton(self.configGroup)
        self.SANDBOX.setObjectName(u"SANDBOX")
        self.horizontalLayout_2.addWidget(self.SANDBOX)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.formLayout_2.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.verticalLayout_2.addWidget(self.configGroup)

        # Query Group
        self.queryGroup = QGroupBox(Widget)
        self.queryGroup.setObjectName(u"queryGroup")
        self.verticalLayout_3 = QVBoxLayout(self.queryGroup)
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.label_6 = QLabel(self.queryGroup)
        self.label_6.setObjectName(u"label_6")
        self.horizontalLayout_3.addWidget(self.label_6)

        self.orderId = QLineEdit(self.queryGroup)
        self.orderId.setObjectName(u"orderId")
        self.horizontalLayout_3.addWidget(self.orderId)

        self.sub_btn = QPushButton(self.queryGroup)
        self.sub_btn.setObjectName(u"sub_btn")
        self.horizontalLayout_3.addWidget(self.sub_btn)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.label_7 = QLabel(self.queryGroup)
        self.label_7.setObjectName(u"label_7")
        self.verticalLayout_3.addWidget(self.label_7)

        self.textBrowser = QTextBrowser(self.queryGroup)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(0, 280))
        self.verticalLayout_3.addWidget(self.textBrowser)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.clr_btn = QPushButton(self.queryGroup)
        self.clr_btn.setObjectName(u"clr_btn")
        self.horizontalLayout_4.addWidget(self.clr_btn)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalLayout_2.addWidget(self.queryGroup)

        self.retranslateUi(Widget)
        QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"easy order", None))
        self.configGroup.setTitle(QCoreApplication.translate("Widget", u"配置", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Issuer ID", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Key ID", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Bundle ID", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Private Key", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Environment", None))
        self.issuerId.setPlaceholderText(QCoreApplication.translate("Widget", u"Enter issuer ID", None))
        self.keyId.setPlaceholderText(QCoreApplication.translate("Widget", u"Enter key ID", None))
        self.bundleId.setPlaceholderText(QCoreApplication.translate("Widget", u"Enter bundle ID", None))
        self.filePath.setText(QCoreApplication.translate("Widget", u"/path/to/SubscriptionKey_xxx.p8", None))
        self.filePath.setPlaceholderText(QCoreApplication.translate("Widget", u"Select .p8 key file", None))
        self.sel_btn.setText(QCoreApplication.translate("Widget", u"Select", None))
        self.PRODUCTION.setText(QCoreApplication.translate("Widget", u"PRODUCTION", None))
        self.SANDBOX.setText(QCoreApplication.translate("Widget", u"SANDBOX", None))
        self.queryGroup.setTitle(QCoreApplication.translate("Widget", u"查询", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Order ID", None))
        self.orderId.setPlaceholderText(QCoreApplication.translate("Widget", u"Enter order ID to search", None))
        self.sub_btn.setText(QCoreApplication.translate("Widget", u"Search", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Result", None))
        self.clr_btn.setText(QCoreApplication.translate("Widget", u"Clear", None))