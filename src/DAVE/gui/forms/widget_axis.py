# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_axis.ui',
# licensing of 'widget_axis.ui' applies.
#
# Created: Fri May 15 10:16:21 2020
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_widget_axis(object):
    def setupUi(self, widget_axis):
        widget_axis.setObjectName("widget_axis")
        widget_axis.resize(427, 637)
        widget_axis.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayout = QtWidgets.QVBoxLayout(widget_axis)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(widget_axis)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.frame = QtWidgets.QFrame(widget_axis)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.checkBox_1 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_1.setObjectName("checkBox_1")
        self.gridLayout.addWidget(self.checkBox_1, 0, 1, 1, 1)
        self.doubleSpinBox_1 = QtWidgets.QDoubleSpinBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_1.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_1.setSizePolicy(sizePolicy)
        self.doubleSpinBox_1.setDecimals(3)
        self.doubleSpinBox_1.setMinimum(-999999999999.0)
        self.doubleSpinBox_1.setMaximum(99999999999999.0)
        self.doubleSpinBox_1.setObjectName("doubleSpinBox_1")
        self.gridLayout.addWidget(self.doubleSpinBox_1, 0, 2, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 1, 1, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_2.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_2.setSizePolicy(sizePolicy)
        self.doubleSpinBox_2.setDecimals(3)
        self.doubleSpinBox_2.setMinimum(-999999999999.0)
        self.doubleSpinBox_2.setMaximum(99999999999999.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout.addWidget(self.doubleSpinBox_2, 1, 2, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 2, 1, 1, 1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_3.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_3.setSizePolicy(sizePolicy)
        self.doubleSpinBox_3.setDecimals(3)
        self.doubleSpinBox_3.setMinimum(-999999999999.0)
        self.doubleSpinBox_3.setMaximum(99999999999999.0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout.addWidget(self.doubleSpinBox_3, 2, 2, 1, 2)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout.addWidget(self.frame_2, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 4, 1, 1, 1)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_4.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_4.setSizePolicy(sizePolicy)
        self.doubleSpinBox_4.setDecimals(3)
        self.doubleSpinBox_4.setMinimum(-999999999999.0)
        self.doubleSpinBox_4.setMaximum(99999999999999.0)
        self.doubleSpinBox_4.setSingleStep(5.0)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout.addWidget(self.doubleSpinBox_4, 4, 2, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 5, 1, 1, 1)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_5.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_5.setSizePolicy(sizePolicy)
        self.doubleSpinBox_5.setDecimals(3)
        self.doubleSpinBox_5.setMinimum(-999999999999.0)
        self.doubleSpinBox_5.setMaximum(99999999999999.0)
        self.doubleSpinBox_5.setSingleStep(5.0)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.gridLayout.addWidget(self.doubleSpinBox_5, 5, 2, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 6, 1, 1, 1)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_6.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_6.setSizePolicy(sizePolicy)
        self.doubleSpinBox_6.setDecimals(3)
        self.doubleSpinBox_6.setMinimum(-999999999999.0)
        self.doubleSpinBox_6.setMaximum(99999999999999.0)
        self.doubleSpinBox_6.setSingleStep(5.0)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.gridLayout.addWidget(self.doubleSpinBox_6, 6, 2, 1, 2)
        self.verticalLayout.addWidget(self.frame)
        self.toolButton = QtWidgets.QToolButton(widget_axis)
        self.toolButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.toolButton.setObjectName("toolButton")
        self.verticalLayout.addWidget(self.toolButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(widget_axis)
        QtCore.QMetaObject.connectSlotsByName(widget_axis)

    def retranslateUi(self, widget_axis):
        widget_axis.setWindowTitle(QtWidgets.QApplication.translate("widget_axis", "Form", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("widget_axis", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Set position and rotation.</span></p><p>Modes that are &quot;<span style=\" font-weight:600;\">fixed</span>&quot; will not move when solving statics</p></body></html>", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("widget_axis", "X - translation", None, -1))
        self.checkBox_1.setText(QtWidgets.QApplication.translate("widget_axis", "Fixed", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("widget_axis", "Y - translation", None, -1))
        self.checkBox_2.setText(QtWidgets.QApplication.translate("widget_axis", "Fixed", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("widget_axis", "Z - translation", None, -1))
        self.checkBox_3.setText(QtWidgets.QApplication.translate("widget_axis", "Fixed", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("widget_axis", "X-rotation", None, -1))
        self.checkBox_4.setText(QtWidgets.QApplication.translate("widget_axis", "Fixed", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("widget_axis", "Y-rotation", None, -1))
        self.checkBox_5.setText(QtWidgets.QApplication.translate("widget_axis", "Fixed", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("widget_axis", "Z-rotation", None, -1))
        self.checkBox_6.setText(QtWidgets.QApplication.translate("widget_axis", "Fixed", None, -1))
        self.toolButton.setToolTip(QtWidgets.QApplication.translate("widget_axis", "<html><head/><body><p><span style=\" font-weight:600;\">Definition:</span></p><p>Rotation is defined as a rotation about a single axis.</p><p>- The axis of rotation is defined by the X,Y and Z components of the rotation.</p><p>- The angle or rotation is defined by the length of the rotation vector.</p><p><span style=\" font-weight:600;\"><br/>Examples:</span></p><p>x=0, y=0, z=90 ---&gt; 90 degees Rotation about Z-axis</p><p>x=10, y= 10, z= 0 --&gt; Axis of rotation is (1,1,0) and rotation angle |(10,10,0)| = sqrt(200)</p><p>x=Free, y =0, z= 0 --&gt; Axis system is free to rotate about the x-axis</p><p>x=Free, y = Free, z=0 --&gt; Axis system is free to rotate about any axis with z=0. The effect of this is hard to visualize.</p><p><br/></p><p><span style=\" font-weight:600;\">Tips:</span></p><p>To define subsequent rotations about different axis it is often more convenient to stack axis-nodes on top of eachother. For example to model a rotation of 20 degrees about the z-axis (yaw) and rotation of 5 degrees about the y-axis (pitch) simply consider the following:</p><p>1. Create an axis system for the yaw. Set the rotation to (0,0,20)</p><p>2. Create a second axis system and place it under yaw. Set the rotation of this axis system to (0,5,0).</p></body></html>", None, -1))
        self.toolButton.setText(QtWidgets.QApplication.translate("widget_axis", "??? (hoover for info)", None, -1))

