﻿#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Created on 2017.7.10

@author: Sam
'''

from maya import cmds


def doIt(rl=False):
    
    if rl: 
        cmds.optionVar(rm="PutaoTools_Project")
        currentMode = cmds.setMenuMode()
        cmds.setMenuMode(currentMode)
    
    try: 
        import barbarian.utils
        if rl: reload(barbarian.utils)
        import barbarian.utils.config
        if rl: reload(barbarian.utils.config)
        import barbarian.utils.ui
        if rl: 
            barbarian.utils.ui.QtUI.cleanUp()
            reload(barbarian.utils.ui)
        import barbarian.utils.ui.PuTaoMainUI
        if rl: reload(barbarian.utils.ui.PuTaoMainUI)
        import barbarian.utils.ui.playblastOptionUI
        if rl: reload(barbarian.utils.ui.playblastOptionUI)
        import barbarian.utils.ui.motionLibUI
        if rl: reload(barbarian.utils.ui.motionLibUI)
        import barbarian.utils.ui.resourceLibUI
        if rl: reload(barbarian.utils.ui.resourceLibUI)
        import barbarian.utils.main
        if rl: reload(barbarian.utils.main)
        import barbarian.utils.ui.CGTWUI
        if rl: reload(barbarian.utils.ui.CGTWUI)
        
        import barbarian.cgtw
        if rl: reload(barbarian.cgtw)
        import barbarian.cgtw.database
        if rl: reload(barbarian.cgtw.database)
        import barbarian.cgtw.model
        if rl: reload(barbarian.cgtw.model)
        import barbarian.cgtw.delegate
        if rl: reload(barbarian.cgtw.delegate)
        
        import barbarian.model
        if rl: reload(barbarian.model)
        import barbarian.model.renamer
        if rl: reload(barbarian.model.renamer)
        import barbarian.model.checkModel
        if rl: reload(barbarian.model.checkModel)
        import barbarian.model.RemoveNamespace
        if rl: reload(barbarian.model.RemoveNamespace)
        import barbarian.model.turntable
        if rl: reload(barbarian.model.turntable)
        
        import barbarian.rig
        if rl: reload(barbarian.rig)
        import barbarian.rig.copySkin
        if rl: reload(barbarian.rig.copySkin)
        import barbarian.rig.blendShapeMel.blendShapeManage
        if rl: reload(barbarian.rig.blendShapeMel.blendShapeManage)
        
        import barbarian.anim
        if rl: reload(barbarian.anim)
        import barbarian.anim.playblast
        if rl: reload(barbarian.anim.playblast)
        import barbarian.anim.motionLib
        if rl: reload(barbarian.anim.motionLib)
        import barbarian.anim.resourceLib
        if rl: reload(barbarian.anim.resourceLib)
        import barbarian.anim.CreateProjectCamera
        if rl: reload(barbarian.anim.CreateProjectCamera)
        import barbarian.anim.poseLibModule
        if rl: reload(barbarian.anim.poseLibModule)
        
        import barbarian.render
        if rl: reload(barbarian.render)
        import barbarian.render.selectObjectType
        if rl: reload(barbarian.render.selectObjectType)
        import barbarian.render.AttributeSetter
        if rl: reload(barbarian.render.AttributeSetter)
        import barbarian.render.RenderSetting
        if rl: reload(barbarian.render.RenderSetting)
        
        import barbarian.fx
        if rl: reload(barbarian.fx)
        
        import SoftClusterEX
        if rl: reload(SoftClusterEX)
        
    except Exception, e: cmds.confirmDialog(message=u'加载异常：%s'%e, title=u"PuTao", icon="critical")
    
    if rl: barbarian.tool.__refreshUI__()
