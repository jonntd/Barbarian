﻿'''
Created on 2017.6.9

@author: Sam
'''

import pymel.core as pm
import barbarian.model
import barbarian.rig
import barbarian.anim
import barbarian.render
import barbarian.fx
import barbarian.utils

class Entrance(object):
    '''
    --------------------------------------------------------------------------------
    Class Representing the Entrance UI
    --------------------------------------------------------------------------------
    '''
    
    def __init__(self, layout):
        
        if pm.control("itBtn", exists=True):
            pm.deleteUI("itBtn")
        
        from barbarian.utils import getPath, getHelp, kIcon
        
        self.widget = None
        self.layout = layout
        self.button = pm.iconTextButton("itBtn",
            style="iconAndTextHorizontal",
            image=getPath(kIcon, "logo.jpg"), 
            width=80, flat=0, parent=layout, 
            backgroundColor=[.2,.2,.2], command=pm.Callback(getHelp))
        
        currentMode = pm.setMenuMode()
        
        pm.scriptJob(event=["MenuModeChanged", self.__build__], parent=self.button)
        self.__build__()
    
        state_dic = {"modelingMenuSet": (currentMode == "modelingMenuSet"),
                     "riggingMenuSet": (currentMode == "riggingMenuSet"),
                     "animationMenuSet": (currentMode == "animationMenuSet"),
                     "renderingMenuSet": (currentMode == "renderingMenuSet"),
                     "dynamicsMenuSet": (currentMode == "dynamicsMenuSet")}
    
        pm.popupMenu(parent=self.button)
        pm.menuItem(label=u'模型', radioButton=state_dic["modelingMenuSet"],
                    command=lambda *args: pm.setMenuMode("modelingMenuSet"))
        pm.menuItem(label=u'绑定', radioButton=state_dic["riggingMenuSet"],
                    command=lambda *args: pm.setMenuMode("riggingMenuSet"))
        pm.menuItem(label=u'动画', radioButton=state_dic["animationMenuSet"],
                    command=lambda *args: pm.setMenuMode("animationMenuSet"))
        pm.menuItem(label=u'渲染', radioButton=state_dic["renderingMenuSet"],
                    command=lambda *args: pm.setMenuMode("renderingMenuSet"))
        pm.menuItem(label=u'特效', radioButton=state_dic["dynamicsMenuSet"],
                    command=lambda *args: pm.setMenuMode("dynamicsMenuSet"))
        
    def __build__(self):
        
        from barbarian.utils import getPath, kUI
        
        currentMode = pm.setMenuMode()
        mi_dic = {"modelingMenuSet": u"[模型]",
                  "riggingMenuSet": u"[绑定]",
                  "animationMenuSet": u"[动画]",
                  "renderingMenuSet": u"[渲染]",
                  "dynamicsMenuSet": u"[特效]"}
        
        if not currentMode in mi_dic:
            return
        
        if pm.control("Form", exists=True):
            pm.deleteUI("Form")
        try:
            self.widget = pm.loadUI(f=getPath(kUI, "%s.ui" % currentMode))
            width = pm.control(self.widget, q=True, width=True)
            pm.control(self.widget, e=True, parent=self.layout, width=width)
            pm.shelfLayout(self.layout, e=True, position=(self.button, 1))
            pm.shelfLayout(self.layout, e=True, position=(self.widget, 2))
        except:
            self.widget = None
        
        #To fix a control refresh bug
        pm.control(self.button, e=True, manage=False)
        pm.iconTextButton(self.button, e=True, manage=True, label=mi_dic[currentMode])

'''
--------------------------------------------------------------------------------
Tool Initialization at Maya Startup
--------------------------------------------------------------------------------
'''
#initialize plugins
plugins = ["pyPBMpegCmd", "CustomDeformers"]
try:
    for i in plugins:
        pm.loadPlugin(i)
except:
    pass

#initialize entrance
if not pm.shelfLayout("PuTao", exists=True):
    pm.mel.eval("addNewShelfTab \"PuTao\";")
Entrance(pm.shelfLayout("PuTao", q=True, fpn=True))

print u"╔══════════════════════════════════════════════════════════╗"
print u"╟────────── PUTAOTOOLS INITIALIZATION COMPLETED ───────────╢"
print u"╚══════════════════════════════════════════════════════════╝"
