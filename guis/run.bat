call conda activate deploy

echo call pyside2-uic main_form.ui -o "..\src\DAVE\gui\forms\main_form.py"
echo call pyside2-uic widget_modeshapes.ui -o "..\src\DAVE\gui\forms\widgetUI_modeshapes.py"
call pyside2-uic widget_ballastconfiguration.ui -o "..\src\DAVE\gui\forms\widgetUI_ballastconfiguration.py"
echo call pyside2-uic widget_ballastsolver.ui -o "..\src\DAVE\gui\forms\widgetUI_ballastsolver.py"
echo call pyside2-uic widget_airy.ui -o "..\src\DAVE\gui\forms\widgetUI_airy.py"
echo call pyside2-uic widget_stability_displ.ui -o "..\src\DAVE\gui\forms\widget_stability_displUI.py"
call pyside2-uic widget_explore.ui -o "..\src\DAVE\gui\forms\widgetUI_explore.py"
call pyside2-uic widget_tank_order.ui -o "..\src\DAVE\gui\forms\widgetUI_tank_order.py"

echo call pyside2-rcc ..\guis\resources.qrc -o "..\src\DAVE\forms\resources_rc.py"

echo call pyside2-uic main_form.ui -o "..\src\DAVE\forms\viewer_form.py"

call pyside2-uic widget_waveinteraction.ui -o "..\src\DAVE\forms\widget_waveinteraction.py"
echo call pyside2-uic widget_axis.ui -o "..\src\DAVE\forms\widget_axis.py"
echo call pyside2-uic widget_body.ui -o "..\src\DAVE\forms\widget_body.py"
echo call pyside2-uic widget_poi.ui -o "..\src\DAVE\forms\widget_poi.py"
echo call pyside2-uic widget_cable.ui -o "..\src\DAVE\forms\widget_cable.py"
echo call pyside2-uic addnode_form.ui -o "..\src\DAVE\forms\addnode_form.py"
echo call pyside2-uic widget_name.ui -o "..\src\DAVE\forms\widget_name.py"
echo call pyside2-uic widget_visual.ui -o "..\src\DAVE\forms\widget_visual.py"
echo call pyside2-uic widget_force.ui -o "..\src\DAVE\forms\widget_force.py"
echo call pyside2-uic widget_force.ui -o "..\src\DAVE\forms\widget_force.py"
echo call pyside2-uic widget_sheave.ui -o "..\src\DAVE\forms\widget_sheave.py"
echo call pyside2-uic widget_linhyd.ui -o "..\src\DAVE\forms\widget_linhyd.py"
echo call pyside2-uic widget_lincon6.ui -o "..\src\DAVE\forms\widget_lincon6.py"
echo call pyside2-uic widget_beam.ui -o "..\src\DAVE\forms\widget_beam.py"
echo call pyside2-uic widget_con2d.ui -o "..\src\DAVE\forms\widget_con2d.py"
echo call pyside2-uic frm_standard_assets.ui -o "..\src\DAVE\forms\frm_standard_assets.py"
echo call pyside2-uic dlg_solver.ui -o "..\src\DAVE\forms\dlg_solver.py"
echo call pyside2-uic frm_animation.ui -o "..\src\DAVE\forms\frm_animation.py"
echo call pyside2-uic widget_dynprop.ui -o "..\src\DAVE\forms\widget_dynprop.py"


call pyside2-rcc resources.qrc -o "..\src\DAVE\forms\resources_rc.py"