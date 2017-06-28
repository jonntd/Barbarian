import barbarian.model.renamer
import barbarian.model.checkModel
import barbarian.model.RemoveNamespace

import pymel.core as pm
from barbarian.utils import *


class Renamer(object):
    '''
    --------------------------------------------------------------------------------
    Class Representing the Rename Tool
    --------------------------------------------------------------------------------
    '''
    win              = "renamerWin"
    searchTextField  = "searchInput"
    replaceTextField = "replaceInput"
    renameTextField  = "middleInput"
    prefixTextField  = "prefixInput"
    suffixTextField  = "suffixInput"
    prefixOptionMenu = "prefixCmb"
    
    def __init__(self):
        if pm.window(Renamer.win, exists=True):
            pm.deleteUI(Renamer.win)
        
        pm.loadUI(f=getPath(kUI, "renamer.ui"))
        pm.showWindow(Renamer.win)
    
    @classmethod
    def rename(cls):

        prefix_dic = {"Middle": "M", "Left": "L", "Right": "R", "Up": "U",
                     "Down": "D", "Front": "F", "Back": "B"}
    
        dag_type_dic = {"mesh": "Geo",
                        "nurbsSurface": "Nbs",
                        "joint": "Jnt",
                        "clusterHandle": "Cus",
                        "multiplyDivide": "Mul",
                        "plusMinusAverage": "Pma",
                        "locator": "Loc",
                        "distanceDimShape": "Dis",
                        "parentConstraint": "Pat",
                        "orientConstraint": "Oct",
                        "pointConstraint": "Pot",
                        "aimConstraint": "Aim",
                        "poleVectorConstraint": "Pvc",
                        "transform": "GRP",
                        "lattice": "Lie",
                        "baseLattice": "Ble",
                        "ikHandle": "Ikh",
                        "ikEffector": "Ike",
                        "nurbsCurve": "Crv",
                        "deformSine": "Sin",
                        "deformBend": "Ben", }
    
        dg_type_dic = {"aiStandard": "Ais",
                       "aiSkin": "Sss",
                       "aiAmbientOcclusion": "Aao",
                       "aiUtility": "Aut",
                       "lambert": "Lam",
                       "blinn": "Bli",
                       "surfaceShader": "Sfs", }
    
        sels = pm.ls(sl=True)
        
        name = pm.textField(cls.renameTextField, q=True, tx=True)
        options = pm.optionMenu(cls.prefixOptionMenu, q=True, v=True)
    
        for sel in sels:
    
            pick_walk = pm.pickWalk(sel, d="down")
            pm.select(sel)
            obj_type = pm.objectType(pick_walk)
    
            num = 1
            new_name = ""
            num_str = "%02d" % num
    
            prefix = prefix_dic[options] + "_"
            tmp_dic = dag_type_dic
            
            for key in dg_type_dic:
                if key == obj_type:
                    prefix = ""
                    tmp_dic = dg_type_dic
                    break
                
            try: suffix = "_" + num_str + "_" + tmp_dic[obj_type]
            except: continue
            
            new_name = prefix + name + suffix
    
            while pm.objExists(new_name) and new_name != sel:
                num = num + 1
                num_str = "%02d" % num
                new_name = prefix + name + "_" + \
                    num_str + "_" + tmp_dic[obj_type]
    
            pm.rename(sel, new_name)
        
    @classmethod
    def addPrefix(cls):
        sels = pm.ls(sl=True)
        name = pm.textField(cls.prefixTextField, q=True, tx=True)
        
        for sel in sels:
            pm.rename(sel, name+"_"+sel)
        
    @classmethod
    def addSuffix(cls):
        sels = pm.ls(sl=True)
        name = pm.textField(cls.suffixTextField, q=True, tx=True)
        
        for sel in sels:
            pm.rename(sel, sel+"_"+name)
            
    @classmethod
    def search(cls):
        find_string = pm.textField(cls.searchTextField, q=True, text=True)
        matches = pm.ls("*" + find_string + "*", type="transform")
        pm.select(matches, r=True)
    
    @classmethod
    def replace(cls):
        find_string = pm.textField(cls.searchTextField, q=True, text=True)
        replace_string = pm.textField(cls.replaceTextField, q=True, text=True)
        matches = pm.ls(sl=True)
        
        for match in matches:
            new_name = match.split("|")[-1].replace(find_string, replace_string)
            pm.rename(match, new_name)


