# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'main_pagesWVIGns.ui'
##
# Created by: Qt User Interface Compiler version 6.4.3
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 600)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt;")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.page_1)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.label)

        self.frame_btn_1 = QFrame(self.page_1)
        self.frame_btn_1.setObjectName(u"frame_btn_1")
        self.frame_btn_1.setMinimumSize(QSize(0, 40))
        self.frame_btn_1.setMaximumSize(QSize(16777215, 40))
        self.frame_btn_1.setFrameShape(QFrame.StyledPanel)
        self.frame_btn_1.setFrameShadow(QFrame.Raised)
        self.btn_1_layout = QVBoxLayout(self.frame_btn_1)
        self.btn_1_layout.setSpacing(0)
        self.btn_1_layout.setObjectName(u"btn_1_layout")
        self.btn_1_layout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_btn_1)
        self.pushButton.setObjectName(u"pushButton")

        self.btn_1_layout.addWidget(self.pushButton)

        self.verticalLayout.addWidget(self.frame_btn_1)

        self.Reinstatement_Date_Edit = QDateEdit(self.page_1)
        self.Reinstatement_Date_Edit.setObjectName(u"Reinstatement_Date_Edit")

        self.verticalLayout.addWidget(self.Reinstatement_Date_Edit)

        self.spinBox = QSpinBox(self.page_1)
        self.spinBox.setObjectName(u"spinBox")

        self.verticalLayout.addWidget(self.spinBox)

        self.page_1_layout.addLayout(self.verticalLayout)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"background:orange")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"background:lightblue")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.empty_page_label = QLabel(self.page_3)
        self.empty_page_label.setObjectName(u"empty_page_label")
        font = QFont()
        font.setPointSize(16)
        self.empty_page_label.setFont(font)
        self.empty_page_label.setAlignment(Qt.AlignCenter)

        self.page_3_layout.addWidget(self.empty_page_label)

        self.pages.addWidget(self.page_3)

        self.main_pages_layout.addWidget(self.pages)

        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(
            QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate(
            "MainPages", u"Reinstatement Automation", None))
        self.pushButton.setText(QCoreApplication.translate(
            "MainPages", u"PushButton", None))
        self.empty_page_label.setText(
            QCoreApplication.translate("MainPages", u"Empty Page", None))
    # retranslateUi
