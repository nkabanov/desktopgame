# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import res_rc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1569, 640)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(135, 206, 235, 255), stop:1 rgba(255, 250, 250, 255));\n"
"font-family: Comfortaa\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout_9 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.main_menu = QWidget()
        self.main_menu.setObjectName(u"main_menu")
        sizePolicy.setHeightForWidth(self.main_menu.sizePolicy().hasHeightForWidth())
        self.main_menu.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.main_menu)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 50)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(350, 75, 350, -1)
        self.label_8 = QLabel(self.main_menu)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Comfortaa"])
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 40px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"qproperty-alignment: 'AlignCenter';\n"
"text-align: left;\n"
"padding-left: 60px;\n"
"background-color: rgb(208, 233, 244);\n"
"")

        self.verticalLayout_6.addWidget(self.label_8)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.verticalLayout_6.setStretch(0, 2)
        self.verticalLayout_6.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(350, -1, 350, -1)
        self.label_13 = QLabel(self.main_menu)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 7px;\n"
"background-color: rgb(208, 233, 244);\n"
"")
        self.label_13.setPixmap(QPixmap(u":/icon/icons/play2.svg"))
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_13)

        self.btn_gamemodes_2 = QPushButton(self.main_menu)
        self.btn_gamemodes_2.setObjectName(u"btn_gamemodes_2")
        sizePolicy.setHeightForWidth(self.btn_gamemodes_2.sizePolicy().hasHeightForWidth())
        self.btn_gamemodes_2.setSizePolicy(sizePolicy)
        self.btn_gamemodes_2.setFont(font)
        self.btn_gamemodes_2.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:40px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")
        self.btn_gamemodes_2.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_gamemodes_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 10)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(350, -1, 350, -1)
        self.label_14 = QLabel(self.main_menu)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setStyleSheet(u"background-color: rgb(208, 233, 244);\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"\n"
"")
        self.label_14.setPixmap(QPixmap(u":/icon/icons/dictionary.svg"))
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_14)

        self.btn_dictionary_2 = QPushButton(self.main_menu)
        self.btn_dictionary_2.setObjectName(u"btn_dictionary_2")
        sizePolicy.setHeightForWidth(self.btn_dictionary_2.sizePolicy().hasHeightForWidth())
        self.btn_dictionary_2.setSizePolicy(sizePolicy)
        self.btn_dictionary_2.setFont(font)
        self.btn_dictionary_2.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:40px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.horizontalLayout_2.addWidget(self.btn_dictionary_2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 10)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(350, -1, 350, -1)
        self.label_7 = QLabel(self.main_menu)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setStyleSheet(u"background-color: rgb(208, 233, 244);\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"\n"
"")
        self.label_7.setPixmap(QPixmap(u":/icon/icons/stats.svg"))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.btn_stats = QPushButton(self.main_menu)
        self.btn_stats.setObjectName(u"btn_stats")
        sizePolicy.setHeightForWidth(self.btn_stats.sizePolicy().hasHeightForWidth())
        self.btn_stats.setSizePolicy(sizePolicy)
        self.btn_stats.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:40px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.horizontalLayout_6.addWidget(self.btn_stats)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 10)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(350, -1, 350, -1)
        self.label_12 = QLabel(self.main_menu)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 7px;\n"
"background-color: rgb(208, 233, 244);")
        self.label_12.setPixmap(QPixmap(u":/icon/icons/feedback.svg"))
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_12)

        self.btn_feedback_2 = QPushButton(self.main_menu)
        self.btn_feedback_2.setObjectName(u"btn_feedback_2")
        sizePolicy.setHeightForWidth(self.btn_feedback_2.sizePolicy().hasHeightForWidth())
        self.btn_feedback_2.setSizePolicy(sizePolicy)
        self.btn_feedback_2.setFont(font)
        self.btn_feedback_2.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:40px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.horizontalLayout_3.addWidget(self.btn_feedback_2)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 10)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)

        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.stackedWidget.addWidget(self.main_menu)
        self.game_modes = QWidget()
        self.game_modes.setObjectName(u"game_modes")
        sizePolicy.setHeightForWidth(self.game_modes.sizePolicy().hasHeightForWidth())
        self.game_modes.setSizePolicy(sizePolicy)
        self.verticalLayout_12 = QVBoxLayout(self.game_modes)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.back_3 = QPushButton(self.game_modes)
        self.back_3.setObjectName(u"back_3")
        sizePolicy.setHeightForWidth(self.back_3.sizePolicy().hasHeightForWidth())
        self.back_3.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Comfortaa"])
        font1.setPointSize(28)
        font1.setBold(False)
        self.back_3.setFont(font1)
        self.back_3.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"	background-color: rgb(208, 233, 244);\n"
"	border: 2px solid black;\n"
"	border-radius: 7px;\n"
"	box-shadow: 1 1 1px rgba(255, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #d0dff4;\n"
"} \n"
"QPushButton:pressed {\n"
"	background-color: #1f6391;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icon/icons/back.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.back_3.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.back_3)

        self.label_5 = QLabel(self.game_modes)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 40px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"\n"
"background-color: rgb(208, 233, 244);\n"
"")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 21)

        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(50)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, -1, 0, -1)
        self.label = QLabel(self.game_modes)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 40px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: rgb(208, 233, 244);\n"
"")

        self.verticalLayout_13.addWidget(self.label)


        self.verticalLayout_9.addLayout(self.verticalLayout_13)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(25)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(350, -1, 350, 50)
        self.btn_easymode = QPushButton(self.game_modes)
        self.btn_easymode.setObjectName(u"btn_easymode")
        sizePolicy.setHeightForWidth(self.btn_easymode.sizePolicy().hasHeightForWidth())
        self.btn_easymode.setSizePolicy(sizePolicy)
        self.btn_easymode.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:40px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.verticalLayout_7.addWidget(self.btn_easymode)

        self.btn_hardmode = QPushButton(self.game_modes)
        self.btn_hardmode.setObjectName(u"btn_hardmode")
        sizePolicy.setHeightForWidth(self.btn_hardmode.sizePolicy().hasHeightForWidth())
        self.btn_hardmode.setSizePolicy(sizePolicy)
        self.btn_hardmode.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:40px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.verticalLayout_7.addWidget(self.btn_hardmode)

        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 1)

        self.verticalLayout_9.addLayout(self.verticalLayout_7)

        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 7)

        self.verticalLayout_10.addLayout(self.verticalLayout_9)

        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 15)

        self.verticalLayout_8.addLayout(self.verticalLayout_10)


        self.verticalLayout_12.addLayout(self.verticalLayout_8)

        self.stackedWidget.addWidget(self.game_modes)
        self.easy_game = QWidget()
        self.easy_game.setObjectName(u"easy_game")
        sizePolicy.setHeightForWidth(self.easy_game.sizePolicy().hasHeightForWidth())
        self.easy_game.setSizePolicy(sizePolicy)
        self.verticalLayout_17 = QVBoxLayout(self.easy_game)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.back_4 = QPushButton(self.easy_game)
        self.back_4.setObjectName(u"back_4")
        sizePolicy.setHeightForWidth(self.back_4.sizePolicy().hasHeightForWidth())
        self.back_4.setSizePolicy(sizePolicy)
        self.back_4.setFont(font1)
        self.back_4.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")
        self.back_4.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.back_4)

        self.label_15 = QLabel(self.easy_game)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 35px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: rgb(208, 233, 244);\n"
"")

        self.horizontalLayout_4.addWidget(self.label_15)

        self.label_18 = QLabel(self.easy_game)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 35px;\n"
"background-color: rgb(208, 233, 244);\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"\n"
"")
        self.label_18.setTextFormat(Qt.TextFormat.AutoText)
        self.label_18.setScaledContents(False)
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_18.setWordWrap(False)

        self.horizontalLayout_4.addWidget(self.label_18)

        self.label_17 = QLabel(self.easy_game)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 35px;\n"
"background-color: rgb(208, 233, 244);\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"\n"
"")
        self.label_17.setTextFormat(Qt.TextFormat.AutoText)
        self.label_17.setScaledContents(False)
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_17.setWordWrap(False)

        self.horizontalLayout_4.addWidget(self.label_17)

        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 15)
        self.horizontalLayout_4.setStretch(2, 3)
        self.horizontalLayout_4.setStretch(3, 3)

        self.verticalLayout_16.addLayout(self.horizontalLayout_4)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 0, -1, -1)
        self.label_6 = QLabel(self.easy_game)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 35px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: rgb(208, 233, 244);\n"
"")

        self.verticalLayout_15.addWidget(self.label_6)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(35)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(50, -1, 50, -1)
        self.easy_answer2 = QPushButton(self.easy_game)
        self.easy_answer2.setObjectName(u"easy_answer2")
        sizePolicy.setHeightForWidth(self.easy_answer2.sizePolicy().hasHeightForWidth())
        self.easy_answer2.setSizePolicy(sizePolicy)
        self.easy_answer2.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:25px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.horizontalLayout_10.addWidget(self.easy_answer2)

        self.easy_answer1 = QPushButton(self.easy_game)
        self.easy_answer1.setObjectName(u"easy_answer1")
        sizePolicy.setHeightForWidth(self.easy_answer1.sizePolicy().hasHeightForWidth())
        self.easy_answer1.setSizePolicy(sizePolicy)
        self.easy_answer1.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:25px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.horizontalLayout_10.addWidget(self.easy_answer1)

        self.easy_answer3 = QPushButton(self.easy_game)
        self.easy_answer3.setObjectName(u"easy_answer3")
        sizePolicy.setHeightForWidth(self.easy_answer3.sizePolicy().hasHeightForWidth())
        self.easy_answer3.setSizePolicy(sizePolicy)
        self.easy_answer3.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:25px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.horizontalLayout_10.addWidget(self.easy_answer3)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 1)
        self.horizontalLayout_10.setStretch(2, 1)

        self.verticalLayout_15.addLayout(self.horizontalLayout_10)

        self.verticalLayout_15.setStretch(0, 1)
        self.verticalLayout_15.setStretch(1, 7)

        self.verticalLayout_16.addLayout(self.verticalLayout_15)

        self.verticalLayout_16.setStretch(0, 1)
        self.verticalLayout_16.setStretch(1, 15)

        self.verticalLayout_14.addLayout(self.verticalLayout_16)


        self.verticalLayout_17.addLayout(self.verticalLayout_14)

        self.stackedWidget.addWidget(self.easy_game)
        self.hard_game = QWidget()
        self.hard_game.setObjectName(u"hard_game")
        self.verticalLayout_21 = QVBoxLayout(self.hard_game)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.back_5 = QPushButton(self.hard_game)
        self.back_5.setObjectName(u"back_5")
        sizePolicy.setHeightForWidth(self.back_5.sizePolicy().hasHeightForWidth())
        self.back_5.setSizePolicy(sizePolicy)
        self.back_5.setFont(font1)
        self.back_5.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")
        self.back_5.setIcon(icon)

        self.horizontalLayout_11.addWidget(self.back_5)

        self.label_16 = QLabel(self.hard_game)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 35px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: rgb(208, 233, 244);\n"
"")

        self.horizontalLayout_11.addWidget(self.label_16)

        self.label_19 = QLabel(self.hard_game)
        self.label_19.setObjectName(u"label_19")
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 35px;\n"
"background-color: rgb(208, 233, 244);\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"\n"
"")
        self.label_19.setTextFormat(Qt.TextFormat.AutoText)
        self.label_19.setScaledContents(False)
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_19.setWordWrap(False)

        self.horizontalLayout_11.addWidget(self.label_19)

        self.label_20 = QLabel(self.hard_game)
        self.label_20.setObjectName(u"label_20")
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 35px;\n"
"background-color: rgb(208, 233, 244);\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"\n"
"")
        self.label_20.setTextFormat(Qt.TextFormat.AutoText)
        self.label_20.setScaledContents(False)
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_20.setWordWrap(False)

        self.horizontalLayout_11.addWidget(self.label_20)

        self.horizontalLayout_11.setStretch(0, 2)
        self.horizontalLayout_11.setStretch(1, 15)
        self.horizontalLayout_11.setStretch(2, 3)
        self.horizontalLayout_11.setStretch(3, 3)

        self.verticalLayout_20.addLayout(self.horizontalLayout_11)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, -1, -1, 150)
        self.label_2 = QLabel(self.hard_game)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 35px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: rgb(208, 233, 244);\n"
"")

        self.verticalLayout_19.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.hard_game)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 35px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: rgb(208, 233, 244);\n"
"")

        self.verticalLayout_19.addWidget(self.lineEdit)

        self.verticalLayout_19.setStretch(0, 1)
        self.verticalLayout_19.setStretch(1, 7)

        self.verticalLayout_20.addLayout(self.verticalLayout_19)

        self.verticalLayout_20.setStretch(0, 1)
        self.verticalLayout_20.setStretch(1, 15)

        self.verticalLayout_18.addLayout(self.verticalLayout_20)


        self.verticalLayout_21.addLayout(self.verticalLayout_18)

        self.stackedWidget.addWidget(self.hard_game)
        self.dictionary = QWidget()
        self.dictionary.setObjectName(u"dictionary")
        self.verticalLayout_27 = QVBoxLayout(self.dictionary)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(50)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.back_2 = QPushButton(self.dictionary)
        self.back_2.setObjectName(u"back_2")
        sizePolicy.setHeightForWidth(self.back_2.sizePolicy().hasHeightForWidth())
        self.back_2.setSizePolicy(sizePolicy)
        self.back_2.setFont(font1)
        self.back_2.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")
        self.back_2.setIcon(icon)

        self.horizontalLayout_12.addWidget(self.back_2)

        self.label_3 = QLabel(self.dictionary)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 40px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: rgb(208, 233, 244);\n"
"")

        self.horizontalLayout_12.addWidget(self.label_3)

        self.horizontalLayout_12.setStretch(0, 2)
        self.horizontalLayout_12.setStretch(1, 21)

        self.verticalLayout_26.addLayout(self.horizontalLayout_12)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_21 = QLabel(self.dictionary)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 40px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: rgb(208, 233, 244);\n"
"")

        self.verticalLayout_25.addWidget(self.label_21)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(-1, 50, -1, 50)
        self.btn_user_search = QPushButton(self.dictionary)
        self.btn_user_search.setObjectName(u"btn_user_search")
        sizePolicy.setHeightForWidth(self.btn_user_search.sizePolicy().hasHeightForWidth())
        self.btn_user_search.setSizePolicy(sizePolicy)
        self.btn_user_search.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:40px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.verticalLayout_24.addWidget(self.btn_user_search)

        self.btn_po_bukvam = QPushButton(self.dictionary)
        self.btn_po_bukvam.setObjectName(u"btn_po_bukvam")
        sizePolicy.setHeightForWidth(self.btn_po_bukvam.sizePolicy().hasHeightForWidth())
        self.btn_po_bukvam.setSizePolicy(sizePolicy)
        self.btn_po_bukvam.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:40px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.verticalLayout_24.addWidget(self.btn_po_bukvam)

        self.btn_sokr_list = QPushButton(self.dictionary)
        self.btn_sokr_list.setObjectName(u"btn_sokr_list")
        sizePolicy.setHeightForWidth(self.btn_sokr_list.sizePolicy().hasHeightForWidth())
        self.btn_sokr_list.setSizePolicy(sizePolicy)
        self.btn_sokr_list.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:40px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.verticalLayout_24.addWidget(self.btn_sokr_list)

        self.verticalLayout_24.setStretch(0, 1)
        self.verticalLayout_24.setStretch(1, 1)
        self.verticalLayout_24.setStretch(2, 1)

        self.verticalLayout_25.addLayout(self.verticalLayout_24)

        self.verticalLayout_25.setStretch(0, 1)
        self.verticalLayout_25.setStretch(1, 7)

        self.verticalLayout_26.addLayout(self.verticalLayout_25)

        self.verticalLayout_26.setStretch(0, 1)
        self.verticalLayout_26.setStretch(1, 15)

        self.verticalLayout_23.addLayout(self.verticalLayout_26)


        self.verticalLayout_27.addLayout(self.verticalLayout_23)

        self.stackedWidget.addWidget(self.dictionary)
        self.feedback_ty = QWidget()
        self.feedback_ty.setObjectName(u"feedback_ty")
        self.verticalLayout_50 = QVBoxLayout(self.feedback_ty)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setSpacing(48)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(175, 150, 175, 150)
        self.label_25 = QLabel(self.feedback_ty)
        self.label_25.setObjectName(u"label_25")
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 40px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"background-color: rgb(208, 233, 244);\n"
"")
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_49.addWidget(self.label_25)

        self.back_30 = QPushButton(self.feedback_ty)
        self.back_30.setObjectName(u"back_30")
        sizePolicy.setHeightForWidth(self.back_30.sizePolicy().hasHeightForWidth())
        self.back_30.setSizePolicy(sizePolicy)
        self.back_30.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:40px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.verticalLayout_49.addWidget(self.back_30)

        self.verticalLayout_49.setStretch(0, 5)
        self.verticalLayout_49.setStretch(1, 4)

        self.verticalLayout_48.addLayout(self.verticalLayout_49)


        self.verticalLayout_50.addLayout(self.verticalLayout_48)

        self.stackedWidget.addWidget(self.feedback_ty)
        self.game_result = QWidget()
        self.game_result.setObjectName(u"game_result")
        sizePolicy.setHeightForWidth(self.game_result.sizePolicy().hasHeightForWidth())
        self.game_result.setSizePolicy(sizePolicy)
        self.verticalLayout_30 = QVBoxLayout(self.game_result)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setSpacing(48)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(175, 150, 175, 150)
        self.label_66 = QLabel(self.game_result)
        self.label_66.setObjectName(u"label_66")
        sizePolicy.setHeightForWidth(self.label_66.sizePolicy().hasHeightForWidth())
        self.label_66.setSizePolicy(sizePolicy)
        self.label_66.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size:35px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: rgb(208, 233, 244);\n"
"")

        self.verticalLayout_29.addWidget(self.label_66)

        self.back_1 = QPushButton(self.game_result)
        self.back_1.setObjectName(u"back_1")
        sizePolicy.setHeightForWidth(self.back_1.sizePolicy().hasHeightForWidth())
        self.back_1.setSizePolicy(sizePolicy)
        self.back_1.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.verticalLayout_29.addWidget(self.back_1)

        self.verticalLayout_29.setStretch(0, 5)
        self.verticalLayout_29.setStretch(1, 4)

        self.verticalLayout_28.addLayout(self.verticalLayout_29)


        self.verticalLayout_30.addLayout(self.verticalLayout_28)

        self.stackedWidget.addWidget(self.game_result)
        self.user_search = QWidget()
        self.user_search.setObjectName(u"user_search")
        self.verticalLayout_34 = QVBoxLayout(self.user_search)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.back_6 = QPushButton(self.user_search)
        self.back_6.setObjectName(u"back_6")
        sizePolicy.setHeightForWidth(self.back_6.sizePolicy().hasHeightForWidth())
        self.back_6.setSizePolicy(sizePolicy)
        self.back_6.setFont(font1)
        self.back_6.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")
        self.back_6.setIcon(icon)

        self.horizontalLayout_13.addWidget(self.back_6)

        self.label_22 = QLabel(self.user_search)
        self.label_22.setObjectName(u"label_22")
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 35px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: rgb(208, 233, 244);\n"
"")

        self.horizontalLayout_13.addWidget(self.label_22)

        self.horizontalLayout_13.setStretch(0, 2)
        self.horizontalLayout_13.setStretch(1, 21)

        self.verticalLayout_33.addLayout(self.horizontalLayout_13)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_4 = QLabel(self.user_search)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 35px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: rgb(208, 233, 244);\n"
"")

        self.verticalLayout_32.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(self.user_search)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 35px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: rgb(208, 233, 244);\n"
"")

        self.verticalLayout_32.addWidget(self.lineEdit_2)

        self.listWidget = QListWidget(self.user_search)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 35px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: rgb(208, 233, 244);\n"
"\n"
"")

        self.verticalLayout_32.addWidget(self.listWidget)

        self.verticalLayout_32.setStretch(0, 1)
        self.verticalLayout_32.setStretch(1, 1)
        self.verticalLayout_32.setStretch(2, 2)

        self.verticalLayout_33.addLayout(self.verticalLayout_32)

        self.verticalLayout_33.setStretch(0, 1)
        self.verticalLayout_33.setStretch(1, 15)

        self.verticalLayout_31.addLayout(self.verticalLayout_33)


        self.verticalLayout_34.addLayout(self.verticalLayout_31)

        self.stackedWidget.addWidget(self.user_search)
        self.user_search_result = QWidget()
        self.user_search_result.setObjectName(u"user_search_result")
        self.verticalLayout_38 = QVBoxLayout(self.user_search_result)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.back_22 = QPushButton(self.user_search_result)
        self.back_22.setObjectName(u"back_22")
        sizePolicy.setHeightForWidth(self.back_22.sizePolicy().hasHeightForWidth())
        self.back_22.setSizePolicy(sizePolicy)
        self.back_22.setFont(font1)
        self.back_22.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")
        self.back_22.setIcon(icon)

        self.horizontalLayout_14.addWidget(self.back_22)

        self.label_67 = QLabel(self.user_search_result)
        self.label_67.setObjectName(u"label_67")
        sizePolicy.setHeightForWidth(self.label_67.sizePolicy().hasHeightForWidth())
        self.label_67.setSizePolicy(sizePolicy)
        self.label_67.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 35px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: rgb(208, 233, 244);\n"
"")

        self.horizontalLayout_14.addWidget(self.label_67)

        self.horizontalLayout_14.setStretch(0, 2)
        self.horizontalLayout_14.setStretch(1, 21)

        self.verticalLayout_37.addLayout(self.horizontalLayout_14)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setSpacing(100)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_68 = QLabel(self.user_search_result)
        self.label_68.setObjectName(u"label_68")
        sizePolicy.setHeightForWidth(self.label_68.sizePolicy().hasHeightForWidth())
        self.label_68.setSizePolicy(sizePolicy)
        self.label_68.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 35px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: rgb(208, 233, 244);\n"
"")
        self.label_68.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_36.addWidget(self.label_68)

        self.another_search = QPushButton(self.user_search_result)
        self.another_search.setObjectName(u"another_search")
        sizePolicy.setHeightForWidth(self.another_search.sizePolicy().hasHeightForWidth())
        self.another_search.setSizePolicy(sizePolicy)
        self.another_search.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.verticalLayout_36.addWidget(self.another_search)

        self.verticalLayout_36.setStretch(0, 5)
        self.verticalLayout_36.setStretch(1, 1)

        self.verticalLayout_37.addLayout(self.verticalLayout_36)

        self.verticalLayout_37.setStretch(0, 1)
        self.verticalLayout_37.setStretch(1, 15)

        self.verticalLayout_35.addLayout(self.verticalLayout_37)


        self.verticalLayout_38.addLayout(self.verticalLayout_35)

        self.stackedWidget.addWidget(self.user_search_result)
        self.sokr_list = QWidget()
        self.sokr_list.setObjectName(u"sokr_list")
        sizePolicy.setHeightForWidth(self.sokr_list.sizePolicy().hasHeightForWidth())
        self.sokr_list.setSizePolicy(sizePolicy)
        self.verticalLayout_42 = QVBoxLayout(self.sokr_list)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.back_7 = QPushButton(self.sokr_list)
        self.back_7.setObjectName(u"back_7")
        sizePolicy.setHeightForWidth(self.back_7.sizePolicy().hasHeightForWidth())
        self.back_7.setSizePolicy(sizePolicy)
        self.back_7.setFont(font1)
        self.back_7.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")
        self.back_7.setIcon(icon)

        self.horizontalLayout_15.addWidget(self.back_7)

        self.label_24 = QLabel(self.sokr_list)
        self.label_24.setObjectName(u"label_24")
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 35px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: rgb(208, 233, 244);\n"
"")

        self.horizontalLayout_15.addWidget(self.label_24)

        self.horizontalLayout_15.setStretch(0, 2)
        self.horizontalLayout_15.setStretch(1, 21)

        self.verticalLayout_41.addLayout(self.horizontalLayout_15)

        self.scrollArea = QScrollArea(self.sokr_list)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"    background-color: rgb(208, 233, 244);\n"
"    border: 2px solid black;\n"
"	border-radius: 7px;\n"
"	padding: 3px\n"
"}\n"
"\n"
"QScrollBar:vertical, QScrollBar:horizontal {\n"
"	background-color: white;\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    border: 2px transparent;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollArea::viewport {\n"
"    padding: 0px;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical, QScrollBar::handle:horizontal {\n"
"		border: 2px solid black;\n"
"   		border-radius: 0px;\n"
"		background-color: #5a8bb8;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover {\n"
"    background-color: #4a7397;\n"
"}\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: lightblue;\n"
"	border:2px solid skyblue;\n"
"	border-radius:0px;\n"
"}\n"
"\n"
"")
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1653, 6448))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setStyleSheet(u"background-color: rgb(208, 233, 244);\n"
"border: none;\n"
"margin: 0px;")
        self.verticalLayout_40 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 9, -1, -1)
        self.widget = QWidget(self.scrollAreaWidgetContents_2)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(0, 0))
        self.widget.setStyleSheet(u"background-color: transparent;\n"
"border:2px transparent;\n"
"border-radius:7px;\n"
"")
        self.verticalLayout_43 = QVBoxLayout(self.widget)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_23 = QLabel(self.widget)
        self.label_23.setObjectName(u"label_23")
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setMinimumSize(QSize(0, 0))
        self.label_23.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 25px;\n"
"border: none;\n"
"background-color: transparent;\n"
"")
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.label_23.setWordWrap(True)

        self.verticalLayout_43.addWidget(self.label_23)


        self.verticalLayout_40.addWidget(self.widget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_41.addWidget(self.scrollArea)

        self.verticalLayout_41.setStretch(0, 1)
        self.verticalLayout_41.setStretch(1, 15)

        self.verticalLayout_39.addLayout(self.verticalLayout_41)


        self.verticalLayout_42.addLayout(self.verticalLayout_39)

        self.stackedWidget.addWidget(self.sokr_list)
        self.feedback_page = QWidget()
        self.feedback_page.setObjectName(u"feedback_page")
        self.verticalLayout_47 = QVBoxLayout(self.feedback_page)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.back_23 = QPushButton(self.feedback_page)
        self.back_23.setObjectName(u"back_23")
        sizePolicy.setHeightForWidth(self.back_23.sizePolicy().hasHeightForWidth())
        self.back_23.setSizePolicy(sizePolicy)
        self.back_23.setFont(font1)
        self.back_23.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")
        self.back_23.setIcon(icon)

        self.horizontalLayout_16.addWidget(self.back_23)

        self.label_69 = QLabel(self.feedback_page)
        self.label_69.setObjectName(u"label_69")
        sizePolicy.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy)
        self.label_69.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 35px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"background-color: rgb(208, 233, 244);\n"
"")
        self.label_69.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_69)

        self.horizontalLayout_16.setStretch(0, 2)
        self.horizontalLayout_16.setStretch(1, 21)

        self.verticalLayout_46.addLayout(self.horizontalLayout_16)

        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_70 = QLabel(self.feedback_page)
        self.label_70.setObjectName(u"label_70")
        sizePolicy.setHeightForWidth(self.label_70.sizePolicy().hasHeightForWidth())
        self.label_70.setSizePolicy(sizePolicy)
        self.label_70.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 35px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: rgb(208, 233, 244);\n"
"")

        self.verticalLayout_45.addWidget(self.label_70)

        self.lineEdit_3 = QLineEdit(self.feedback_page)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setToolTipDuration(-1)
        self.lineEdit_3.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 25px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: rgb(208, 233, 244);\n"
"")

        self.verticalLayout_45.addWidget(self.lineEdit_3)

        self.verticalLayout_45.setStretch(0, 2)
        self.verticalLayout_45.setStretch(1, 5)

        self.verticalLayout_46.addLayout(self.verticalLayout_45)

        self.verticalLayout_46.setStretch(0, 1)
        self.verticalLayout_46.setStretch(1, 15)

        self.verticalLayout_44.addLayout(self.verticalLayout_46)


        self.verticalLayout_47.addLayout(self.verticalLayout_44)

        self.stackedWidget.addWidget(self.feedback_page)
        self.letter_search = QWidget()
        self.letter_search.setObjectName(u"letter_search")
        self.horizontalLayout_22 = QHBoxLayout(self.letter_search)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.back_24 = QPushButton(self.letter_search)
        self.back_24.setObjectName(u"back_24")
        sizePolicy.setHeightForWidth(self.back_24.sizePolicy().hasHeightForWidth())
        self.back_24.setSizePolicy(sizePolicy)
        self.back_24.setFont(font1)
        self.back_24.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")
        self.back_24.setIcon(icon)

        self.horizontalLayout_7.addWidget(self.back_24)

        self.label_72 = QLabel(self.letter_search)
        self.label_72.setObjectName(u"label_72")
        sizePolicy.setHeightForWidth(self.label_72.sizePolicy().hasHeightForWidth())
        self.label_72.setSizePolicy(sizePolicy)
        self.label_72.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 35px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"background-color: rgb(208, 233, 244);\n"
"")
        self.label_72.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_72)

        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 21)

        self.verticalLayout_11.addLayout(self.horizontalLayout_7)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(50)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_71 = QLabel(self.letter_search)
        self.label_71.setObjectName(u"label_71")
        sizePolicy.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy)
        self.label_71.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 35px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: rgb(208, 233, 244);\n"
"")

        self.verticalLayout_3.addWidget(self.label_71)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.letter_19 = QPushButton(self.letter_search)
        self.letter_19.setObjectName(u"letter_19")
        sizePolicy.setHeightForWidth(self.letter_19.sizePolicy().hasHeightForWidth())
        self.letter_19.setSizePolicy(sizePolicy)
        self.letter_19.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_19, 3, 0, 1, 1)

        self.letter_1 = QPushButton(self.letter_search)
        self.letter_1.setObjectName(u"letter_1")
        sizePolicy.setHeightForWidth(self.letter_1.sizePolicy().hasHeightForWidth())
        self.letter_1.setSizePolicy(sizePolicy)
        self.letter_1.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_1, 0, 0, 1, 1)

        self.letter_2 = QPushButton(self.letter_search)
        self.letter_2.setObjectName(u"letter_2")
        sizePolicy.setHeightForWidth(self.letter_2.sizePolicy().hasHeightForWidth())
        self.letter_2.setSizePolicy(sizePolicy)
        self.letter_2.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_2, 0, 1, 1, 1)

        self.letter_3 = QPushButton(self.letter_search)
        self.letter_3.setObjectName(u"letter_3")
        sizePolicy.setHeightForWidth(self.letter_3.sizePolicy().hasHeightForWidth())
        self.letter_3.setSizePolicy(sizePolicy)
        self.letter_3.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_3, 0, 2, 1, 1)

        self.letter_4 = QPushButton(self.letter_search)
        self.letter_4.setObjectName(u"letter_4")
        sizePolicy.setHeightForWidth(self.letter_4.sizePolicy().hasHeightForWidth())
        self.letter_4.setSizePolicy(sizePolicy)
        self.letter_4.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_4, 0, 3, 1, 1)

        self.letter_5 = QPushButton(self.letter_search)
        self.letter_5.setObjectName(u"letter_5")
        sizePolicy.setHeightForWidth(self.letter_5.sizePolicy().hasHeightForWidth())
        self.letter_5.setSizePolicy(sizePolicy)
        self.letter_5.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_5, 0, 4, 1, 1)

        self.letter_6 = QPushButton(self.letter_search)
        self.letter_6.setObjectName(u"letter_6")
        sizePolicy.setHeightForWidth(self.letter_6.sizePolicy().hasHeightForWidth())
        self.letter_6.setSizePolicy(sizePolicy)
        self.letter_6.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_6, 0, 5, 1, 1)

        self.letter_20 = QPushButton(self.letter_search)
        self.letter_20.setObjectName(u"letter_20")
        sizePolicy.setHeightForWidth(self.letter_20.sizePolicy().hasHeightForWidth())
        self.letter_20.setSizePolicy(sizePolicy)
        self.letter_20.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_20, 3, 1, 1, 1)

        self.letter_7 = QPushButton(self.letter_search)
        self.letter_7.setObjectName(u"letter_7")
        sizePolicy.setHeightForWidth(self.letter_7.sizePolicy().hasHeightForWidth())
        self.letter_7.setSizePolicy(sizePolicy)
        self.letter_7.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_7, 1, 0, 1, 1)

        self.letter_13 = QPushButton(self.letter_search)
        self.letter_13.setObjectName(u"letter_13")
        sizePolicy.setHeightForWidth(self.letter_13.sizePolicy().hasHeightForWidth())
        self.letter_13.setSizePolicy(sizePolicy)
        self.letter_13.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_13, 2, 0, 1, 1)

        self.letter_8 = QPushButton(self.letter_search)
        self.letter_8.setObjectName(u"letter_8")
        sizePolicy.setHeightForWidth(self.letter_8.sizePolicy().hasHeightForWidth())
        self.letter_8.setSizePolicy(sizePolicy)
        self.letter_8.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_8, 1, 1, 1, 1)

        self.letter_14 = QPushButton(self.letter_search)
        self.letter_14.setObjectName(u"letter_14")
        sizePolicy.setHeightForWidth(self.letter_14.sizePolicy().hasHeightForWidth())
        self.letter_14.setSizePolicy(sizePolicy)
        self.letter_14.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_14, 2, 1, 1, 1)

        self.letter_9 = QPushButton(self.letter_search)
        self.letter_9.setObjectName(u"letter_9")
        sizePolicy.setHeightForWidth(self.letter_9.sizePolicy().hasHeightForWidth())
        self.letter_9.setSizePolicy(sizePolicy)
        self.letter_9.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_9, 1, 2, 1, 1)

        self.letter_10 = QPushButton(self.letter_search)
        self.letter_10.setObjectName(u"letter_10")
        sizePolicy.setHeightForWidth(self.letter_10.sizePolicy().hasHeightForWidth())
        self.letter_10.setSizePolicy(sizePolicy)
        self.letter_10.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_10, 1, 3, 1, 1)

        self.letter_11 = QPushButton(self.letter_search)
        self.letter_11.setObjectName(u"letter_11")
        sizePolicy.setHeightForWidth(self.letter_11.sizePolicy().hasHeightForWidth())
        self.letter_11.setSizePolicy(sizePolicy)
        self.letter_11.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_11, 1, 4, 1, 1)

        self.letter_12 = QPushButton(self.letter_search)
        self.letter_12.setObjectName(u"letter_12")
        sizePolicy.setHeightForWidth(self.letter_12.sizePolicy().hasHeightForWidth())
        self.letter_12.setSizePolicy(sizePolicy)
        self.letter_12.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_12, 1, 5, 1, 1)

        self.letter_15 = QPushButton(self.letter_search)
        self.letter_15.setObjectName(u"letter_15")
        sizePolicy.setHeightForWidth(self.letter_15.sizePolicy().hasHeightForWidth())
        self.letter_15.setSizePolicy(sizePolicy)
        self.letter_15.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_15, 2, 2, 1, 1)

        self.letter_16 = QPushButton(self.letter_search)
        self.letter_16.setObjectName(u"letter_16")
        sizePolicy.setHeightForWidth(self.letter_16.sizePolicy().hasHeightForWidth())
        self.letter_16.setSizePolicy(sizePolicy)
        self.letter_16.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_16, 2, 3, 1, 1)

        self.letter_17 = QPushButton(self.letter_search)
        self.letter_17.setObjectName(u"letter_17")
        sizePolicy.setHeightForWidth(self.letter_17.sizePolicy().hasHeightForWidth())
        self.letter_17.setSizePolicy(sizePolicy)
        self.letter_17.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_17, 2, 4, 1, 1)

        self.letter_18 = QPushButton(self.letter_search)
        self.letter_18.setObjectName(u"letter_18")
        sizePolicy.setHeightForWidth(self.letter_18.sizePolicy().hasHeightForWidth())
        self.letter_18.setSizePolicy(sizePolicy)
        self.letter_18.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_18, 2, 5, 1, 1)

        self.letter_21 = QPushButton(self.letter_search)
        self.letter_21.setObjectName(u"letter_21")
        sizePolicy.setHeightForWidth(self.letter_21.sizePolicy().hasHeightForWidth())
        self.letter_21.setSizePolicy(sizePolicy)
        self.letter_21.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_21, 3, 2, 1, 1)

        self.letter_22 = QPushButton(self.letter_search)
        self.letter_22.setObjectName(u"letter_22")
        sizePolicy.setHeightForWidth(self.letter_22.sizePolicy().hasHeightForWidth())
        self.letter_22.setSizePolicy(sizePolicy)
        self.letter_22.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_22, 3, 3, 1, 1)

        self.letter_23 = QPushButton(self.letter_search)
        self.letter_23.setObjectName(u"letter_23")
        sizePolicy.setHeightForWidth(self.letter_23.sizePolicy().hasHeightForWidth())
        self.letter_23.setSizePolicy(sizePolicy)
        self.letter_23.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_23, 3, 4, 1, 1)

        self.letter_24 = QPushButton(self.letter_search)
        self.letter_24.setObjectName(u"letter_24")
        sizePolicy.setHeightForWidth(self.letter_24.sizePolicy().hasHeightForWidth())
        self.letter_24.setSizePolicy(sizePolicy)
        self.letter_24.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_24, 3, 5, 1, 1)

        self.letter_25 = QPushButton(self.letter_search)
        self.letter_25.setObjectName(u"letter_25")
        sizePolicy.setHeightForWidth(self.letter_25.sizePolicy().hasHeightForWidth())
        self.letter_25.setSizePolicy(sizePolicy)
        self.letter_25.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_25, 4, 0, 1, 1)

        self.letter_26 = QPushButton(self.letter_search)
        self.letter_26.setObjectName(u"letter_26")
        sizePolicy.setHeightForWidth(self.letter_26.sizePolicy().hasHeightForWidth())
        self.letter_26.setSizePolicy(sizePolicy)
        self.letter_26.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_26, 4, 1, 1, 1)

        self.letter_27 = QPushButton(self.letter_search)
        self.letter_27.setObjectName(u"letter_27")
        sizePolicy.setHeightForWidth(self.letter_27.sizePolicy().hasHeightForWidth())
        self.letter_27.setSizePolicy(sizePolicy)
        self.letter_27.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_27, 4, 2, 1, 1)

        self.letter_28 = QPushButton(self.letter_search)
        self.letter_28.setObjectName(u"letter_28")
        sizePolicy.setHeightForWidth(self.letter_28.sizePolicy().hasHeightForWidth())
        self.letter_28.setSizePolicy(sizePolicy)
        self.letter_28.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_28, 4, 3, 1, 1)

        self.letter_29 = QPushButton(self.letter_search)
        self.letter_29.setObjectName(u"letter_29")
        sizePolicy.setHeightForWidth(self.letter_29.sizePolicy().hasHeightForWidth())
        self.letter_29.setSizePolicy(sizePolicy)
        self.letter_29.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_29, 4, 4, 1, 1)

        self.letter_30 = QPushButton(self.letter_search)
        self.letter_30.setObjectName(u"letter_30")
        sizePolicy.setHeightForWidth(self.letter_30.sizePolicy().hasHeightForWidth())
        self.letter_30.setSizePolicy(sizePolicy)
        self.letter_30.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_30, 4, 5, 1, 1)

        self.letter_31 = QPushButton(self.letter_search)
        self.letter_31.setObjectName(u"letter_31")
        sizePolicy.setHeightForWidth(self.letter_31.sizePolicy().hasHeightForWidth())
        self.letter_31.setSizePolicy(sizePolicy)
        self.letter_31.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_31, 5, 0, 1, 1)

        self.letter_32 = QPushButton(self.letter_search)
        self.letter_32.setObjectName(u"letter_32")
        sizePolicy.setHeightForWidth(self.letter_32.sizePolicy().hasHeightForWidth())
        self.letter_32.setSizePolicy(sizePolicy)
        self.letter_32.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_32, 5, 1, 1, 1)

        self.letter_33 = QPushButton(self.letter_search)
        self.letter_33.setObjectName(u"letter_33")
        sizePolicy.setHeightForWidth(self.letter_33.sizePolicy().hasHeightForWidth())
        self.letter_33.setSizePolicy(sizePolicy)
        self.letter_33.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.gridLayout_2.addWidget(self.letter_33, 5, 2, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout_2.setRowStretch(3, 1)
        self.gridLayout_2.setRowStretch(4, 1)
        self.gridLayout_2.setRowStretch(5, 1)

        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 7)

        self.verticalLayout_11.addLayout(self.verticalLayout_3)

        self.verticalLayout_11.setStretch(0, 1)
        self.verticalLayout_11.setStretch(1, 15)

        self.verticalLayout.addLayout(self.verticalLayout_11)


        self.horizontalLayout_22.addLayout(self.verticalLayout)

        self.stackedWidget.addWidget(self.letter_search)
        self.letter_search_words = QWidget()
        self.letter_search_words.setObjectName(u"letter_search_words")
        self.verticalLayout_55 = QVBoxLayout(self.letter_search_words)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_52 = QVBoxLayout()
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_54 = QVBoxLayout()
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.back_25 = QPushButton(self.letter_search_words)
        self.back_25.setObjectName(u"back_25")
        sizePolicy.setHeightForWidth(self.back_25.sizePolicy().hasHeightForWidth())
        self.back_25.setSizePolicy(sizePolicy)
        self.back_25.setFont(font1)
        self.back_25.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")
        self.back_25.setIcon(icon)

        self.horizontalLayout_21.addWidget(self.back_25)

        self.label_74 = QLabel(self.letter_search_words)
        self.label_74.setObjectName(u"label_74")
        sizePolicy.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy)
        self.label_74.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 35px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"background-color: rgb(208, 233, 244);\n"
"")
        self.label_74.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_74)

        self.horizontalLayout_21.setStretch(0, 2)
        self.horizontalLayout_21.setStretch(1, 21)

        self.verticalLayout_54.addLayout(self.horizontalLayout_21)

        self.verticalLayout_53 = QVBoxLayout()
        self.verticalLayout_53.setSpacing(50)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.label_73 = QLabel(self.letter_search_words)
        self.label_73.setObjectName(u"label_73")
        sizePolicy.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy)
        self.label_73.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 35px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: rgb(208, 233, 244);\n"
"")

        self.verticalLayout_53.addWidget(self.label_73)

        self.list_words = QListWidget(self.letter_search_words)
        self.list_words.setObjectName(u"list_words")
        self.list_words.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 35px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"background-color: rgb(208, 233, 244);\n"
"")

        self.verticalLayout_53.addWidget(self.list_words)

        self.verticalLayout_53.setStretch(0, 1)
        self.verticalLayout_53.setStretch(1, 7)

        self.verticalLayout_54.addLayout(self.verticalLayout_53)

        self.verticalLayout_54.setStretch(0, 1)
        self.verticalLayout_54.setStretch(1, 15)

        self.verticalLayout_52.addLayout(self.verticalLayout_54)


        self.verticalLayout_55.addLayout(self.verticalLayout_52)

        self.stackedWidget.addWidget(self.letter_search_words)
        self.letter_search_result = QWidget()
        self.letter_search_result.setObjectName(u"letter_search_result")
        self.verticalLayout_58 = QVBoxLayout(self.letter_search_result)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_51 = QVBoxLayout()
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_57 = QVBoxLayout()
        self.verticalLayout_57.setSpacing(50)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.back_26 = QPushButton(self.letter_search_result)
        self.back_26.setObjectName(u"back_26")
        sizePolicy.setHeightForWidth(self.back_26.sizePolicy().hasHeightForWidth())
        self.back_26.setSizePolicy(sizePolicy)
        self.back_26.setFont(font1)
        self.back_26.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")
        self.back_26.setIcon(icon)

        self.horizontalLayout_8.addWidget(self.back_26)

        self.label_75 = QLabel(self.letter_search_result)
        self.label_75.setObjectName(u"label_75")
        sizePolicy.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy)
        self.label_75.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 35px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"background-color: rgb(208, 233, 244);\n"
"")
        self.label_75.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_75)

        self.horizontalLayout_8.setStretch(0, 2)
        self.horizontalLayout_8.setStretch(1, 21)

        self.verticalLayout_57.addLayout(self.horizontalLayout_8)

        self.verticalLayout_56 = QVBoxLayout()
        self.verticalLayout_56.setSpacing(50)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(-1, -1, -1, 0)
        self.label_76 = QLabel(self.letter_search_result)
        self.label_76.setObjectName(u"label_76")
        sizePolicy.setHeightForWidth(self.label_76.sizePolicy().hasHeightForWidth())
        self.label_76.setSizePolicy(sizePolicy)
        self.label_76.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 25px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"background-color: rgb(208, 233, 244);\n"
"")
        self.label_76.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.label_76.setWordWrap(True)

        self.verticalLayout_56.addWidget(self.label_76)

        self.another_search_2 = QPushButton(self.letter_search_result)
        self.another_search_2.setObjectName(u"another_search_2")
        sizePolicy.setHeightForWidth(self.another_search_2.sizePolicy().hasHeightForWidth())
        self.another_search_2.setSizePolicy(sizePolicy)
        self.another_search_2.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.verticalLayout_56.addWidget(self.another_search_2)

        self.verticalLayout_56.setStretch(0, 5)
        self.verticalLayout_56.setStretch(1, 1)

        self.verticalLayout_57.addLayout(self.verticalLayout_56)

        self.verticalLayout_57.setStretch(0, 1)
        self.verticalLayout_57.setStretch(1, 15)

        self.verticalLayout_51.addLayout(self.verticalLayout_57)


        self.verticalLayout_58.addLayout(self.verticalLayout_51)

        self.stackedWidget.addWidget(self.letter_search_result)
        self.stats = QWidget()
        self.stats.setObjectName(u"stats")
        self.verticalLayout_61 = QVBoxLayout(self.stats)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_60 = QVBoxLayout()
        self.verticalLayout_60.setSpacing(50)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.back_27 = QPushButton(self.stats)
        self.back_27.setObjectName(u"back_27")
        sizePolicy.setHeightForWidth(self.back_27.sizePolicy().hasHeightForWidth())
        self.back_27.setSizePolicy(sizePolicy)
        self.back_27.setFont(font1)
        self.back_27.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")
        self.back_27.setIcon(icon)

        self.horizontalLayout_17.addWidget(self.back_27)

        self.label_77 = QLabel(self.stats)
        self.label_77.setObjectName(u"label_77")
        sizePolicy.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy)
        self.label_77.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 35px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"background-color: rgb(208, 233, 244);\n"
"")
        self.label_77.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_77)

        self.horizontalLayout_17.setStretch(0, 2)
        self.horizontalLayout_17.setStretch(1, 21)

        self.verticalLayout_60.addLayout(self.horizontalLayout_17)

        self.verticalLayout_59 = QVBoxLayout()
        self.verticalLayout_59.setSpacing(50)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(350, -1, 350, 50)
        self.label_9 = QLabel(self.stats)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setStyleSheet(u"color: black;\n"
"font-weight: bold;\n"
"font-size: 40px;\n"
"border: 2px solid black;\n"
"border-radius: 7px;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: rgb(208, 233, 244);\n"
"")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_59.addWidget(self.label_9)

        self.reset_stats = QPushButton(self.stats)
        self.reset_stats.setObjectName(u"reset_stats")
        self.reset_stats.setStyleSheet(u"QPushButton {\n"
"                color: black;\n"
"                font-weight: bold;\n"
"                font-size:35px;\n"
"                background-color: rgb(208, 233, 244);\n"
"                border: 2px solid black;\n"
"                border-radius: 7px;\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #d0dff4;\n"
"            } \n"
"			QPushButton:pressed {\n"
"            	background-color: #1f6391;\n"
"        }")

        self.verticalLayout_59.addWidget(self.reset_stats)


        self.verticalLayout_60.addLayout(self.verticalLayout_59)

        self.verticalLayout_60.setStretch(0, 1)
        self.verticalLayout_60.setStretch(1, 15)

        self.verticalLayout_5.addLayout(self.verticalLayout_60)


        self.verticalLayout_61.addLayout(self.verticalLayout_5)

        self.stackedWidget.addWidget(self.stats)

        self.horizontalLayout_9.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(7)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c \u0432 \u0438\u0433\u0440\u0443\n"
"\u041f\u0435\u0440\u0435\u0432\u043e\u0434\u0447\u0438\u043a \u0441 \u0440\u0443\u0441\u0441\u043a\u043e\u0433\u043e \u043d\u0430 \u0440\u0443\u0441\u0441\u043a\u0438\u0439!", None))
        self.label_13.setText("")
        self.btn_gamemodes_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c\u044b \u0438\u0433\u0440\u044b", None))
        self.label_14.setText("")
        self.btn_dictionary_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0432\u0430\u0440\u044c", None))
        self.label_7.setText("")
        self.btn_stats.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.label_12.setText("")
        self.btn_feedback_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u043e\u0442\u0437\u044b\u0432", None))
        self.back_3.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c\u044b \u0438\u0433\u0440\u044b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0440\u0435\u0436\u0438\u043c \u0438\u0433\u0440\u044b", None))
        self.btn_easymode.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u0438\u0433\u0440\u0430", None))
        self.btn_hardmode.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0436\u043d\u0430\u044f \u0438\u0433\u0440\u0430", None))
        self.back_4.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u0438\u0433\u0440\u0430", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0420\u0430\u0443\u043d\u0434</p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icon/icons/heart2.svg\"/>\u0416\u0438\u0437\u043d\u0438 </p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435, \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0435\u0435 \u0441\u043b\u043e\u0432\u0443", None))
        self.easy_answer2.setText("")
        self.easy_answer1.setText("")
        self.easy_answer3.setText("")
        self.back_5.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0436\u043d\u0430\u044f \u0438\u0433\u0440\u0430", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0420\u0430\u0443\u043d\u0434</p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icon/icons/heart2.svg\"/>\u0416\u0438\u0437\u043d\u0438 </p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 1 \u043b\u044e\u0431\u043e\u0439 \u0441\u0438\u043d\u043e\u043d\u0438\u043c, \u043f\u043e\u0434\u0445\u043e\u0434\u044f\u0449\u0438\u0439 \u043a \u0441\u043b\u043e\u0432\u0443", None))
        self.lineEdit.setText("")
        self.back_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0432\u0430\u0440\u044c", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u043d\u0442\u0435\u0440\u0435\u0441\u0443\u044e\u0449\u0443\u044e \u0432\u0430\u0441 \u0444\u0443\u043d\u043a\u0446\u0438\u044e", None))
        self.btn_user_search.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0439 \u0432\u0432\u043e\u0434", None))
        self.btn_po_bukvam.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0431\u0443\u043a\u0432\u0430\u043c", None))
        self.btn_sokr_list.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u0438\u0439", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0430\u0441\u0438\u0431\u043e \u0437\u0430 \u0432\u0430\u0448 \u043e\u0442\u0437\u044b\u0432!", None))
        self.back_30.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432 \u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0433\u0440\u0430 \u0437\u0430\u043a\u043e\u043d\u0447\u0435\u043d\u0430!\n"
"\u0412\u044b \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e \u043e\u0442\u0432\u0435\u0442\u0438\u043b\u0438 \u043d\u0430 7 \u0438\u0437 10 \u0432\u043e\u043f\u0440\u043e\u0441\u043e\u0432", None))
        self.back_1.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432 \u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.back_6.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0439 \u0432\u0432\u043e\u0434", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043d\u0442\u0435\u0440\u0435\u0441\u0443\u044e\u0449\u0435\u0435 \u0432\u0430\u0441 \u0441\u043b\u043e\u0432\u043e", None))
        self.lineEdit_2.setText("")
        self.back_22.setText("")
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0439 \u0432\u0432\u043e\u0434", None))
        self.label_68.setText("")
        self.another_search.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438 \u0434\u0440\u0443\u0433\u043e\u0435 \u0441\u043b\u043e\u0432\u043e", None))
        self.back_7.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u0438\u0439", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u0430\u0432\u0438\u0430. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0430\u0432\u0438\u0430\u0446\u0438\u0438\n"
"\n"
"\u0430\u0432\u0442\u043e. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044c\u043d\u043e\u0433\u043e \u0434\u0435\u043b\u0430\n"
"\n"
"\u0430\u043c\u0435\u0440.  \u2013 \u0430\u043c\u0435\u0440\u0438\u043a\u0430\u043d\u0441\u043a\u0438\u0439.\n"
"\n"
"\u0430\u043d\u0433\u043b. \u2013 \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439 \u044f\u0437\u044b\u043a\n"
"\n"
"\u0430\u043d\u0438\u043c. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0430\u043d\u0438\u043c\u0435\n"
"\n"
"\u0430\u043d\u0442\u0440. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0430\u043d\u0442\u0440\u043e\u043f\u043e\u043b\u043e\u0433\u0438\u0438\n"
"\n"
"\u0430\u0440\u0445\u0435\u043e\u043b. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0430\u0440\u0445\u0435\u043e\u043b\u043e\u0433\u0438\u0438\n"
"\n"
"\u0430\u0440\u0445\u0438\u0442. \u2013 \u0442\u0435\u0440"
                        "\u043c\u0438\u043d \u0430\u0440\u0445\u0438\u0442\u0435\u043a\u0442\u0443\u0440\u044b\n"
"\n"
"\u0430\u0441\u0442\u0440\u043e\u043d. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0430\u0441\u0442\u0440\u043e\u043d\u043e\u043c\u0438\u0438\n"
"\n"
"\u0431\u0438\u0437. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0431\u0438\u0437\u043d\u0435\u0441\u0430\n"
"\n"
"\u0431\u0438\u043e\u043b. -  \u0442\u0435\u0440\u043c\u0438\u043d \u0431\u0438\u043e\u043b\u043e\u0433\u0438\u0438\n"
"\n"
"\u0431\u0438\u043e\u0445. - \u0442\u0435\u0440\u043c\u0438\u043d \u0431\u0438\u043e\u0445\u0438\u043c\u0438\u0438\n"
"\n"
"\u0431\u043e\u0442. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0431\u043e\u0442\u0430\u043d\u0438\u043a\u0438\n"
"\n"
"\u0431\u0442\u0445. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0431\u0438\u043e\u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0439\n"
"\n"
"\u0432\u043e\u0435\u043d. \u2013 \u0432\u043e\u0435\u043d\u043d\u044b\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u0433\u0435\u043d."
                        " \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0433\u0435\u043d\u0435\u0442\u0438\u043a\u0438\n"
"\n"
"\u0433\u0435\u043e\u0433\u0440. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0433\u0435\u043e\u0433\u0440\u0430\u0444\u0438\u0438\n"
"\n"
"\u0433\u0435\u043e\u0434. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0433\u0435\u043e\u0434\u0435\u0437\u0438\u0438\n"
"\n"
"\u0433\u0435\u043e\u043b. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0433\u0435\u043e\u043b\u043e\u0433\u0438\u0438\n"
"\n"
"\u0433\u0440\u0430\u0444. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0433\u0440\u0430\u0444\u0438\u043a\u0438\n"
"\n"
"\u0433\u0440\u0435\u0447. \u2013 \u0434\u0440\u0435\u0432\u043d\u0435\u0433\u0440\u0435\u0447\u0435\u0441\u043a\u0438\u0439 \u044f\u0437\u044b\u043a\n"
"\n"
"\u0434\u0438\u043f\u043b. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0434\u0438\u043f\u043b\u043e\u043c\u0430\u0442\u0438\u0438\n"
"\n"
"\u0434\u0440. \u2013 \u0434\u0440\u0443\u0433\u0438\u0435\n"
"\n"
"\u0435\u0434. \u2013 \u0435\u0434\u0438"
                        "\u043d\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0435 \u0447\u0438\u0441\u043b\u043e\n"
"\n"
"\u0436.-\u0434. - \u0436\u0435\u043b\u0435\u0437\u043d\u043e\u0434\u043e\u0440\u043e\u0436\u043d\u044b\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u0437\u043e\u043e\u043b. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0437\u043e\u043e\u043b\u043e\u0433\u0438\u0438\n"
"\n"
"\u0438\u0433\u0440. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0438\u0433\u0440\n"
"\n"
"\u0438\u0437\u0434. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0438\u0437\u0434\u0430\u0442\u0435\u043b\u044c\u0441\u043a\u043e\u0433\u043e \u0434\u0435\u043b\u0430\n"
"\n"
"\u0438\u0437\u043c. \u2013 \u043c\u0435\u0440\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f\n"
"\n"
"\u0438\u043d\u0442\u0435\u0440\u043d. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0438\u043d\u0442\u0435\u0440\u043d\u0435\u0442\u0430\n"
"\n"
"\u0438\u043d\u0444. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438"
                        "\u043a\u0438\n"
"\n"
"\u0438\u0441\u043a. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0438\u0441\u043a\u0443\u0441\u0441\u0442\u0432\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f\n"
"\n"
"\u0438\u0441\u0442. \u2013 \u0438\u0441\u0442\u043e\u0440\u0438\u0437\u043c, \u0442\u0435\u0440\u043c\u0438\u043d \u0438\u0441\u0442\u043e\u0440\u0438\u0438\n"
"\n"
"\u043a\u0430\u0437. - \u0442\u0435\u0440\u043c\u0438\u043d \u043a\u0430\u0437\u0438\u043d\u043e\n"
"\n"
"\u043a\u0430\u043d\u0446. \u2013 \u043a\u0430\u043d\u0446\u0435\u043b\u044f\u0440\u0441\u043a\u0438\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u043a\u0438\u0431\u0435\u0440. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u043a\u0438\u0431\u0435\u0440\u043d\u0435\u0442\u0438\u043a\u0438\n"
"\n"
"\u043a\u0438\u043d\u043e. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u043a\u0438\u043d\u043e\u0438\u0441\u043a\u0443\u0441\u0441\u0442\u0432\u0430\n"
"\n"
"\u043a\u043e\u043c.  - \u043a\u043e\u043c\u043c\u0435\u0440\u0447\u0435\u0441\u043a\u0438\u0439 \u0442"
                        "\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u043a\u043e\u043c\u043f. \u2013 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043d\u044b\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u043a\u043e\u043c\u043f. \u0441\u043b\u0435\u043d\u0433 \u2013 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043d\u044b\u0439 \u0441\u043b\u0435\u043d\u0433\n"
"\n"
"\u043a\u043e\u0441\u043c. - \u043a\u043e\u0441\u043c\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u043a\u043e\u0441\u043c\u0435\u0442. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u043a\u043e\u0441\u043c\u0435\u0442\u043e\u043b\u043e\u0433\u0438\u0438\n"
"\n"
"\u043b\u0430\u0442. \u2013 \u043b\u0430\u0442\u0438\u043d\u0441\u043a\u0438\u0439 \u044f\u0437\u044b\u043a\n"
"\n"
"\u043b\u0438\u043d\u0433\u0432. \u2013 \u043b\u0438\u043d\u0433\u0432\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u043b\u0438\u0442. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d"
                        " \u043b\u0438\u0442\u0435\u0440\u0430\u0442\u0443\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f\n"
"\n"
"\u043c\u0430\u0440\u043a. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u043c\u0430\u0440\u043a\u0435\u0442\u0438\u043d\u0433\u0430\n"
"\n"
"\u043c\u0430\u0442. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0438\n"
"\n"
"\u043c\u0430\u0442\u0435\u0440. \u2013 \u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u043e\u0432\n"
"\n"
"\u043c\u0435\u0434. \u2013 \u043c\u0435\u0434\u0438\u0446\u0438\u043d\u0441\u043a\u0438\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u043c\u0435\u0442\u0430\u043b. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u043c\u0435\u0442\u0430\u043b\u043b\u0443\u0440\u0433\u0438\u0438\n"
"\n"
"\u043c\u0435\u0442\u0435\u043e. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u043c\u0435\u0442\u0435\u043e\u0440\u043e\u043b\u043e\u0433\u0438\u0438\n"
"\n"
"\u043c"
                        "\u0438\u043d\u0435\u0440. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u043c\u0438\u043d\u0435\u0440\u0430\u043b\u043e\u0433\u0438\u0438\n"
"\n"
"\u043c\u043d. -  \u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0435 \u0447\u0438\u0441\u043b\u043e\n"
"\n"
"\u043c\u043e\u0434. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u043c\u043e\u0434\u044b\n"
"\n"
"\u043c\u043e\u043b. \u0441\u043b\u0435\u043d\u0433. \u2013 \u043c\u043e\u043b\u043e\u0434\u0435\u0436\u043d\u044b\u0439 \u0441\u043b\u0435\u043d\u0433\n"
"\n"
"\u043c\u043e\u0440. \u2013 \u043c\u043e\u0440\u0441\u043a\u043e\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u043c\u0443\u0437. \u2013 \u043c\u0443\u0437\u044b\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u043c\u0443\u0437. \u0441\u043b\u0435\u043d\u0433 \u2013 \u043c\u0443\u0437\u044b\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u043b\u0435\u043d\u0433\n"
"\n"
"\u043d\u0430\u043f\u0440. \u2013 \u043d\u0430\u043f\u0440\u0438\u043c"
                        "\u0435\u0440\n"
"\n"
"\u043d\u0435\u0438\u0437\u043c. \u2013 \u043d\u0435\u0438\u0437\u043c\u0435\u043d\u044f\u0435\u043c\u0430\u044f \u0447\u0430\u0441\u0442\u044c \u0440\u0435\u0447\u0438\n"
"\n"
"\u043d\u0435\u043c. \u2013 \u043d\u0435\u043c\u0435\u0446\u043a\u0438\u0439 \u044f\u0437\u044b\u043a\n"
"\n"
"\u043d\u0435\u0434\u0435\u0440\u043b. \u2013 \u043d\u0438\u0434\u0435\u0440\u043b\u0430\u043d\u0434\u0441\u043a\u0438\u0439 \u044f\u0437\u044b\u043a\n"
"\n"
"\u043d\u0435\u0441\u043a\u043b. \u2013 \u043d\u0435\u0441\u043a\u043b\u043e\u043d\u044f\u0435\u043c\u043e\u0435 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0435\n"
"\n"
"\u043d\u0435\u0444\u0442. \u2013 \u043d\u0435\u0444\u0442\u0435\u0433\u0430\u0437\u043e\u0432\u044b\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u043e\u0431\u0440. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u044f\n"
"\n"
"\u043e\u0431\u0449. \u2013 \u043e\u0431\u0449\u0435\u0443"
                        "\u043f\u043e\u0442\u0440\u0435\u0431\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0435 \u0441\u043b\u043e\u0432\u043e\n"
"\n"
"\u043e\u043f\u0442. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u043e\u043f\u0442\u0438\u043a\u0438\n"
"\n"
"\u043f\u0430\u0434. \u2013 \u043f\u0430\u0434\u0435\u0436\n"
"\n"
"\u043f\u0435\u0440\u0435\u043d.  \u2013 \u043f\u0435\u0440\u0435\u043d\u043e\u0441\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435\n"
"\n"
"\u043f\u0438\u0449. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u043f\u0438\u0449\u0435\u0432\u043e\u0439 \u043f\u0440\u043e\u043c\u044b\u0448\u043b\u0435\u043d\u043d\u043e\u0441\u0442\u0438\n"
"\n"
"\u043f\u043e\u043b\u0438\u0433\u0440. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u043f\u043e\u043b\u0438\u0433\u0440\u0430\u0444\u0438\u0438\n"
"\n"
"\u043f\u043e\u043b\u0438\u0442. \u2013 \u043f\u043e\u043b\u0438\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u043f\u0441\u0438\u0445. \u2013 \u0442\u0435\u0440\u043c"
                        "\u0438\u043d \u043f\u0441\u0438\u0445\u043e\u043b\u043e\u0433\u0438\u0438\n"
"\n"
"\u043f\u0443\u0442. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u043f\u0443\u0442\u0435\u0448\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u0438\u043a\u0430\n"
"\n"
"\u0440\u0430\u0434. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0440\u0430\u0434\u0438\u043e\u0442\u0435\u0445\u043d\u0438\u043a\u0438\n"
"\n"
"\u0440\u0430\u0437\u0433. \u2013 \u0440\u0430\u0437\u0433\u043e\u0432\u043e\u0440\u043d\u043e\u0435 \u0441\u043b\u043e\u0432\u043e\n"
"\n"
"\u0440\u0435\u0434\u043a. \u2013 \u0440\u0435\u0434\u043a\u043e \u0443\u043f\u043e\u0442\u0440\u0435\u0431\u043b\u044f\u0435\u043c\u043e\u0435 \u0441\u043b\u043e\u0432\u043e\n"
"\n"
"\u0440\u0435\u043a\u043b. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0440\u0435\u043a\u043b\u0430\u043c\u044b\n"
"\n"
"\u0440\u0435\u043b. \u2013 \u0440\u0435\u043b\u0438\u0433\u0438\u043e\u0437\u043d\u044b\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u0440\u0443\u0441. \u2013 \u0440\u0443\u0441\u0441"
                        "\u043a\u0438\u0439 \u044f\u0437\u044b\u043a\n"
"\n"
"\u0440\u044b\u0431. \u2013 \u0440\u044b\u0431\u043e\u043b\u043e\u0432\u043d\u044b\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u0441.-\u0445. \u2013 \u0441\u0435\u043b\u044c\u0441\u043a\u043e\u0445\u043e\u0437\u044f\u0439\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u0441\u0435\u043a\u0441. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0441\u0435\u043a\u0441\u0430\n"
"\n"
"\u0441\u043c. \u2013 \u0441\u043c\u043e\u0442\u0440\u0438(\u0442\u0435)\n"
"\n"
"\u0441\u043e\u043a\u0440. \u2013 \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u0438\u0435, \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u044b\u0439\n"
"\n"
"\u0441\u043e\u0446. \u2013 \u0441\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u0441\u043f\u0435\u0446. \u2013 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u0441"
                        "\u043f\u043e\u0440\u0442 \u2013 \u0441\u043f\u043e\u0440\u0442\u0438\u0432\u043d\u044b\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u0441\u0440.  \u2013 \u0441\u0440\u0430\u0432\u043d\u0438\u0442\u0435\n"
"\n"
"\u0441\u0442\u0440. \u2013 \u0441\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u0441\u0442\u0440\u0430\u0445. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0441\u0442\u0440\u0430\u0445\u043e\u0432\u043e\u0433\u043e \u0434\u0435\u043b\u0430\n"
"\n"
"\u0442\u0430\u043c. - \u0442\u0430\u043c\u043e\u0436\u0435\u043d\u043d\u044b\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u0442\u0435\u043a\u0441\u0442. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0442\u0435\u043a\u0441\u0442\u0438\u043b\u044c\u043d\u043e\u0439 \u043f\u0440\u043e\u043c\u044b\u0448\u043b\u0435\u043d\u043d\u043e\u0441\u0442\u0438\n"
"\n"
"\u0442\u0435\u0445. \u2013 \u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0442\u0435\u0440\u043c\u0438"
                        "\u043d\n"
"\n"
"\u0442\u0438\u043f\u043e\u0433\u0440. \u2013 \u0442\u0438\u043f\u043e\u0433\u0440\u0430\u0444\u0441\u043a\u0438\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u0442\u043b\u0432. \u2013 \u0442\u0435\u043b\u0435\u0432\u0438\u0437\u0438\u043e\u043d\u043d\u044b\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u0442\u0440\u0430\u043d\u0441\u043f. \u2013 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043d\u044b\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u0443\u043c\u0435\u043d\u044c\u0448. \u2013 \u0443\u043c\u0435\u043d\u044c\u0448\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0435\n"
"\n"
"\u0443\u0441\u0442\u0430\u0440. \u2013 \u0443\u0441\u0442\u0430\u0440\u0435\u0432\u0448\u0435\u0435 \u0441\u043b\u043e\u0432\u043e (\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435)\n"
"\n"
"\u0444\u0430\u043d\u0442. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0444\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0438\n"
"\n"
"\u0444\u0438\u0437. \u2013 \u0444\u0438\u0437\u0438\u0447\u0435"
                        "\u0441\u043a\u0438\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u0444\u0438\u043b\u043e\u0441. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0444\u0438\u043b\u043e\u0441\u043e\u0444\u0438\u0438\n"
"\n"
"\u0444\u0438\u043d. \u2013 \u0444\u0438\u043d\u0430\u043d\u0441\u043e\u0432\u044b\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u0444\u043e\u0442. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u0444\u043e\u0442\u043e\u0434\u0435\u043b\u0430\n"
"\n"
"\u0444\u0440. \u2013 \u0444\u0440\u0430\u043d\u0446\u0443\u0437\u0441\u043a\u0438\u0439 \u044f\u0437\u044b\u043a, \u0444\u0440\u0430\u043d\u0446\u0443\u0437\u0441\u043a\u0438\u0439\n"
"\n"
"\u0445\u0438\u043c. \u2013 \u0445\u0438\u043c\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u0447\u0430\u0441\u0442. \u2013 \u0447\u0430\u0441\u0442\u043e \u0443\u043f\u043e\u0442\u0440\u0435\u0431\u043b\u044f\u0435\u043c\u044b\u0439\n"
"\n"
"\u0448\u0443\u0442\u043b. \u2013 \u0448\u0443\u0442\u043b\u0438\u0432\u043e\u0435 "
                        "\u0443\u043f\u043e\u0442\u0440\u0435\u0431\u043b\u0435\u043d\u0438\u0435 \u0441\u043b\u043e\u0432\u0430\n"
"\n"
"\u044d\u043a.  \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u044d\u043a\u043e\u043d\u043e\u043c\u0438\u043a\u0438\n"
"\n"
"\u044d\u043a\u043e\u043b. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u044d\u043a\u043e\u043b\u043e\u0433\u0438\u0438\n"
"\n"
"\u044d\u043b. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u0442\u0435\u0445\u043d\u0438\u043a\u0438\n"
"\n"
"\u044d\u0442. - \u0442\u0435\u0440\u043c\u0438\u043d \u044d\u0442\u0438\u043a\u0438\n"
"\n"
"\u044d\u0442\u043d. \u2013 \u0442\u0435\u0440\u043c\u0438\u043d \u044d\u0442\u043d\u043e\u0433\u0440\u0430\u0444\u0438\u0438\n"
"\n"
"\u044e\u0440. \u2013 \u044e\u0440\u0438\u0434\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0442\u0435\u0440\u043c\u0438\u043d\n"
"\n"
"\u044f\u0437. \u2013 \u044f\u0437\u044b\u043a, \u044f\u0437\u044b\u043a\u0438", None))
        self.back_23.setText("")
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u043e\u0442\u0437\u044b\u0432", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442 \u0432\u0430\u0448\u0435\u0433\u043e \u043e\u0442\u0437\u044b\u0432\u0430!", None))
        self.lineEdit_3.setText("")
        self.back_24.setText("")
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0431\u0443\u043a\u0432\u0435", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u043d\u0442\u0435\u0440\u0435\u0441\u0443\u044e\u0449\u0443\u044e \u0432\u0430\u0441 \u0431\u0443\u043a\u0432\u0443", None))
        self.letter_19.setText(QCoreApplication.translate("MainWindow", u"\u0421", None))
        self.letter_1.setText(QCoreApplication.translate("MainWindow", u"\u0410", None))
        self.letter_2.setText(QCoreApplication.translate("MainWindow", u"\u0411", None))
        self.letter_3.setText(QCoreApplication.translate("MainWindow", u"\u0412", None))
        self.letter_4.setText(QCoreApplication.translate("MainWindow", u"\u0413", None))
        self.letter_5.setText(QCoreApplication.translate("MainWindow", u"\u0414", None))
        self.letter_6.setText(QCoreApplication.translate("MainWindow", u"\u0415", None))
        self.letter_20.setText(QCoreApplication.translate("MainWindow", u"\u0422", None))
        self.letter_7.setText(QCoreApplication.translate("MainWindow", u"\u0401", None))
        self.letter_13.setText(QCoreApplication.translate("MainWindow", u"\u041b", None))
        self.letter_8.setText(QCoreApplication.translate("MainWindow", u"\u0416", None))
        self.letter_14.setText(QCoreApplication.translate("MainWindow", u"\u041c", None))
        self.letter_9.setText(QCoreApplication.translate("MainWindow", u"\u0417", None))
        self.letter_10.setText(QCoreApplication.translate("MainWindow", u"\u0418", None))
        self.letter_11.setText(QCoreApplication.translate("MainWindow", u"\u0419", None))
        self.letter_12.setText(QCoreApplication.translate("MainWindow", u"\u041a", None))
        self.letter_15.setText(QCoreApplication.translate("MainWindow", u"\u041d", None))
        self.letter_16.setText(QCoreApplication.translate("MainWindow", u"\u041e", None))
        self.letter_17.setText(QCoreApplication.translate("MainWindow", u"\u041f", None))
        self.letter_18.setText(QCoreApplication.translate("MainWindow", u"\u0420", None))
        self.letter_21.setText(QCoreApplication.translate("MainWindow", u"\u0423", None))
        self.letter_22.setText(QCoreApplication.translate("MainWindow", u"\u0424", None))
        self.letter_23.setText(QCoreApplication.translate("MainWindow", u"\u0425", None))
        self.letter_24.setText(QCoreApplication.translate("MainWindow", u"\u0426", None))
        self.letter_25.setText(QCoreApplication.translate("MainWindow", u"\u0427", None))
        self.letter_26.setText(QCoreApplication.translate("MainWindow", u"\u0428", None))
        self.letter_27.setText(QCoreApplication.translate("MainWindow", u"\u0429", None))
        self.letter_28.setText(QCoreApplication.translate("MainWindow", u"\u042a", None))
        self.letter_29.setText(QCoreApplication.translate("MainWindow", u"\u042b", None))
        self.letter_30.setText(QCoreApplication.translate("MainWindow", u"\u042c", None))
        self.letter_31.setText(QCoreApplication.translate("MainWindow", u"\u042d", None))
        self.letter_32.setText(QCoreApplication.translate("MainWindow", u"\u042e", None))
        self.letter_33.setText(QCoreApplication.translate("MainWindow", u"\u042f", None))
        self.back_25.setText("")
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0431\u0443\u043a\u0432\u0435", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u043d\u0442\u0435\u0440\u0435\u0441\u0443\u044e\u0449\u0435\u0435 \u0432\u0430\u0441 \u0441\u043b\u043e\u0432\u043e", None))
        self.back_26.setText("")
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0431\u0443\u043a\u0432\u0435", None))
        self.label_76.setText("")
        self.another_search_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0434\u0440\u0443\u0433\u0443\u044e \u0431\u0443\u043a\u0432\u0443", None))
        self.back_27.setText("")
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.label_9.setText("")
        self.reset_stats.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0443", None))
    # retranslateUi

