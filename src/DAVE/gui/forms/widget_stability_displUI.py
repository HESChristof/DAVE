# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_stability_displ.ui',
# licensing of 'widget_stability_displ.ui' applies.
#
# Created: Wed Dec 25 10:21:04 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_WidgetDispDrivenStability(object):
    def setupUi(self, WidgetDispDrivenStability):
        WidgetDispDrivenStability.setObjectName("WidgetDispDrivenStability")
        WidgetDispDrivenStability.resize(566, 528)
        WidgetDispDrivenStability.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.gridLayout = QtWidgets.QGridLayout(WidgetDispDrivenStability)
        self.gridLayout.setObjectName("gridLayout")
        self.node_name = QtWidgets.QComboBox(WidgetDispDrivenStability)
        self.node_name.setObjectName("node_name")
        self.gridLayout.addWidget(self.node_name, 0, 2, 1, 3)
        self.label_18 = QtWidgets.QLabel(WidgetDispDrivenStability)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 3, 0, 1, 1)
        self.stability_surge = QtWidgets.QCheckBox(WidgetDispDrivenStability)
        self.stability_surge.setObjectName("stability_surge")
        self.gridLayout.addWidget(self.stability_surge, 4, 2, 1, 2)
        self.stability_sway = QtWidgets.QCheckBox(WidgetDispDrivenStability)
        self.stability_sway.setObjectName("stability_sway")
        self.gridLayout.addWidget(self.stability_sway, 5, 2, 1, 2)
        self.stability_yaw = QtWidgets.QCheckBox(WidgetDispDrivenStability)
        self.stability_yaw.setObjectName("stability_yaw")
        self.gridLayout.addWidget(self.stability_yaw, 6, 2, 1, 2)
        self.stability_trim = QtWidgets.QCheckBox(WidgetDispDrivenStability)
        self.stability_trim.setChecked(False)
        self.stability_trim.setObjectName("stability_trim")
        self.gridLayout.addWidget(self.stability_trim, 7, 2, 1, 2)
        self.label_13 = QtWidgets.QLabel(WidgetDispDrivenStability)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 8, 0, 1, 1)
        self.stability_n_steps = QtWidgets.QSpinBox(WidgetDispDrivenStability)
        self.stability_n_steps.setMaximum(1000)
        self.stability_n_steps.setProperty("value", 40)
        self.stability_n_steps.setObjectName("stability_n_steps")
        self.gridLayout.addWidget(self.stability_n_steps, 3, 2, 1, 2)
        self.label_11 = QtWidgets.QLabel(WidgetDispDrivenStability)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)
        self.stability_do_teardown = QtWidgets.QCheckBox(WidgetDispDrivenStability)
        self.stability_do_teardown.setChecked(True)
        self.stability_do_teardown.setObjectName("stability_do_teardown")
        self.gridLayout.addWidget(self.stability_do_teardown, 8, 2, 1, 2)
        self.stability_go = QtWidgets.QPushButton(WidgetDispDrivenStability)
        self.stability_go.setObjectName("stability_go")
        self.gridLayout.addWidget(self.stability_go, 9, 4, 1, 2)
        self.label_16 = QtWidgets.QLabel(WidgetDispDrivenStability)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 1, 0, 1, 1)
        self.stability_heel_start = QtWidgets.QSpinBox(WidgetDispDrivenStability)
        self.stability_heel_start.setMinimum(-180)
        self.stability_heel_start.setMaximum(20)
        self.stability_heel_start.setObjectName("stability_heel_start")
        self.gridLayout.addWidget(self.stability_heel_start, 2, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(WidgetDispDrivenStability)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 1, 5, 1, 1)
        self.label_14 = QtWidgets.QLabel(WidgetDispDrivenStability)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 3, 1, 1)
        self.stability_heel_max = QtWidgets.QSpinBox(WidgetDispDrivenStability)
        self.stability_heel_max.setMaximum(180)
        self.stability_heel_max.setProperty("value", 40)
        self.stability_heel_max.setObjectName("stability_heel_max")
        self.gridLayout.addWidget(self.stability_heel_max, 2, 4, 1, 1)
        self.label_15 = QtWidgets.QLabel(WidgetDispDrivenStability)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 5, 1, 1)
        self.label_12 = QtWidgets.QLabel(WidgetDispDrivenStability)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 1)
        self.stability_displacement = QtWidgets.QDoubleSpinBox(WidgetDispDrivenStability)
        self.stability_displacement.setMaximum(999999999999999.0)
        self.stability_displacement.setProperty("value", 1.0)
        self.stability_displacement.setObjectName("stability_displacement")
        self.gridLayout.addWidget(self.stability_displacement, 1, 2, 1, 3)
        self.label_10 = QtWidgets.QLabel(WidgetDispDrivenStability)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 5, 1, 1)
        self.pushButton = QtWidgets.QPushButton(WidgetDispDrivenStability)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 10, 4, 1, 2)

        self.retranslateUi(WidgetDispDrivenStability)
        QtCore.QMetaObject.connectSlotsByName(WidgetDispDrivenStability)
        WidgetDispDrivenStability.setTabOrder(self.node_name, self.stability_displacement)
        WidgetDispDrivenStability.setTabOrder(self.stability_displacement, self.stability_heel_start)
        WidgetDispDrivenStability.setTabOrder(self.stability_heel_start, self.stability_heel_max)
        WidgetDispDrivenStability.setTabOrder(self.stability_heel_max, self.stability_n_steps)
        WidgetDispDrivenStability.setTabOrder(self.stability_n_steps, self.stability_surge)
        WidgetDispDrivenStability.setTabOrder(self.stability_surge, self.stability_sway)
        WidgetDispDrivenStability.setTabOrder(self.stability_sway, self.stability_yaw)
        WidgetDispDrivenStability.setTabOrder(self.stability_yaw, self.stability_trim)
        WidgetDispDrivenStability.setTabOrder(self.stability_trim, self.stability_do_teardown)
        WidgetDispDrivenStability.setTabOrder(self.stability_do_teardown, self.stability_go)
        WidgetDispDrivenStability.setTabOrder(self.stability_go, self.pushButton)

    def retranslateUi(self, WidgetDispDrivenStability):
        WidgetDispDrivenStability.setWindowTitle(QtWidgets.QApplication.translate("WidgetDispDrivenStability", "Form", None, -1))
        self.label_18.setText(QtWidgets.QApplication.translate("WidgetDispDrivenStability", "Steps", None, -1))
        self.stability_surge.setText(QtWidgets.QApplication.translate("WidgetDispDrivenStability", "Allow Surge", None, -1))
        self.stability_sway.setText(QtWidgets.QApplication.translate("WidgetDispDrivenStability", "Allow Sway", None, -1))
        self.stability_yaw.setText(QtWidgets.QApplication.translate("WidgetDispDrivenStability", "Allow Yaw", None, -1))
        self.stability_trim.setText(QtWidgets.QApplication.translate("WidgetDispDrivenStability", "Allow Trim", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("WidgetDispDrivenStability", "Tear-down", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("WidgetDispDrivenStability", "Node", None, -1))
        self.stability_do_teardown.setText(QtWidgets.QApplication.translate("WidgetDispDrivenStability", "Delete temporary nodes", None, -1))
        self.stability_go.setText(QtWidgets.QApplication.translate("WidgetDispDrivenStability", "Displacement driven curve", None, -1))
        self.label_16.setText(QtWidgets.QApplication.translate("WidgetDispDrivenStability", "Displacement", None, -1))
        self.label_17.setText(QtWidgets.QApplication.translate("WidgetDispDrivenStability", "[kN]", None, -1))
        self.label_14.setText(QtWidgets.QApplication.translate("WidgetDispDrivenStability", "till", None, -1))
        self.label_15.setText(QtWidgets.QApplication.translate("WidgetDispDrivenStability", "[degrees]", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("WidgetDispDrivenStability", "Range", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("WidgetDispDrivenStability", "[Axis or Rigid-body]", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("WidgetDispDrivenStability", "Visualize [destructive]", None, -1))

