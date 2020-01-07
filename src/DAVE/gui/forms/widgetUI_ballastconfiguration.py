# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_ballastconfiguration.ui',
# licensing of 'widget_ballastconfiguration.ui' applies.
#
# Created: Tue Jan  7 14:43:03 2020
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_widget_ballastsystem(object):
    def setupUi(self, widget_ballastsystem):
        widget_ballastsystem.setObjectName("widget_ballastsystem")
        widget_ballastsystem.resize(1270, 1320)
        widget_ballastsystem.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayout = QtWidgets.QVBoxLayout(widget_ballastsystem)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(widget_ballastsystem)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pbFillAll = QtWidgets.QPushButton(self.widget_2)
        self.pbFillAll.setObjectName("pbFillAll")
        self.horizontalLayout_2.addWidget(self.pbFillAll)
        self.pbEmptyAll = QtWidgets.QPushButton(self.widget_2)
        self.pbEmptyAll.setObjectName("pbEmptyAll")
        self.horizontalLayout_2.addWidget(self.pbEmptyAll)
        self.pbToggleFreeze = QtWidgets.QPushButton(self.widget_2)
        self.pbToggleFreeze.setObjectName("pbToggleFreeze")
        self.horizontalLayout_2.addWidget(self.pbToggleFreeze)
        self.pbUnfreezeAll = QtWidgets.QPushButton(self.widget_2)
        self.pbUnfreezeAll.setObjectName("pbUnfreezeAll")
        self.horizontalLayout_2.addWidget(self.pbUnfreezeAll)
        self.pbFreezeAll = QtWidgets.QPushButton(self.widget_2)
        self.pbFreezeAll.setObjectName("pbFreezeAll")
        self.horizontalLayout_2.addWidget(self.pbFreezeAll)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.widget_2)
        self.tableWidget = QtWidgets.QTableWidget(widget_ballastsystem)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(widget_ballastsystem)
        QtCore.QMetaObject.connectSlotsByName(widget_ballastsystem)
        widget_ballastsystem.setTabOrder(self.tableWidget, self.pbFillAll)
        widget_ballastsystem.setTabOrder(self.pbFillAll, self.pbEmptyAll)
        widget_ballastsystem.setTabOrder(self.pbEmptyAll, self.pbToggleFreeze)
        widget_ballastsystem.setTabOrder(self.pbToggleFreeze, self.pbUnfreezeAll)
        widget_ballastsystem.setTabOrder(self.pbUnfreezeAll, self.pbFreezeAll)

    def retranslateUi(self, widget_ballastsystem):
        widget_ballastsystem.setWindowTitle(QtWidgets.QApplication.translate("widget_ballastsystem", "Form", None, -1))
        self.pbFillAll.setText(QtWidgets.QApplication.translate("widget_ballastsystem", "Fill all", None, -1))
        self.pbEmptyAll.setText(QtWidgets.QApplication.translate("widget_ballastsystem", "Empty all", None, -1))
        self.pbToggleFreeze.setText(QtWidgets.QApplication.translate("widget_ballastsystem", "Toggle freeze", None, -1))
        self.pbUnfreezeAll.setText(QtWidgets.QApplication.translate("widget_ballastsystem", "Unfreeze all", None, -1))
        self.pbFreezeAll.setText(QtWidgets.QApplication.translate("widget_ballastsystem", "Freeze all", None, -1))
        self.tableWidget.verticalHeaderItem(0).setText(QtWidgets.QApplication.translate("widget_ballastsystem", "Tank1", None, -1))
        self.tableWidget.verticalHeaderItem(1).setText(QtWidgets.QApplication.translate("widget_ballastsystem", "Tank2", None, -1))
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("widget_ballastsystem", "Capacity [kN]", None, -1))
        self.tableWidget.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("widget_ballastsystem", "Fill [%]", None, -1))
        self.tableWidget.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("widget_ballastsystem", "Frozen", None, -1))
        self.tableWidget.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("widget_ballastsystem", "X [m]", None, -1))
        self.tableWidget.horizontalHeaderItem(4).setText(QtWidgets.QApplication.translate("widget_ballastsystem", "Y [m]", None, -1))
        self.tableWidget.horizontalHeaderItem(5).setText(QtWidgets.QApplication.translate("widget_ballastsystem", "Z [m]", None, -1))

