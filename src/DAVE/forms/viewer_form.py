# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2107, 1721)
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Dave_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame3d = QtWidgets.QFrame(self.centralwidget)
        self.frame3d.setAcceptDrops(False)
        self.frame3d.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame3d.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame3d.setObjectName("frame3d")
        self.label_2 = QtWidgets.QLabel(self.frame3d)
        self.label_2.setGeometry(QtCore.QRect(580, 410, 161, 20))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.frame3d)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2107, 31))
        self.menubar.setObjectName("menubar")
        self.menuSolve_Statics = QtWidgets.QMenu(self.menubar)
        self.menuSolve_Statics.setObjectName("menuSolve_Statics")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuView_2 = QtWidgets.QMenu(self.menubar)
        self.menuView_2.setObjectName("menuView_2")
        self.menuWhat_if = QtWidgets.QMenu(self.menubar)
        self.menuWhat_if.setObjectName("menuWhat_if")
        self.menuMarine = QtWidgets.QMenu(self.menubar)
        self.menuMarine.setObjectName("menuMarine")
        self.menuRender = QtWidgets.QMenu(self.menubar)
        self.menuRender.setObjectName("menuRender")
        MainWindow.setMenuBar(self.menubar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.treeView = QtWidgets.QTreeView(self.dockWidgetContents)
        self.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treeView.setRootIsDecorated(True)
        self.treeView.setExpandsOnDoubleClick(False)
        self.treeView.setObjectName("treeView")
        self.treeView.header().setVisible(False)
        self.gridLayout.addWidget(self.treeView, 0, 0, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.dockWidget_2 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.dockWidgetContents_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.dockWidgetContents_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pbGenerateSceneCode = QtWidgets.QPushButton(self.frame_3)
        self.pbGenerateSceneCode.setObjectName("pbGenerateSceneCode")
        self.verticalLayout_2.addWidget(self.pbGenerateSceneCode)
        self.pbCopyFeedback = QtWidgets.QPushButton(self.frame_3)
        self.pbCopyFeedback.setObjectName("pbCopyFeedback")
        self.verticalLayout_2.addWidget(self.pbCopyFeedback)
        self.horizontalLayout_4.addWidget(self.frame_3)
        self.teFeedback = QtWidgets.QTextEdit(self.dockWidgetContents_2)
        self.teFeedback.setAutoFillBackground(False)
        self.teFeedback.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.teFeedback.setObjectName("teFeedback")
        self.horizontalLayout_4.addWidget(self.teFeedback)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_2)
        self.dockWidget_3 = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_3.sizePolicy().hasHeightForWidth())
        self.dockWidget_3.setSizePolicy(sizePolicy)
        self.dockWidget_3.setFloating(True)
        self.dockWidget_3.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget_3.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_3.setObjectName("dockWidget_3")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_3.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_3.setSizePolicy(sizePolicy)
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widgetLayout = QtWidgets.QVBoxLayout()
        self.widgetLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.widgetLayout.setSpacing(0)
        self.widgetLayout.setObjectName("widgetLayout")
        self.verticalLayout_3.addLayout(self.widgetLayout)
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_3)
        self.pythonDockWidget = QtWidgets.QDockWidget(MainWindow)
        self.pythonDockWidget.setFloating(True)
        self.pythonDockWidget.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.pythonDockWidget.setObjectName("pythonDockWidget")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.dockWidgetContents_4)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.teHistory = QtWidgets.QTextEdit(self.dockWidgetContents_4)
        self.teHistory.setReadOnly(True)
        self.teHistory.setObjectName("teHistory")
        self.verticalLayout.addWidget(self.teHistory)
        self.frame_2 = QtWidgets.QFrame(self.dockWidgetContents_4)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbCopyHistory = QtWidgets.QPushButton(self.frame_2)
        self.pbCopyHistory.setObjectName("pbCopyHistory")
        self.horizontalLayout.addWidget(self.pbCopyHistory)
        self.pbStartOver = QtWidgets.QPushButton(self.frame_2)
        self.pbStartOver.setObjectName("pbStartOver")
        self.horizontalLayout.addWidget(self.pbStartOver)
        self.verticalLayout.addWidget(self.frame_2)
        self.label_3 = QtWidgets.QLabel(self.dockWidgetContents_4)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.teCode = QtWidgets.QTextEdit(self.dockWidgetContents_4)
        self.teCode.setObjectName("teCode")
        self.verticalLayout.addWidget(self.teCode)
        self.cbAutoExecute = QtWidgets.QCheckBox(self.dockWidgetContents_4)
        self.cbAutoExecute.setChecked(True)
        self.cbAutoExecute.setObjectName("cbAutoExecute")
        self.verticalLayout.addWidget(self.cbAutoExecute)
        self.cbAutoStatics = QtWidgets.QCheckBox(self.dockWidgetContents_4)
        self.cbAutoStatics.setObjectName("cbAutoStatics")
        self.verticalLayout.addWidget(self.cbAutoStatics)
        self.frame = QtWidgets.QFrame(self.dockWidgetContents_4)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pbRunCode = QtWidgets.QPushButton(self.frame)
        self.pbRunCode.setObjectName("pbRunCode")
        self.horizontalLayout_3.addWidget(self.pbRunCode)
        self.verticalLayout.addWidget(self.frame)
        self.pythonDockWidget.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.pythonDockWidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidget_4 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_4.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget_4.setObjectName("dockWidget_4")
        self.dockWidgetContents_5 = QtWidgets.QWidget()
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dockWidgetContents_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.dispPropTree = QtWidgets.QTreeWidget(self.dockWidgetContents_5)
        self.dispPropTree.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.dispPropTree.setAlternatingRowColors(True)
        self.dispPropTree.setRootIsDecorated(False)
        self.dispPropTree.setObjectName("dispPropTree")
        item_0 = QtWidgets.QTreeWidgetItem(self.dispPropTree)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.dispPropTree.header().setVisible(False)
        self.gridLayout_2.addWidget(self.dispPropTree, 0, 0, 1, 1)
        self.dockWidget_4.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_4)
        self.goalseekDockWidget = QtWidgets.QDockWidget(MainWindow)
        self.goalseekDockWidget.setFloating(True)
        self.goalseekDockWidget.setObjectName("goalseekDockWidget")
        self.dockWidgetContents_6 = QtWidgets.QWidget()
        self.dockWidgetContents_6.setObjectName("dockWidgetContents_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.dockWidgetContents_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_9 = QtWidgets.QLabel(self.dockWidgetContents_6)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.dockWidgetContents_6)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.dockWidgetContents_6)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.gsValue = QtWidgets.QLineEdit(self.dockWidgetContents_6)
        self.gsValue.setObjectName("gsValue")
        self.gridLayout_3.addWidget(self.gsValue, 1, 2, 1, 1)
        self.gsSetProp = QtWidgets.QLineEdit(self.dockWidgetContents_6)
        self.gsSetProp.setObjectName("gsSetProp")
        self.gridLayout_3.addWidget(self.gsSetProp, 0, 2, 1, 1)
        self.gsSetNode = QtWidgets.QLineEdit(self.dockWidgetContents_6)
        self.gsSetNode.setObjectName("gsSetNode")
        self.gridLayout_3.addWidget(self.gsSetNode, 0, 4, 1, 1)
        self.gsChangeProp = QtWidgets.QLineEdit(self.dockWidgetContents_6)
        self.gsChangeProp.setObjectName("gsChangeProp")
        self.gridLayout_3.addWidget(self.gsChangeProp, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.dockWidgetContents_6)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)
        self.gsChangeNode = QtWidgets.QLineEdit(self.dockWidgetContents_6)
        self.gsChangeNode.setObjectName("gsChangeNode")
        self.gridLayout_3.addWidget(self.gsChangeNode, 2, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.dockWidgetContents_6)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.dockWidgetContents_6)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 2, 3, 1, 1)
        self.btnGoalSeek = QtWidgets.QPushButton(self.dockWidgetContents_6)
        self.btnGoalSeek.setObjectName("btnGoalSeek")
        self.gridLayout_3.addWidget(self.btnGoalSeek, 3, 4, 1, 1)
        self.goalseekDockWidget.setWidget(self.dockWidgetContents_6)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.goalseekDockWidget)
        self.stabilityDockWidget = QtWidgets.QDockWidget(MainWindow)
        self.stabilityDockWidget.setFloating(True)
        self.stabilityDockWidget.setObjectName("stabilityDockWidget")
        self.dockWidgetContents_7 = QtWidgets.QWidget()
        self.dockWidgetContents_7.setObjectName("dockWidgetContents_7")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.dockWidgetContents_7)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_10 = QtWidgets.QLabel(self.dockWidgetContents_7)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 0, 4, 1, 1)
        self.stability_displacement = QtWidgets.QDoubleSpinBox(self.dockWidgetContents_7)
        self.stability_displacement.setMaximum(999999999999999.0)
        self.stability_displacement.setProperty("value", 1.0)
        self.stability_displacement.setObjectName("stability_displacement")
        self.gridLayout_4.addWidget(self.stability_displacement, 1, 1, 1, 3)
        self.stability_node_name = QtWidgets.QLineEdit(self.dockWidgetContents_7)
        self.stability_node_name.setObjectName("stability_node_name")
        self.gridLayout_4.addWidget(self.stability_node_name, 0, 1, 1, 3)
        self.label_17 = QtWidgets.QLabel(self.dockWidgetContents_7)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 1, 4, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.dockWidgetContents_7)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.dockWidgetContents_7)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 2, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.dockWidgetContents_7)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.dockWidgetContents_7)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 8, 0, 1, 1)
        self.stability_heel_max = QtWidgets.QSpinBox(self.dockWidgetContents_7)
        self.stability_heel_max.setProperty("value", 60)
        self.stability_heel_max.setObjectName("stability_heel_max")
        self.gridLayout_4.addWidget(self.stability_heel_max, 2, 3, 1, 1)
        self.stability_n_steps = QtWidgets.QSpinBox(self.dockWidgetContents_7)
        self.stability_n_steps.setProperty("value", 60)
        self.stability_n_steps.setObjectName("stability_n_steps")
        self.gridLayout_4.addWidget(self.stability_n_steps, 3, 1, 1, 2)
        self.stability_heel_start = QtWidgets.QSpinBox(self.dockWidgetContents_7)
        self.stability_heel_start.setMinimum(-180)
        self.stability_heel_start.setMaximum(20)
        self.stability_heel_start.setObjectName("stability_heel_start")
        self.gridLayout_4.addWidget(self.stability_heel_start, 2, 1, 1, 1)
        self.stability_do_teardown = QtWidgets.QCheckBox(self.dockWidgetContents_7)
        self.stability_do_teardown.setChecked(True)
        self.stability_do_teardown.setObjectName("stability_do_teardown")
        self.gridLayout_4.addWidget(self.stability_do_teardown, 8, 1, 1, 2)
        self.stability_trim = QtWidgets.QCheckBox(self.dockWidgetContents_7)
        self.stability_trim.setChecked(True)
        self.stability_trim.setObjectName("stability_trim")
        self.gridLayout_4.addWidget(self.stability_trim, 7, 1, 1, 2)
        self.label_18 = QtWidgets.QLabel(self.dockWidgetContents_7)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 3, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.dockWidgetContents_7)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 2, 2, 1, 1)
        self.stability_sway = QtWidgets.QCheckBox(self.dockWidgetContents_7)
        self.stability_sway.setObjectName("stability_sway")
        self.gridLayout_4.addWidget(self.stability_sway, 5, 1, 1, 2)
        self.stability_yaw = QtWidgets.QCheckBox(self.dockWidgetContents_7)
        self.stability_yaw.setObjectName("stability_yaw")
        self.gridLayout_4.addWidget(self.stability_yaw, 6, 1, 1, 2)
        self.stability_surge = QtWidgets.QCheckBox(self.dockWidgetContents_7)
        self.stability_surge.setObjectName("stability_surge")
        self.gridLayout_4.addWidget(self.stability_surge, 4, 1, 1, 2)
        self.label_15 = QtWidgets.QLabel(self.dockWidgetContents_7)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 2, 4, 1, 1)
        self.stability_go = QtWidgets.QPushButton(self.dockWidgetContents_7)
        self.stability_go.setObjectName("stability_go")
        self.gridLayout_4.addWidget(self.stability_go, 9, 3, 1, 2)
        self.stabilityDockWidget.setWidget(self.dockWidgetContents_7)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.stabilityDockWidget)
        self.actionSave_scene = QtWidgets.QAction(MainWindow)
        self.actionSave_scene.setObjectName("actionSave_scene")
        self.actionImport_sub_scene = QtWidgets.QAction(MainWindow)
        self.actionImport_sub_scene.setObjectName("actionImport_sub_scene")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionHorizontal_camera = QtWidgets.QAction(MainWindow)
        self.actionHorizontal_camera.setObjectName("actionHorizontal_camera")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action2D_mode = QtWidgets.QAction(MainWindow)
        self.action2D_mode.setCheckable(True)
        self.action2D_mode.setObjectName("action2D_mode")
        self.actionDark_mode = QtWidgets.QAction(MainWindow)
        self.actionDark_mode.setCheckable(False)
        self.actionDark_mode.setObjectName("actionDark_mode")
        self.actionShow_visuals = QtWidgets.QAction(MainWindow)
        self.actionShow_visuals.setCheckable(True)
        self.actionShow_visuals.setChecked(True)
        self.actionShow_visuals.setObjectName("actionShow_visuals")
        self.actionShow_Geometry_elements = QtWidgets.QAction(MainWindow)
        self.actionShow_Geometry_elements.setCheckable(True)
        self.actionShow_Geometry_elements.setChecked(True)
        self.actionShow_Geometry_elements.setObjectName("actionShow_Geometry_elements")
        self.actionShow_force_applyting_element = QtWidgets.QAction(MainWindow)
        self.actionShow_force_applyting_element.setCheckable(True)
        self.actionShow_force_applyting_element.setChecked(True)
        self.actionShow_force_applyting_element.setObjectName("actionShow_force_applyting_element")
        self.actionSet_all_visible = QtWidgets.QAction(MainWindow)
        self.actionSet_all_visible.setObjectName("actionSet_all_visible")
        self.actionSet_all_hidden = QtWidgets.QAction(MainWindow)
        self.actionSet_all_hidden.setObjectName("actionSet_all_hidden")
        self.actionFull_refresh = QtWidgets.QAction(MainWindow)
        self.actionFull_refresh.setObjectName("actionFull_refresh")
        self.actionShow_water_plane = QtWidgets.QAction(MainWindow)
        self.actionShow_water_plane.setCheckable(True)
        self.actionShow_water_plane.setChecked(False)
        self.actionShow_water_plane.setObjectName("actionShow_water_plane")
        self.actionAdd_light = QtWidgets.QAction(MainWindow)
        self.actionAdd_light.setObjectName("actionAdd_light")
        self.actionShow_all_forces_at_same_size = QtWidgets.QAction(MainWindow)
        self.actionShow_all_forces_at_same_size.setCheckable(True)
        self.actionShow_all_forces_at_same_size.setChecked(True)
        self.actionShow_all_forces_at_same_size.setObjectName("actionShow_all_forces_at_same_size")
        self.actionIncrease_force_size = QtWidgets.QAction(MainWindow)
        self.actionIncrease_force_size.setObjectName("actionIncrease_force_size")
        self.actionDecrease_force_size = QtWidgets.QAction(MainWindow)
        self.actionDecrease_force_size.setObjectName("actionDecrease_force_size")
        self.actionIncrease_Geometry_size = QtWidgets.QAction(MainWindow)
        self.actionIncrease_Geometry_size.setObjectName("actionIncrease_Geometry_size")
        self.actionDecrease_Geometry_size = QtWidgets.QAction(MainWindow)
        self.actionDecrease_Geometry_size.setObjectName("actionDecrease_Geometry_size")
        self.actionPython_console = QtWidgets.QAction(MainWindow)
        self.actionPython_console.setObjectName("actionPython_console")
        self.actionGoal_seek = QtWidgets.QAction(MainWindow)
        self.actionGoal_seek.setObjectName("actionGoal_seek")
        self.actionStability_curve = QtWidgets.QAction(MainWindow)
        self.actionStability_curve.setObjectName("actionStability_curve")
        self.actionOptimize = QtWidgets.QAction(MainWindow)
        self.actionOptimize.setObjectName("actionOptimize")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionImport_browser = QtWidgets.QAction(MainWindow)
        self.actionImport_browser.setObjectName("actionImport_browser")
        self.actionRender_current_view = QtWidgets.QAction(MainWindow)
        self.actionRender_current_view.setObjectName("actionRender_current_view")
        self.dockWidget_3.raise_()
        self.pythonDockWidget.raise_()
        self.dockWidget_4.raise_()
        self.goalseekDockWidget.raise_()
        self.stabilityDockWidget.raise_()
        self.menuSolve_Statics.addAction(self.actionNew)
        self.menuSolve_Statics.addSeparator()
        self.menuSolve_Statics.addAction(self.actionOpen)
        self.menuSolve_Statics.addAction(self.actionImport_sub_scene)
        self.menuSolve_Statics.addAction(self.actionImport_browser)
        self.menuSolve_Statics.addSeparator()
        self.menuSolve_Statics.addAction(self.actionSave_scene)
        self.menuView.addAction(self.actionHorizontal_camera)
        self.menuView.addSeparator()
        self.menuView.addAction(self.action2D_mode)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionAdd_light)
        self.menuView.addAction(self.actionDark_mode)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionShow_all_forces_at_same_size)
        self.menuView.addAction(self.actionIncrease_force_size)
        self.menuView.addAction(self.actionDecrease_force_size)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionIncrease_Geometry_size)
        self.menuView.addAction(self.actionDecrease_Geometry_size)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionShow_visuals)
        self.menuView.addAction(self.actionShow_Geometry_elements)
        self.menuView.addAction(self.actionShow_force_applyting_element)
        self.menuView.addAction(self.actionShow_water_plane)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionSet_all_visible)
        self.menuView.addAction(self.actionSet_all_hidden)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionFull_refresh)
        self.menuView_2.addAction(self.actionPython_console)
        self.menuWhat_if.addAction(self.actionGoal_seek)
        self.menuWhat_if.addAction(self.actionOptimize)
        self.menuMarine.addAction(self.actionStability_curve)
        self.menuRender.addAction(self.actionRender_current_view)
        self.menubar.addAction(self.menuSolve_Statics.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuView_2.menuAction())
        self.menubar.addAction(self.menuWhat_if.menuAction())
        self.menubar.addAction(self.menuMarine.menuAction())
        self.menubar.addAction(self.menuRender.menuAction())
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pbCopyHistory, self.pbCopyFeedback)
        MainWindow.setTabOrder(self.pbCopyFeedback, self.teFeedback)
        MainWindow.setTabOrder(self.teFeedback, self.teHistory)
        MainWindow.setTabOrder(self.teHistory, self.gsSetProp)
        MainWindow.setTabOrder(self.gsSetProp, self.gsSetNode)
        MainWindow.setTabOrder(self.gsSetNode, self.gsValue)
        MainWindow.setTabOrder(self.gsValue, self.gsChangeProp)
        MainWindow.setTabOrder(self.gsChangeProp, self.gsChangeNode)
        MainWindow.setTabOrder(self.gsChangeNode, self.btnGoalSeek)
        MainWindow.setTabOrder(self.btnGoalSeek, self.pbRunCode)
        MainWindow.setTabOrder(self.pbRunCode, self.dispPropTree)
        MainWindow.setTabOrder(self.dispPropTree, self.cbAutoStatics)
        MainWindow.setTabOrder(self.cbAutoStatics, self.pbGenerateSceneCode)
        MainWindow.setTabOrder(self.pbGenerateSceneCode, self.pbStartOver)
        MainWindow.setTabOrder(self.pbStartOver, self.treeView)
        MainWindow.setTabOrder(self.treeView, self.teCode)
        MainWindow.setTabOrder(self.teCode, self.cbAutoExecute)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DAVE"))
        self.label_2.setText(_translate("MainWindow", "3D view loading...."))
        self.menuSolve_Statics.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuView_2.setTitle(_translate("MainWindow", "Window"))
        self.menuWhat_if.setTitle(_translate("MainWindow", "Optimize"))
        self.menuMarine.setTitle(_translate("MainWindow", "Marine"))
        self.menuRender.setTitle(_translate("MainWindow", "Blender"))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Nodes"))
        self.dockWidget_2.setWindowTitle(_translate("MainWindow", "Feedback"))
        self.pbGenerateSceneCode.setText(_translate("MainWindow", "Generate Scene Code"))
        self.pbCopyFeedback.setText(_translate("MainWindow", "Copy"))
        self.dockWidget_3.setWindowTitle(_translate("MainWindow", "Node Properties Editor"))
        self.pythonDockWidget.setWindowTitle(_translate("MainWindow", "Python code"))
        self.label.setText(_translate("MainWindow", "History of succesfully executed code:"))
        self.pbCopyHistory.setText(_translate("MainWindow", "Copy all"))
        self.pbStartOver.setText(_translate("MainWindow", "Start over"))
        self.label_3.setText(_translate("MainWindow", "New code to be executed"))
        self.cbAutoExecute.setText(_translate("MainWindow", "Auto execute generated code"))
        self.cbAutoStatics.setText(_translate("MainWindow", "Solve statics on after succesfull execution"))
        self.pbRunCode.setText(_translate("MainWindow", "Run code"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.dockWidget_4.setWindowTitle(_translate("MainWindow", "Derived Properties"))
        self.dispPropTree.headerItem().setText(0, _translate("MainWindow", "1"))
        __sortingEnabled = self.dispPropTree.isSortingEnabled()
        self.dispPropTree.setSortingEnabled(False)
        self.dispPropTree.topLevelItem(0).setText(0, _translate("MainWindow", "Property"))
        self.dispPropTree.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Value"))
        self.dispPropTree.setSortingEnabled(__sortingEnabled)
        self.goalseekDockWidget.setWindowTitle(_translate("MainWindow", "Goal-seek"))
        self.label_9.setText(_translate("MainWindow", "(scalar number)"))
        self.label_4.setText(_translate("MainWindow", "Set propery:"))
        self.label_5.setText(_translate("MainWindow", "To value:"))
        self.label_6.setText(_translate("MainWindow", "By changing:"))
        self.label_7.setText(_translate("MainWindow", "of node"))
        self.label_8.setText(_translate("MainWindow", "of node"))
        self.btnGoalSeek.setText(_translate("MainWindow", "Go -->"))
        self.stabilityDockWidget.setWindowTitle(_translate("MainWindow", "Stability curves"))
        self.label_10.setText(_translate("MainWindow", "[Axis or Rigid-body]"))
        self.stability_node_name.setText(_translate("MainWindow", "Axis or Rigid body name here"))
        self.label_17.setText(_translate("MainWindow", "[kN]"))
        self.label_11.setText(_translate("MainWindow", "Node"))
        self.label_12.setText(_translate("MainWindow", "Range"))
        self.label_16.setText(_translate("MainWindow", "Displacement"))
        self.label_13.setText(_translate("MainWindow", "Tear-down"))
        self.stability_do_teardown.setText(_translate("MainWindow", "Delete temporary nodes"))
        self.stability_trim.setText(_translate("MainWindow", "Allow Trim"))
        self.label_18.setText(_translate("MainWindow", "Steps"))
        self.label_14.setText(_translate("MainWindow", "till"))
        self.stability_sway.setText(_translate("MainWindow", "Allow Sway"))
        self.stability_yaw.setText(_translate("MainWindow", "Allow Yaw"))
        self.stability_surge.setText(_translate("MainWindow", "Allow Surge"))
        self.label_15.setText(_translate("MainWindow", "[degrees]"))
        self.stability_go.setText(_translate("MainWindow", "Displacement driven curve"))
        self.actionSave_scene.setText(_translate("MainWindow", "Save as"))
        self.actionImport_sub_scene.setText(_translate("MainWindow", "Import (file)"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionHorizontal_camera.setText(_translate("MainWindow", "Level camera (make horizon horizontal)"))
        self.actionHorizontal_camera.setShortcut(_translate("MainWindow", "Alt+L"))
        self.action.setText(_translate("MainWindow", "---"))
        self.action2D_mode.setText(_translate("MainWindow", "2D mode"))
        self.actionDark_mode.setText(_translate("MainWindow", "Make darker"))
        self.actionDark_mode.setShortcut(_translate("MainWindow", "Alt+-"))
        self.actionShow_visuals.setText(_translate("MainWindow", "Show visuals"))
        self.actionShow_Geometry_elements.setText(_translate("MainWindow", "Show Geometry elements"))
        self.actionShow_force_applyting_element.setText(_translate("MainWindow", "Show non-geometry elements"))
        self.actionSet_all_visible.setText(_translate("MainWindow", "Set all visible"))
        self.actionSet_all_hidden.setText(_translate("MainWindow", "Set all hidden"))
        self.actionFull_refresh.setText(_translate("MainWindow", "Full refresh"))
        self.actionShow_water_plane.setText(_translate("MainWindow", "Show water-plane"))
        self.actionAdd_light.setText(_translate("MainWindow", "Make lighter"))
        self.actionAdd_light.setShortcut(_translate("MainWindow", "Alt+="))
        self.actionShow_all_forces_at_same_size.setText(_translate("MainWindow", "Show all forces same size (normalize)"))
        self.actionIncrease_force_size.setText(_translate("MainWindow", "Increase force size"))
        self.actionIncrease_force_size.setShortcut(_translate("MainWindow", "Alt+]"))
        self.actionDecrease_force_size.setText(_translate("MainWindow", "Decrease force size"))
        self.actionDecrease_force_size.setShortcut(_translate("MainWindow", "Alt+["))
        self.actionIncrease_Geometry_size.setText(_translate("MainWindow", "Increase Geometry size (poi, axis)"))
        self.actionIncrease_Geometry_size.setShortcut(_translate("MainWindow", "Alt+Shift+]"))
        self.actionDecrease_Geometry_size.setText(_translate("MainWindow", "Decrease Geometry size"))
        self.actionDecrease_Geometry_size.setShortcut(_translate("MainWindow", "Alt+Shift+["))
        self.actionPython_console.setText(_translate("MainWindow", "Python console"))
        self.actionGoal_seek.setText(_translate("MainWindow", "Goal-seek (one variable)"))
        self.actionStability_curve.setText(_translate("MainWindow", "Stability-curve"))
        self.actionOptimize.setText(_translate("MainWindow", "TODO: Optimize (multiple variables)"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionImport_browser.setText(_translate("MainWindow", "Import (browser)"))
        self.actionRender_current_view.setText(_translate("MainWindow", "Render current view"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

