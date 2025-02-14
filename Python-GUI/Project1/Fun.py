#!/usr/bin/env python
#coding=utf-8
#此文件由PyMe自动生成，如需要手动编写，请鼠标右键点击左边锁定标记，在弹出菜单中取消锁定。
import os
from   os.path import abspath, dirname
import shutil
import tkinter
import time
import requests
import threading
from   pathlib import Path
import pyautogui
from   tkinter import *
import tkinter.ttk
import tkinter.font
import tkinter.simpledialog
from PIL import Image,ImageTk
from ctypes import windll, byref, create_unicode_buffer, create_string_buffer
import zipfile
import math
import json
import re
zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
file_path = os.path.abspath(__file__)
G_ExeDir = os.path.dirname(file_path)
G_ResDir =  os.path.join(G_ExeDir,"Resources")
G_UIElementDictionary={}
G_UICommandDictionary={}
G_UIElementPlaceDictionary={}
G_UIElementUserDataArray={}
G_UIElementVariableArray={}
G_UIElementIconDictionary={}
G_UIInputDataArray={} 
G_UIElementAliasDictionary={}
G_UIGroupDictionary={}
G_UIStyleDictionary={}
G_CanvasSizeDictionary={}
G_CanvasShapeDictionary={}
G_CanvasParamDictionary={}
G_CanvasFontDictionary={}
G_CanvasImageDictionary={}
G_CanvasPointDictionary={}
G_CanvasEventDictionary={}
G_RootSize=None
G_UserVarDict={}
def IsInt(text):
    """是否是整数字符串"""
    if text.isdigit() == True:
        return True
    return False
def IsFloat(text):
    """是否是浮点字符中"""
    if text.count('.') == 1:
        left = text.split('.')[0]
        right = text.split('.')[1]
        lright = ''
        if left.count('-') == 1 and left[0] == '-':
            lright = left.split('-')[1]
        elif left.count('-') == 0:
            lright = left
        if right.isdigit() and lright.isdigit():
            return True
    return False
def IsNumeric(text):
    """是否是数字字符串"""
    if IsInt(text) == True or IsFloat(text) == True:
        return True
    return False
def CheckSpecialChar(text):
    """是否包含特殊字符"""
    string = '~!@#$%^&*()+-*/<>,.[]、‘’\'"{\}/^'
    for i in string:
        if i in text:
            return True
    return False
def IsMobilePhone(text):
    """是否是手机号"""
    ret = re.match(r"^1[35789]\d{9}$", text)
    if ret:
        return True
    return False
def IsEmail(text):
    """是否是Email"""
    index1 = text.find('@')
    index2 = text.find('.')
    if index1 == -1:
        return False
    elif index2 == -1:
        return False
    elif index2 < index1:
        return False
    elif index2 == len(text)-1:
        return False
    return True
G_ResourcesFileList={}
G_CutContent=None
def Register(uiName,elementName,element,alias=None,groupName=None,styleName=None):
    """注册一个控件,用于记录它:参数1 :界面类名, 参数2:控件名称,参数3 :控件。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UICommandDictionary
    global G_UIElementPlaceDictionary
    global G_UIGroupDictionary
    global G_UIStyleDictionary
    global G_CanvasSizeDictionary
    global G_CanvasShapeDictionary
    global G_CanvasParamDictionary
    global G_CanvasFontDictionary
    global G_CanvasImageDictionary
    global G_CanvasEventDictionary
    global G_CanvasPointDictionary
    global G_UIElementVariableArray
    global G_UIElementIconDictionary
    if uiName not in G_UIElementDictionary:
        G_UIElementDictionary[uiName]={}
        G_UICommandDictionary[uiName]={}
        G_UIElementAliasDictionary[uiName]={}
        G_UIElementPlaceDictionary[uiName]={}
        G_UIGroupDictionary[uiName]={}
        G_UIStyleDictionary[uiName]={}
        G_CanvasSizeDictionary[uiName]={}
        G_CanvasShapeDictionary[uiName]={}
        G_CanvasParamDictionary[uiName]={}
        G_CanvasFontDictionary[uiName]={}
        G_CanvasImageDictionary[uiName]={}
        G_CanvasEventDictionary[uiName]={}
        G_CanvasPointDictionary[uiName]={}
        G_UIElementVariableArray[uiName]={}
        G_UIElementIconDictionary[uiName]={}
        G_UIElementIconDictionary[uiName]['MainMenu'] = {}
        G_UIElementIconDictionary[uiName]['SysTray'] = {}
    G_UIElementDictionary[uiName][elementName]=element
    if alias:
        G_UIElementAliasDictionary[uiName][alias]=elementName
    if groupName:
        G_UIGroupDictionary[uiName][elementName]=groupName
    if styleName:
        G_UIStyleDictionary[uiName][elementName]=styleName
    if elementName.find('TreeView_') >= 0:
        G_UIElementIconDictionary[uiName][elementName]={}
def PlayDestroyDialogAction(uiName,result,topLevel,animation='zoomout'):
    def FadeOut(topLevel,alpha):
        try :
            import ctypes
            from ctypes import windll
            hwnd = windll.user32.GetParent(topLevel.winfo_id())
            _winlib = ctypes.windll.user32
            style = _winlib.GetWindowLongA( hwnd, 0xffffffec ) | 0x00080000
            _winlib.SetWindowLongA( hwnd, 0xffffffec, style )
            _winlib.SetLayeredWindowAttributes( hwnd, 0, alpha+1, 2 )
            alpha = alpha - 1
        except ImportError:
            pass
        if alpha > 0:
            topLevel.after(1,lambda:FadeOut(topLevel = topLevel,alpha = alpha))
        else:
            DestroyUI(uiName,result)
            print("结束")
    def ZoomOut(topLevel,zoom,win_x,win_y,win_width,win_height):
        try :
            center_x = win_x + int(win_width/2)
            center_y = win_y + int(win_height/2)
            zw = int(win_width * zoom)
            zh = int(win_height * zoom)
            zx = center_x - int(zw/2)
            zy = center_y - int(zh/2)
            topLevel.geometry('%dx%d+%d+%d'%(zw,zh,zx,zy))
            zoom = zoom - 0.01
        except ImportError:
            pass
        if zoom > 0.0:
            topLevel.after(1,lambda:ZoomOut(topLevel = topLevel,zoom = zoom ,win_x = win_x,win_y = win_y,win_width=win_width,win_height=win_height))
        else:
            DestroyUI(uiName,result)
            print("结束")
    if animation == "fadeout":
        try :
            import ctypes
            from ctypes import windll
            hwnd = windll.user32.GetParent(topLevel.winfo_id())
            _winlib = ctypes.windll.user32
            style = _winlib.GetWindowLongA( hwnd, 0xffffffec ) | 0x00080000
            _winlib.SetWindowLongA( hwnd, 0xffffffec, style )
            _winlib.SetLayeredWindowAttributes( hwnd, 0, 0, 2 )
            topLevel.deiconify()
            topLevel.after(1,lambda:FadeOut(topLevel = topLevel,alpha = 255))
        except ImportError:
            pass
    elif animation == "zoomout":
        try :
            win_x = topLevel.winfo_x()
            win_y = topLevel.winfo_y()
            win_width = topLevel.winfo_width()
            win_height = topLevel.winfo_height()
            topLevel.after(1,lambda:ZoomOut(topLevel = topLevel,zoom = 1.0,win_x = win_x,win_y = win_y,win_width=win_width,win_height=win_height))
        except ImportError:
            pass
def DestroyUI(uiName,result=0,animation=''):
    """销毁一个界面:参数1 :界面类名,参数2:CallUIDialog返回值"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UICommandDictionary
    global G_UIElementPlaceDictionary
    global G_UIGroupDictionary
    global G_UIStyleDictionary
    global G_CanvasSizeDictionary
    global G_CanvasShapeDictionary
    global G_CanvasParamDictionary
    global G_CanvasFontDictionary
    global G_CanvasImageDictionary
    global G_CanvasEventDictionary
    global G_CanvasPointDictionary
    global G_UIElementIconDictionary
    global G_UIInputDataArray
    if uiName in G_UIElementDictionary:
        GetUIDataDictionary(uiName)
        root = GetElement(uiName,"root")
        if root is not None:
            animation = animation.lower()
            if animation != '':
                PlayDestroyDialogAction(uiName,result,root,animation)
                return
            try:
                root.destroy()
            except:
                pass
        G_UIElementDictionary.pop(uiName)
        G_UICommandDictionary.pop(uiName)
        G_UIElementAliasDictionary.pop(uiName)
        G_UIElementPlaceDictionary.pop(uiName)
        G_UIGroupDictionary.pop(uiName)
        G_UIStyleDictionary.pop(uiName)
        G_CanvasSizeDictionary.pop(uiName)
        G_CanvasShapeDictionary.pop(uiName)
        G_CanvasParamDictionary.pop(uiName)
        G_CanvasFontDictionary.pop(uiName)
        G_CanvasImageDictionary.pop(uiName)
        G_CanvasEventDictionary.pop(uiName)
        G_CanvasPointDictionary.pop(uiName)
        G_UIElementIconDictionary.pop(uiName)
        G_UIInputDataArray['result'] = result
def GetElement(uiName,elementName):
    """取得控件:参数1 :界面类名, 参数2:控件名称。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary:
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            return G_UIElementDictionary[uiName][elementName]
        if elementName.find("TreeView") >= 0:
            elementName = elementName.replace("TreeView","ListView")
            if elementName in G_UIElementDictionary[uiName]:
                return G_UIElementDictionary[uiName][elementName]
    return None
def GetElementName(element):
    """取得控件的界面类名与控件名称:参数1 :控件"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    for uiName in G_UIElementDictionary:
        for elementName in G_UIElementDictionary[uiName]:
            if G_UIElementDictionary[uiName][elementName] == element:
                return uiName,elementName
    return None,None
def GetElementType(uiName,elementName):
    """取得控件类型:参数1 :界面类名, 参数2:控件名称。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary:
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            splitArray = elementName.split('_')
            return splitArray[0] 
    return None
def GetElementXYWH(uiName,elementName):
    """取得控件所在矩形"""
    element = GetElement(uiName,elementName)
    if element:
        x = element.winfo_x()
        y = element.winfo_y()
        width = element.winfo_width()
        height = element.winfo_height()
        return (x,y,width,height)
    return None
def AddTKVariable(uiName,elementName,defaultValue = None):
    """为控件增加一个Tkinter的内置控件变量,参数1 :界面类名, 参数2:控件名称,参数3:默认值。"""
    global G_UIElementVariableArray
    if uiName not in G_UIElementVariableArray:
        G_UIElementVariableArray[uiName]={}
    NameLower = elementName.lower()
    if NameLower.find('combobox_') >= 0:
        G_UIElementVariableArray[uiName][elementName]=tkinter.IntVar()
    elif NameLower.find('group_') >= 0:
        G_UIElementVariableArray[uiName][elementName]=tkinter.IntVar()
    elif NameLower.find('checkbutton_') >= 0:
        G_UIElementVariableArray[uiName][elementName]=tkinter.BooleanVar()
    else:
        G_UIElementVariableArray[uiName][elementName]=tkinter.StringVar()
    if defaultValue:
        G_UIElementVariableArray[uiName][elementName].set(defaultValue) 
    return G_UIElementVariableArray[uiName][elementName]
def SetTKVariable(uiName,elementName,value):
    """设置控件的tkinter变量.参数1 :界面类名, 参数2:控件名称,参数3:值。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementVariableArray:
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName]
        if elementName in G_UIElementVariableArray[uiName]:
            G_UIElementVariableArray[uiName][elementName].set(value)
        if elementName in G_UIGroupDictionary[uiName]:
            GroupName = G_UIGroupDictionary[uiName][elementName]
            if GroupName in G_UIElementVariableArray[uiName]:
                G_UIElementVariableArray[uiName][GroupName].set(value)
def GetTKVariable(uiName,elementName):
    """取得控件的tkinter变量.参数1 :界面类名, 参数2:控件名称。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementVariableArray:
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName]
        if elementName in G_UIElementVariableArray[uiName]:
            return G_UIElementVariableArray[uiName][elementName].get()
        if elementName in G_UIGroupDictionary[uiName]:
            GroupName = G_UIGroupDictionary[uiName][elementName]
            if GroupName in G_UIElementVariableArray[uiName]:
                return G_UIElementVariableArray[uiName][GroupName].get()
    return None
def AddUserData(uiName,elementName,dataName,datatype,datavalue,isMapToText = 0):
    """为控件添加一个用户数据,参数1 :界面类名, 参数2:控件名称,参数3:dataname为数据名,datatype为数据类型,可以包括int、float、string、list、dictionary等,一般在设计软件中用鼠标右键操作控件,在弹出的“绑定数据”对话枉中设置,参数4:datavalue为数据值,而ismaptotext则是是否将数据直接反映到控件的text变量中。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementUserDataArray
    if uiName not in G_UIElementUserDataArray:
        G_UIElementUserDataArray[uiName]={} 
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if elementName not in G_UIElementUserDataArray[uiName]:
        G_UIElementUserDataArray[uiName][elementName]=[]
    else:
        for EBData in G_UIElementUserDataArray[uiName][elementName]:
            if EBData[0] == dataName:
                EBData[1] = datatype
                EBData[2] = datavalue
                EBData[3] = isMapToText
                if EBData[3] == 1:
                    SetText(uiName,elementName,datavalue) 
                return
    G_UIElementUserDataArray[uiName][elementName].append([dataName,datatype,datavalue,isMapToText])
def DelUserData(uiName,elementName,dataName):
    """删除一个用户变量"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementUserDataArray
    if uiName in G_UIElementUserDataArray:
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName]
        if elementName in G_UIElementUserDataArray[uiName]:
            dataIndex = 0
            for EBData in G_UIElementUserDataArray[uiName][elementName]:
                if EBData[0] == dataName:
                    G_UIElementUserDataArray[uiName][elementName].pop(dataIndex)
                    return 
                dataIndex = dataIndex + 1
def SetUserData(uiName,elementName,dataName,datavalue):
    """设置控件的用户数据值。参数1 :界面类名, 参数2:控件名称,参数3:dataname为数据名,参数4:datavalue为数据值。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementUserDataArray
    if uiName in G_UIElementUserDataArray:
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName]
        if elementName in G_UIElementUserDataArray[uiName]:
            for EBData in G_UIElementUserDataArray[uiName][elementName]:
                if EBData[0] == dataName:
                    EBData[2] = datavalue
                    if EBData[3] == 1:
                        SetText(uiName,elementName,datavalue) 
                    return
def GetUserData(uiName,elementName,dataName):
    """取得控件的用户数据值。参数1 :界面类名, 参数2:控件名称,参数3:dataname为数据名。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementUserDataArray
    if  uiName in G_UIElementUserDataArray:
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName]
        if elementName in G_UIElementUserDataArray[uiName]:
            for EBData in G_UIElementUserDataArray[uiName][elementName]:
                if EBData[0] == dataName:
                    if EBData[1]=='int':
                        return int(EBData[2])
                    elif EBData[1]=='float':
                        return float(EBData[2])
                    else:
                        return EBData[2]
    return None
def SetTKAttrib(uiName,elementName,AttribName,attribValue):
    """设置控件的tkinter属性值。参数1 :界面类名, 参数2:控件名称,参数3:AttribName为属性名,参数4:attribValue为数据值。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName]
        if AttribName in G_UIElementDictionary[uiName][elementName].configure().keys():
            G_UIElementDictionary[uiName][elementName][AttribName]=attribValue
def GetTKAttrib(uiName,elementName,AttribName):
    """获取控件的tkinter属性值。参数1 :界面类名, 参数2:控件名称,参数3:AttribName为属性名。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName]
        return G_UIElementDictionary[uiName][elementName].cget(AttribName)
def SetElementVisible(uiName,elementName,Visible):
    """设置控件显示或隐藏（旧函数，请使用SetVisible）"""
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    G_UIElementPlaceDictionary[uiName][elementName]["visible"] = Visible
    if Visible == True :
        Control = GetElement(uiName,elementName)
        if hasattr(Control,"GetWidget") == True:
            Control = Control.GetWidget()
        if G_UIElementPlaceDictionary[uiName][elementName]["type"] == "pack":
            fill = G_UIElementPlaceDictionary[uiName][elementName]["fill"]
            side = G_UIElementPlaceDictionary[uiName][elementName]["side"]
            padx = G_UIElementPlaceDictionary[uiName][elementName]["padx"]
            pady = G_UIElementPlaceDictionary[uiName][elementName]["pady"]
            expand = G_UIElementPlaceDictionary[uiName][elementName]["expand"]
            SetControlPack(uiName,elementName,fill,side,padx,pady,expand)
        elif G_UIElementPlaceDictionary[uiName][elementName]["type"] == "grid":
            row = G_UIElementPlaceDictionary[uiName][elementName]["row"]
            column = G_UIElementPlaceDictionary[uiName][elementName]["column"]
            rowspan = G_UIElementPlaceDictionary[uiName][elementName]["rowspan"]
            columnspan = G_UIElementPlaceDictionary[uiName][elementName]["columnspan"]
            SetControlGrid(uiName,elementName,row,column,rowspan,columnspan)
        elif G_UIElementPlaceDictionary[uiName][elementName]["type"] == "place":
            x = 0
            if "relx" in G_UIElementPlaceDictionary[uiName][elementName]:
                x = G_UIElementPlaceDictionary[uiName][elementName]["relx"]
            else:
                x = G_UIElementPlaceDictionary[uiName][elementName]["x"]
            y = 0
            if "rely" in G_UIElementPlaceDictionary[uiName][elementName]:
                y = G_UIElementPlaceDictionary[uiName][elementName]["rely"]
            else:
                y = G_UIElementPlaceDictionary[uiName][elementName]["y"]
            w = 0
            if "relwidth" in G_UIElementPlaceDictionary[uiName][elementName]:
                w = G_UIElementPlaceDictionary[uiName][elementName]["relwidth"]
            else:
                w = G_UIElementPlaceDictionary[uiName][elementName]["width"]
            h = 0
            if "relheight" in G_UIElementPlaceDictionary[uiName][elementName]:
                h = G_UIElementPlaceDictionary[uiName][elementName]["relheight"]
            else:
                h = G_UIElementPlaceDictionary[uiName][elementName]["height"]
            SetControlPlace(uiName,elementName,x,y,w,h)
    else:
        Control = GetElement(uiName,elementName)
        if hasattr(Control,"GetWidget") == True:
            Control = Control.GetWidget()
        if G_UIElementPlaceDictionary[uiName][elementName]["type"] == "pack":
            Control.pack_forget()
        elif G_UIElementPlaceDictionary[uiName][elementName]["type"] == "grid":
            Control.grid_forget()
        elif G_UIElementPlaceDictionary[uiName][elementName]["type"] == "place":
            Control.place_forget()
        G_UIElementPlaceDictionary[uiName][elementName]['visible'] = False
def SetVisible(uiName,elementName,Visible):
    """设置控件显示或隐藏"""
    SetElementVisible(uiName,elementName,Visible)
def SetElementEnable(uiName,elementName,Enable):
    """设置控件可用或无效（旧函数，请使用SetEnable）"""
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    element = GetElement(uiName,elementName)
    if hasattr(element,"GetWidget") == True:
        element = element.GetWidget()
    if Enable == True:
        element.configure(state='normal')
    else:
        element.configure(state='disabled')
def SetEnable(uiName,elementName,Enable):
    """设置控件可用或无效"""
    SetElementEnable(uiName,elementName,Enable)
def IsElementVisible(uiName,elementName):
    """取得控件显示或隐藏（旧函数，请使用IsVisible）"""
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    return G_UIElementPlaceDictionary[uiName][elementName]['visible']
def IsVisible(uiName,elementName):
    """取得控件显示或隐藏"""
    return IsElementVisible(uiName,elementName)
def IsElementEnable(uiName,elementName):
    """取得控件可用或无效（旧函数，请使用IsEnable）"""
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    ElementState = G_UIElementDictionary[uiName][elementName].cget('state')
    if ElementState == 'disabled':
        return False
    else:
        return True
def IsEnable(uiName,elementName):
    """取得控件可用或无效"""
    return IsElementEnable(uiName,elementName)
def SetText(uiName,elementName,textValue):
    """设置控件的文本(Label、Button、RadioButton、CheckButton、Entry、Text、ComboBox, SpinBox)。参数1 :界面类名, 参数2:控件名称,参数3:文本内容。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    showtext = str("%s"%textValue)
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementVariableArray:
        if elementName in G_UIElementVariableArray[uiName]:
            G_UIElementVariableArray[uiName][elementName].set(showtext)
            return
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName == "root":
                G_UIElementDictionary[uiName][elementName].title(textValue)
            elif elementName.find('Text_') >= 0:
                G_UIElementDictionary[uiName][elementName].delete('0.0',tkinter.END)
                if len(showtext) > 0:
                   G_UIElementDictionary[uiName][elementName].insert(tkinter.END,showtext)
            elif elementName.find('Entry_') >= 0:
                   G_UIElementDictionary[uiName][elementName].SetText(showtext)
            else:
                G_UIElementDictionary[uiName][elementName].configure(text=showtext)
def InsertText(uiName,elementName,position=tkinter.END,textValue=''):
    """在文本框插入文本"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    showtext = str("%s"%textValue)
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('Text_') >= 0:
                if len(showtext) > 0:
                   G_UIElementDictionary[uiName][elementName].insert(position,showtext)
def GetText(uiName,elementName):
    """获取控件的文本(Label、Button、RadioButton、CheckButton、Entry、Text、 ComboBox, SpinBox)。参数1 :界面类名, 参数2:控件名称。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('Text_') >= 0:
                return G_UIElementDictionary[uiName][elementName].get('0.0', tkinter.END)
            elif elementName.find('Spinbox_') >= 0:
                return str(G_UIElementDictionary[uiName][elementName].get())
            elif elementName.find('ComboBox_') >= 0:
                return str(G_UIElementDictionary[uiName][elementName].get())
            elif elementName.find('ListBox_') >= 0:
                currIndex = G_UIElementDictionary[uiName][elementName].curselection()
                if len(currIndex) > 0 and currIndex[0] >= 0:
                    return  G_UIElementDictionary[uiName][elementName].get(currIndex[0])
            elif elementName.find('Entry_') >= 0:
                if elementName in  G_UIElementVariableArray[uiName]:
                    text = G_UIElementVariableArray[uiName][elementName].get()
                else:
                    text = G_UIElementDictionary[uiName][elementName].GetText()
                return text
            else:
                if uiName in G_UIElementVariableArray:
                    if elementName in G_UIElementVariableArray[uiName]:
                        text = G_UIElementVariableArray[uiName][elementName].get()
                        return text
                return G_UIElementDictionary[uiName][elementName].cget('text')
    return str("")
def SetFont(uiName,elementName,fontName,fontSize,fontWeight='normal',fontSlant='roman',fontUnderline=0,fontOverstrike=0):
    """设置控件字体"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_CanvasFontDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            newFont = None
            if elementName in G_CanvasFontDictionary[uiName]:
                for fontInfo in G_CanvasFontDictionary[uiName][elementName]:
                    if fontInfo[1] == fontName and fontInfo[2] == str(fontSize) and fontInfo[3] == fontWeight and fontInfo[4] == fontSlant and fontInfo[5] == str(fontUnderline) and fontInfo[6] == str(fontOverstrike):
                        newFont = fontInfo[0]
                        break
            else:
                G_CanvasFontDictionary[uiName][elementName] = []
            if newFont is None:
                newFont = tkinter.font.Font(family=fontName, size=fontSize,weight=fontWeight,slant=fontSlant,underline=fontUnderline,overstrike=fontOverstrike)
            if elementName.find('Canvas_') < 0 and elementName.find('Form_') < 0:
                G_UIElementDictionary[uiName][elementName].configure(font=newFont)
            G_CanvasFontDictionary[uiName][elementName].append([newFont,fontName,str(fontSize),fontWeight,fontSlant,str(fontUnderline),str(fontOverstrike)])
def GetFont(uiName,elementName,fontName,fontSize,fontWeight='normal',fontSlant='roman',fontUnderline=0,fontOverstrike=0,createifnofind=False):
    """取得字体"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_CanvasFontDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName in G_CanvasFontDictionary[uiName]:
                for fontInfo in G_CanvasFontDictionary[uiName][elementName]:
                    if fontInfo[1] == fontName and fontInfo[2] == str(fontSize) and fontInfo[3] == fontWeight and fontInfo[4] == fontSlant and fontInfo[5] == str(fontUnderline) and fontInfo[6] == str(fontOverstrike):
                        return fontInfo[0]
            else:
                G_CanvasFontDictionary[uiName][elementName] = []
            if createifnofind == True:
                newFont = tkinter.font.Font(family=fontName, size=fontSize,weight=fontWeight,slant=fontSlant,underline=fontUnderline,overstrike=fontOverstrike)
                G_CanvasFontDictionary[uiName][elementName].append([newFont,fontName,str(fontSize),fontWeight,fontSlant,str(fontUnderline),str(fontOverstrike)])
                return newFont
    return None
def SetBGColor(uiName,elementName,RGBColor):
    """设置控件的背景色。参数1 :界面类名, 参数2:控件名称,参数3:背景颜色。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('Entry_') >= 0:
                G_UIElementDictionary[uiName][elementName].SetBGColor(RGBColor)
            else:
                G_UIElementDictionary[uiName][elementName].configure(bg=RGBColor)
def GetBGColor(uiName,elementName):
    """获取控件的背景色。参数1 :界面类名, 参数2:控件名称。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('Entry_') >= 0:
                return G_UIElementDictionary[uiName][elementName].GetBGColor()
            else:
                return G_UIElementDictionary[uiName][elementName].cget('bg')
    return None
def SetTextColor(uiName,elementName,RGBColor):
    """设置控件的文字色。参数1 :界面类名, 参数2:控件名称,参数3:文字颜色。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('Entry_') >= 0:
                G_UIElementDictionary[uiName][elementName].SetFGColor(RGBColor)
            else:
                G_UIElementDictionary[uiName][elementName].configure(fg=RGBColor)
def GetTextColor(uiName,elementName):
    """获取控件的文字色。参数1 :界面类名, 参数2:控件名称。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('Entry_') >= 0:
                return G_UIElementDictionary[uiName][elementName].GetFGColor()
            else:
                return G_UIElementDictionary[uiName][elementName].cget('fg')
    return None
def SetImage(uiName,elementName,imagePath,autoSize = True):
    """设置控件的背景图片(Label,Button,Text)。参数1 :界面类名, 参数2:控件名称,参数3:图片名称。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    global G_ResourcesFileList
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if elementName.find('Label_') == 0 or elementName.find('Button_') >= 0 :
        Control = GetElement(uiName,elementName)
        if Control != None:
            if uiName in G_UIElementUserDataArray:
                if elementName in G_UIElementUserDataArray[uiName]:
                    for EBData in G_UIElementUserDataArray[uiName][elementName]:
                        if EBData[0] == 'image':
                            EBData[1] = imagePath
                            from   PIL import Image,ImageTk
                            if os.path.exists(imagePath) == False:
                                if imagePath in G_ResourcesFileList:
                                   imagePath = G_ResourcesFileList[imagePath]
                                if os.path.exists(imagePath) == False:
                                    return
                            image=Image.open(imagePath).convert('RGBA')
                            if autoSize == True:
                                image_Resize = image.resize((Control.winfo_width(), Control.winfo_height()),Image.LANCZOS)
                            else:
                                image_Resize = image
                            EBData[2] = ImageTk.PhotoImage(image_Resize)
                            Control.configure(image = EBData[2])
                            return 
            from   PIL import Image,ImageTk
            if os.path.exists(imagePath) == False:
                if imagePath in G_ResourcesFileList:
                    imagePath = G_ResourcesFileList[imagePath]
                if os.path.exists(imagePath) == False:
                    return
            image=Image.open(imagePath).convert('RGBA')
            if autoSize == True:
                image_Resize = image.resize((Control.winfo_width(), Control.winfo_height()),Image.LANCZOS)
            else:
                image_Resize = image
            EBData2 = ImageTk.PhotoImage(image_Resize)
            AddUserData(uiName,elementName,'image',imagePath,EBData2,0)
            Control.configure(image = EBData2)
    if elementName.find('Text_') == 0:
        Control = GetElement(uiName,elementName)
        if Control != None:
            Control.delete('0.0',tkinter.END)
            from   PIL import Image,ImageTk
            if os.path.exists(imagePath) == False:
                if imagePath in G_ResourcesFileList:
                    imagePath = G_ResourcesFileList[imagePath]
                if os.path.exists(imagePath) == False:
                    return
            image=Image.open(imagePath).convert('RGBA')
            image_Resize = image.resize((Control.winfo_width(), Control.winfo_height()),Image.LANCZOS)
            EBData2 = ImageTk.PhotoImage(image_Resize)
            AddUserData(uiName,elementName,'image',imagePath,EBData2,0)
            Control.image_create(tkinter.END, image=EBData2)
def SetCanvasBGImage(uiName,elementName,imagePath,wrapType='Zoom'):
    """设置画布Canvas的背景图片。参数1 :界面类名, 参数2:画布名称,参数3:图片文件,参数4:绘图方式:Original为原始大小,Zoom为缩放匹配画布大小,Tiling为平铺满画布"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    global G_ResourcesFileList
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if elementName.find('Form_') == 0 or elementName.find('Canvas_') >= 0 :
        Control = GetElement(uiName,elementName)
        if Control != None:
            Control.delete('BGImage')
            if wrapType == "Zoom" :
                newImage = Image.open(imagePath).convert('RGBA')
                reSizeImage = newImage.resize((Control.winfo_width(), Control.winfo_height()),Image.LANCZOS)
                newPTImage = ImageTk.PhotoImage(reSizeImage)
                AddUserData(uiName,elementName,'BGImage',imagePath,newPTImage,0)
                Control.create_image(0,0,anchor=tkinter.NW,image=newPTImage,tag="BGImage")
            elif wrapType == "Tiling" :
                newImage = Image.open(imagePath).convert('RGBA')
                newPTImage = ImageTk.PhotoImage(newImage)
                AddUserData(uiName,elementName,'BGImage',imagePath,newPTImage,0)
                RepeatRow = int(Control.winfo_height() / newImage.height) + 1
                RepeatCow = int(Control.winfo_width() / newImage.width) + 1
                for r in range(RepeatRow):
                    for c in range(RepeatCow):
                        Control.create_image(c * newImage.width, r * newImage.height,anchor=tkinter.NW,image=newPTImage,tag="BGImage")
            else:
                newImage = Image.open(imagePath).convert('RGBA')
                newPTImage = ImageTk.PhotoImage(newImage)
                AddUserData(uiName,elementName,'BGImage',imagePath,newPTImage,0)
                Control.create_image(0,0,anchor=tkinter.NW,image=newPTImage,tag="BGImage")
        ReDrawCanvasShape(uiName,elementName)
def GetImage(uiName,elementName):
    """获取控件的背景图像文件(Label、Button)。参数1 :界面类名, 参数2:控件名称。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if elementName.find('Label_') == 0 or elementName.find('Button_') == 0 :
        Control = GetElement(uiName,elementName)
        if Control != None:
            if uiName in G_UIElementUserDataArray:
                if elementName in G_UIElementUserDataArray[uiName]:
                    for EBData in G_UIElementUserDataArray[uiName][elementName]:
                        if EBData[0] == 'image':
                            return EBData[1]
    return str("")
def LoadGIF(uiName,elementName,imagefile,w=0,h=0):
    """播放GIF动画"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    global G_ResourcesFileList
    newImage = None
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if elementName.find('Label_') == 0 or elementName.find('Button_') == 0 or elementName.find('RadioButton_') == 0 or elementName.find('CheckButton_') == 0:
        Control = GetElement(uiName,elementName)
        if Control != None:
            hasGIFAnimation = False
            if imagefile != None:
                resourPath = imagefile 
                if os.path.exists(resourPath) == False:
                    resourPath, imagefile = os.path.split(imagefile)
                    if imagefile in G_ResourcesFileList:
                        resourPath = G_ResourcesFileList[imagefile]
                if os.path.exists(resourPath) == True:
                    try:
                        if imagefile.find('.gif') >= 0:
                            GifData = Image.open(resourPath)
                            seq = []
                            try:
                                while 1:
                                    imageRGBA = GifData.copy().convert('RGBA')
                                    if newImage is None:
                                        newImage = imageRGBA
                                    if w > 0 and h > 0:
                                        resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
                                        newFrame = ImageTk.PhotoImage(resizeImage)
                                    else:
                                        newFrame = ImageTk.PhotoImage(imageRGBA)
                                    seq.append(newFrame)
                                    GifData.seek(len(seq))
                            except EOFError:
                                pass
                            delay = 100
                            try:
                                delay = GifData.info['duration']
                            except KeyError:
                                delay = 100
                            if delay == 0:
                                delay = 100
                            hasGIFAnimation = True
                            if elementName not in G_CanvasImageDictionary[uiName]:
                                G_CanvasImageDictionary[uiName][elementName] = []
                            G_CanvasImageDictionary[uiName][elementName].append([imagefile,[seq,delay,0],w,h])
                        else:
                            newImage = Image.open(resourPath).convert('RGBA')
                    except:
                        return newImage
                if hasGIFAnimation == True:
                    Control.after(100,updateGIFFrame(uiName))
    return newImage
def StopGIF(uiName,elementName):
    """停止GIF动画"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    global G_ResourcesFileList
    newImage = None
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if elementName.find('Label_') == 0 or elementName.find('Button_') == 0 or elementName.find('RadioButton_') == 0 or elementName.find('CheckButton_') == 0:
        Control = GetElement(uiName,elementName)
        if Control != None:
            Control.after_cancel(updateGIFFrame)
            if elementName in G_CanvasImageDictionary[uiName]:
                G_CanvasImageDictionary[uiName][elementName].clear()
def LoadImageToIconList(uiName,elementName,ItemName,imageFile):
    """加载控件的图像文件:参数1 :界面类名, 参数2:控件名称, 参数3:树项名称, 参数4:图片文件"""
    global G_ResourcesFileList
    if imageFile in G_ResourcesFileList:
        imagePath = G_ResourcesFileList[imageFile]
    if os.path.exists(imagePath) == True:
        image = ImageTk.PhotoImage(file = imagePath)
        G_UIElementIconDictionary[uiName][elementName][ItemName] = image
        return image
    return None
def SetItemBGColor(uiName,elementName,lineIndex,color):
    """设置选项背景色"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ComboBox_') >= 0 or elementName.find('ListBox_') >= 0:
                    G_UIElementDictionary[uiName][elementName].itemconfig(lineIndex, {'bg':'+color+'})
def SetItemFGColor(uiName,elementName,lineIndex,color):
    """设置选项文字色"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ComboBox_') >= 0 or elementName.find('ListBox_') >= 0:
                    G_UIElementDictionary[uiName][elementName].itemconfig(lineIndex, {'fg':'+color+'})
def AddItemText(uiName,elementName,text,lineIndex="end"):
    """增加当前ListBox和ComboBox的文字项内容。参数1 :界面类名, 参数2:控件名称 ,参数3:文本内容。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ComboBox_') >= 0:
                ValueArray = list(G_UIElementDictionary[uiName][elementName]['value'])
                if type(lineIndex)==type(1):
                    ValueArray.insert(lineIndex,text)
                else:
                   ValueArray.append(text)
                G_UIElementDictionary[uiName][elementName]['value'] = ValueArray
            elif elementName.find('ListBox_') >= 0:
                if type(lineIndex)==type(1):
                    G_UIElementDictionary[uiName][elementName].insert(lineIndex,text)
                else:
                    G_UIElementDictionary[uiName][elementName].insert(lineIndex, text)
def AddLineText(uiName,elementName,text,lineIndex="end",textTag=''):
    """为Text控件或ListBox控件增加一行文字:参数1 :界面类名, 参数2:控件名称, 参数3:文字内容,参数4:目标行号,参数5:标记名称"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('Text_') >= 0:
                if type(lineIndex)==type(1):
                    lineIndex = lineIndex + 1
                    if textTag != '':
                        G_UIElementDictionary[uiName][elementName].insert("%d.0"%lineIndex,text,textTag)
                    else:
                        G_UIElementDictionary[uiName][elementName].insert("%d.0"%lineIndex,text)
                else:
                    if textTag != '':
                        G_UIElementDictionary[uiName][elementName].insert(lineIndex,text,textTag)
                    else:
                        G_UIElementDictionary[uiName][elementName].insert(lineIndex,text)
            if elementName.find('ListBox_') >= 0:
                if type(lineIndex)==type(1):
                    if textTag != '' :
                        G_UIElementDictionary[uiName][elementName].insert("%d"%lineIndex, text,textTag)
                    else:
                        G_UIElementDictionary[uiName][elementName].insert("%d"%lineIndex, text)
                else:
                    if textTag != '':
                        G_UIElementDictionary[uiName][elementName].insert(lineIndex,text,textTag)
                    else:
                        G_UIElementDictionary[uiName][elementName].insert(lineIndex,text)
def AddPage(uiName,elementName,text,iconFile="",targetUIName=''):
    """增加选项页:参数1 :界面类名, 参数2:控件名称, 参数3:页面标题,参数4:页面图标,参数5:目标界面或文件"""
    global G_ResourcesFileList
    NoteBook = GetElement(uiName,elementName)
    PageFrame = tkinter.Frame(NoteBook)
    PageFrame.place(relx = 0.0,rely = 0.0,relwidth = 1.0,relheight = 1.0)
    PageFrame.configure(bg='red')
    if targetUIName and len(targetUIName) > 0:
        try:
            uiClass = targetUIName
            if targetUIName.find(".py") > 0:
                UIPath, UIFile = os.path.split(targetUIName)
                if UIPath.find(":") < 0:
                    UIPath = os.path.join(G_ExeDir,UIPath)
                import sys
                sys.path.append(UIPath)
                uiClass, extension = os.path.splitext(UIFile)
            import importlib
            from   importlib import import_module
            importModule = importlib.import_module(uiClass)
            importModule = importlib.reload(importModule)
            if hasattr(importModule,"Fun") == True:
                importModule.Fun.G_ExeDir = G_ExeDir
                importModule.Fun.G_ResDir = G_ResDir
                if hasattr(importModule,"EXUIControl") == True:
                    importModule.EXUIControl.G_ExeDir = G_ExeDir
                    importModule.EXUIControl.G_ResDir = G_ResDir
            if uiClass.find('Modules.') == 0:
                LibNameArray =  uiClass.partition("Modules.")
                uiClass = LibNameArray[2]
                newClass = getattr(importModule, uiClass)
            else:
                newClass = getattr(importModule, uiClass)
            newClassInstance = newClass(PageFrame,False)
        except Exception as ex:
            MessageBox(ex)
    if len(iconFile) > 0 and os.path.exists(iconFile) == True:
        if elementName not in G_UIElementIconDictionary[uiName]:
            G_UIElementIconDictionary[uiName][elementName]= {}
        G_UIElementIconDictionary[uiName][elementName][text] = ImageTk.PhotoImage(file=iconFile) 
        NoteBook.add(PageFrame,text = text,image=G_UIElementIconDictionary[uiName][elementName][text],compound="left")
    else:
        NoteBook.add(PageFrame,text = text)
def SelectPage(uiName,elementName,index=0):
    """选中选项页:参数1 :界面类名, 参数2:控件名称, 参数3:页面索引"""
    NoteBook = GetElement(uiName,elementName)
    Pages = NoteBook.winfo_children()
    if index >= 0 and index < len(Pages):
        NoteBook.select(index)
def HidePage(uiName,elementName,index=0):
    """隐藏选项页:参数1 :界面类名, 参数2:控件名称, 参数3:页面索引"""
    NoteBook = GetElement(uiName,elementName)
    Pages = NoteBook.winfo_children()
    if index >= 0 and index < len(Pages):
        NoteBook.hide(index)
def DelPage(uiName,elementName,index=0):
    """删除选项页:参数1 :界面类名, 参数2:控件名称, 参数3:页面索引"""
    NoteBook = GetElement(uiName,elementName)
    Pages = NoteBook.winfo_children()
    if index >= 0 and index < len(Pages):
        NoteBook.forget(Pages[index])
def AddTreeItem(uiName,elementName,parentItem="",insertItemPosition="end",itemName="",itemText="",itemValues=(),iconName="",tag=""):
    """增加树项:参数1 :界面类名, 参数2:控件名称, 参数3:父结点,参数4:插入位置项文字,参数5:树项值,参数6:文字内容,参数7:图标文件,参数8:标记名称"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementIconDictionary
    global G_ResourcesFileList
    Item = None
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0 and len(itemName) > 0:
                if iconName != "":
                    if iconName in G_UIElementIconDictionary[uiName][elementName]:
                        ItemIcon = G_UIElementIconDictionary[uiName][elementName][iconName]
                        Item = G_UIElementDictionary[uiName][elementName].insert(parentItem,insertItemPosition,itemName,text=itemText,values=itemValues,image=ItemIcon,tag=tag)
                    else:
                        ItemIcon = None
                        if os.path.exists(iconName) == True:
                            ItemIcon = ImageTk.PhotoImage(file = iconName)
                        else:
                            if iconName in G_ResourcesFileList:
                               imagePath = G_ResourcesFileList[iconName]
                            if os.path.exists(imagePath) == True:
                                ItemIcon = ImageTk.PhotoImage(file = imagePath)
                        if ItemIcon:
                            Item = G_UIElementDictionary[uiName][elementName].insert(parentItem,insertItemPosition,itemName,text=itemText,values=itemValues,image=ItemIcon,tag=tag)
                            G_UIElementIconDictionary[uiName][elementName][Item] = ItemIcon
                        else:
                            Item = G_UIElementDictionary[uiName][elementName].insert(parentItem,insertItemPosition,itemName,text=itemText,values=itemValues,tag=tag)
                else:
                    Item = G_UIElementDictionary[uiName][elementName].insert(parentItem,insertItemPosition,itemName,text=itemText,values=itemValues,tag=tag)
    return Item
def SetTreeItemText(uiName,elementName,itemName,text):
    """设置树项的文字"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0 and len(itemName) > 0:
                G_UIElementDictionary[uiName][elementName].item(itemName,text=text)
def GetTreeItemText(uiName,elementName,itemName):
    """取得树项的文字"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0 and len(itemName) > 0:
                item_text = G_UIElementDictionary[uiName][elementName].item(itemName,"text")
                return item_text
    return None
def SetTreeItemValues(uiName,elementName,itemName,itemValues):
    """设置树项的值"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0 and len(itemName) > 0:
                G_UIElementDictionary[uiName][elementName].item(itemName,values=itemValues)
def GetTreeItemValues(uiName,elementName,itemName):
    """取得树项的值"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0 and len(itemName) > 0:
                item_value = G_UIElementDictionary[uiName][elementName].item(itemName,"values")
                return item_value
    return None
def SetTreeItemIcon(uiName,elementName,itemName,iconName=""):
    """设置树项的图片"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_ResourcesFileList
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0 and len(itemName) > 0:
                if iconName != "":
                    if iconName in G_UIElementIconDictionary[uiName][elementName]:
                        ItemIcon = G_UIElementIconDictionary[uiName][elementName][iconName]
                        G_UIElementDictionary[uiName][elementName].item(itemName,image=ItemIcon)
                        G_UIElementIconDictionary[uiName][elementName][itemName]=ItemIcon
                    else:
                        ItemIcon = None
                        if os.path.exists(iconName) == True:
                            ItemIcon = ImageTk.PhotoImage(file = iconName)
                        else:
                            if iconName in G_ResourcesFileList:
                               imagePath = G_ResourcesFileList[iconName]
                            if os.path.exists(imagePath) == True:
                                ItemIcon = ImageTk.PhotoImage(file = imagePath)
                        if ItemIcon:
                            G_UIElementDictionary[uiName][elementName].item(itemName,image=ItemIcon)
                            G_UIElementIconDictionary[uiName][elementName][itemName]=ItemIcon
def ExpandTreeItem(uiName,elementName,itemName,expand=True):
    """展开或收缩树项"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0 and len(itemName) > 0:
                G_UIElementDictionary[uiName][elementName].item(itemName,open=expand)
def AddRowText(uiName,elementName,rowIndex ='end',values=(),tag=''):
    """为ListView插入一行"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                if rowIndex == '':
                    rowIndex = 'end'
                G_UIElementDictionary[uiName][elementName].insert('',rowIndex, values=values,tag=tag)
def GetRowTextList(uiName,elementName,rowIndex):
    """取得ListView指定行的所有列文本"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                ListView = G_UIElementDictionary[uiName][elementName]
                rowHandle = ListView.get_children()[rowIndex]
                rowValues = ListView.item(rowHandle,"values")
                return rowValues
    return None
def GetCellText(uiName,elementName,rowIndex,columnIndex):
    """取得ListView指定单元格的文本"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                ListView = G_UIElementDictionary[uiName][elementName]
                rowHandle = ListView.get_children()[rowIndex]
                rowValues = ListView.item(rowHandle,"values")
                return rowValues[columnIndex]
    return None
def SetCellText(uiName,elementName,rowIndex,columnIndex,text):
    """设置ListView指定单元格文字"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                rowHandle = G_UIElementDictionary[uiName][elementName].get_children()[rowIndex]
                G_UIElementDictionary[uiName][elementName].set(rowHandle,column=columnIndex,value=text)
def DeleteRow(uiName,elementName,rowIndex):
    """删除ListView指定行"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                rowHandle = G_UIElementDictionary[uiName][elementName].get_children()[rowIndex]
                G_UIElementDictionary[uiName][elementName].delete(rowHandle)
def DeleteAllRows(uiName,elementName):
    """清空ListView所有行"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                ListView = G_UIElementDictionary[uiName][elementName]
                RootChildren = ListView.get_children()
                for Item in RootChildren:
                    ListView.delete(Item)
def CheckPickedRow(uiName,elementName,x,y):
    """取得鼠标位置ListView的行号"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                ListView = G_UIElementDictionary[uiName][elementName]
                PickedItem = ListView.identify("item",x,y)
                if PickedItem:
                   RootChildren = ListView.get_children()
                   return RootChildren.index(PickedItem)
    return None
def CheckPickedCell(uiName,elementName,x,y):
    """取得鼠标位置ListView的单元格"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                ListView = G_UIElementDictionary[uiName][elementName]
                PickedItem = ListView.identify("item",x,y)
                if PickedItem:
                   row = ListView.index(PickedItem)
                   column = ListView.identify_column(x)
                   column = column.replace("#","")
                   column = int(column) - 1
                   return (row,column)
    return (-1,-1)
def OnListViewCellClicked(event,uiName,widgetName,callbackFunc):
    rowIndex,columnIndex = CheckPickedCell(uiName,widgetName,event.x,event.y)
    if callbackFunc:
        callbackFunc(uiName,widgetName,rowIndex,columnIndex)
def CheckPickedTreeItem(uiName,elementName,x,y):
    """判断当前点击的树结点项"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0:
                return G_UIElementDictionary[uiName][elementName].identify("item",x,y)
    return None
def SelectTreeItem(uiName,elementName,item):
    """选中对应树结点项"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0:
                G_UIElementDictionary[uiName][elementName].selection_set(item)
def MoveTreeItem(uiName,elementName,itemName,parentItem="",insertItemPosition="end"):
    """移动树结点项的位置"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0 and len(itemName) > 0:
                G_UIElementDictionary[uiName][elementName].move(itemName,parentItem,insertItemPosition)
def DelItemText(uiName,elementName,lineIndexOrText):
    """删除当前ListBox和ComboBox的文字项内容。参数1 :界面类名, 参数2:控件名称 ,参数3:文本内容。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ComboBox_') >= 0:
                ValueArray = list(G_UIElementDictionary[uiName][elementName]['value'])
                if type(lineIndexOrText)==type(1):
                    ValueArray.pop(lineIndexOrText)
                    G_UIElementDictionary[uiName][elementName]['value'] = ValueArray
                else:
                    ValueIndex = ValueArray.index(lineIndexOrText)
                    if ValueIndex >= 0:
                        ValueArray.pop(ValueIndex)
                    G_UIElementDictionary[uiName][elementName]['value'] = ValueArray
            elif elementName.find('ListBox_') >= 0:
                if type(lineIndexOrText)==type(1):
                    G_UIElementDictionary[uiName][elementName].delete(lineIndexOrText)
                else:
                    ValueArray = G_UIElementDictionary[uiName][elementName].get(0,tkinter.END)
                    ValueIndex = ValueArray.index(lineIndexOrText)
                    if ValueIndex >= 0:
                        G_UIElementDictionary[uiName][elementName].delete(ValueIndex)
def DelLineText(uiName,elementName,lineIndex="end"):
    """删除Text控件或ListBox控件的指定行文字:参数1 :界面类名, 参数2:控件名称, 参数3:行数"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('Text_') >= 0:
                if type(lineIndex)==type(1):
                    lineIndex = lineIndex + 1
                    beginIndex = str("%d.0"%lineIndex)
                    endIndex = str("%d.0"%(lineIndex+1))
                    G_UIElementDictionary[uiName][elementName].delete(beginIndex,endIndex)
                else:
                    beginIndex = str("%s.0"%lineIndex)
                    endIndex = str("%s.end"%lineIndex)
                    G_UIElementDictionary[uiName][elementName].delete(beginIndex,endIndex)
            elif elementName.find('ListBox_') >= 0:
                if type(lineIndex)==type(1):
                    G_UIElementDictionary[uiName][elementName].delete("%d"%lineIndex)
                else:
                    G_UIElementDictionary[uiName][elementName].delete("%s"%lineIndex)
def DelTreeItem(uiName,elementName,item):
    """删除树项"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0:
                G_UIElementDictionary[uiName][elementName].delete(item)
def DelAllTreeItem(uiName,elementName):
    """删除所有的树结点项"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0:
                TreeView = G_UIElementDictionary[uiName][elementName]
                RootChildren = TreeView.get_children()
                for Item in RootChildren:
                    TreeView.delete(Item)
def DelAllLines(uiName,elementName):
    """清空Text控件或ListBox控件的文字内容。参数1 :界面类名, 参数2:控件名称。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListBox_') >= 0:
                G_UIElementDictionary[uiName][elementName].delete(0,tkinter.END)
            elif elementName.find('Text_') >= 0:
                G_UIElementDictionary[uiName][elementName].delete('0.0',tkinter.END)
def GetSelectText(uiName,elementName):
    """取得ListBox、ComboBox、Navigation的选中索引值。参数1 :界面类名, 参数2:控件名称。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control != None:
        if elementName.find('Text_') == 0 :
            return Control.get(tkinter.SEL_FIRST,tkinter.SEL_LAST)
    return None
def DelSelectText(uiName,elementName):
    """取得ListBox、ComboBox、Navigation的选中索引值。参数1 :界面类名, 参数2:控件名称。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control != None:
        if elementName.find('Text_') == 0 :
            return Control.delete(tkinter.SEL_FIRST,tkinter.SEL_LAST)
    return None
def GetValueList(uiName,elementName):
    """取得当前ListBox、ComboBox和SpinBox等控件值列表的函数"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control != None:
        if elementName.find('ComboBox_') == 0 :
            return Control["values"]
        elif elementName.find('ListBox_') == 0 :
            listValueList = Control.get(0,tkinter.END)
            return listValueList
        elif elementName.find('SpinBox_') == 0 :
            return Control["values"]
    return None
def SetValueList(uiName,elementName,valueList):
    """设置当前ListBox、ComboBox和SpinBox等控件值列表的函数"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control != None:
        if elementName.find('ComboBox_') == 0 :
            Control["values"] = valueList
        elif elementName.find('ListBox_') == 0 :
            listVariable = Control.cget('listvariable')
            listVariable.set(valueList)
        elif elementName.find('SpinBox_') == 0 :
            Control["values"] = valueList
def OnListBoxSelect(event,uiName,widgetName):
    ListBox_Index = GetCurrentIndex(uiName,widgetName)
    if ListBox_Index < 0:
        ListBox_Index = G_UIElementVariableArray[uiName][widgetName].get()
        SetCurrentIndex(uiName,widgetName,ListBox_Index)
def OnListBoxFocusOut(event,uiName,widgetName):
    ListBox_Index = GetCurrentIndex(uiName,widgetName)
    if ListBox_Index >= 0:
        G_UIElementVariableArray[uiName][widgetName].set(ListBox_Index)
def GetCurrentValue(uiName,elementName):
    """取得控件的选中值(RadioButton、CheckButton、Scale、Progress、ListBox、ComboBox、SpinBox、SwitchButton)"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control != None:
        if elementName.find('RadioButton_') == 0 :
            return GetTKVariable(uiName,elementName)
        elif elementName.find('CheckButton_') == 0 :
            return GetTKVariable(uiName,elementName)
        elif elementName.find('ComboBox_') == 0 :
            return Control.get()
        elif elementName.find('Scale_') == 0 :
            return Control.get()
        elif elementName.find('SpinBox_') == 0 :
            return GetTKVariable(uiName,elementName)
        elif elementName.find('SwitchButton_') == 0 :
            return Control.GetCurrValue()
        elif elementName.find('ListBox_') == 0 :
            currIndex = Control.curselection()
            if len(currIndex) > 0 and currIndex[0] >= 0:
                return Control.get(currIndex[0])
        elif elementName.find('Progress_') == 0 :
            return Control["value"]
    return -1
def GetCurrentIndex(uiName,elementName):
    """取得ListBox、ComboBox、Navigation的选中索引值。参数1 :界面类名, 参数2:控件名称。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control != None:
        if elementName.find('ComboBox_') == 0 :
            return Control.current()
        elif elementName.find('ListBox_') == 0 :
            currIndex = Control.curselection()
            if len(currIndex) > 0 and currIndex[0] >= 0:
                return currIndex[0]
        if elementName.find('Navigation_') == 0 :
            return Control.GetCurrentIndex()
    return -1
def SetCurrentValue(uiName,elementName,value):
    """设置控件的选中值(RadioButton、CheckButton、Scale、Progress、ListBox、ComboBox、SpinBox、SwitchButton)"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control != None:
        if elementName.find('RadioButton_') == 0 :
            SetTKVariable(uiName,elementName,value)
        elif elementName.find('CheckButton_') == 0 :
            SetTKVariable(uiName,elementName,value)
        elif elementName.find('ComboBox_') == 0 :
            Control.set(value)
        elif elementName.find('Scale_') == 0 :
            Control.set(value)
        elif elementName.find('SpinBox_') == 0 :
            SetTKVariable(uiName,elementName,value)
        elif elementName.find('SwitchButton_') == 0 :
            Control.SetCurrValue(value)
        elif elementName.find('ListBox_') == 0 :
            Control.selection_clear(0,tkinter.END)
            itemCount = Control.size()
            for itemIndex in range(0,itemCount):
                itemText = Control.get(itemIndex)
                if itemText == value:
                    Control.select_set(itemIndex)
                    break
        elif elementName.find('Progress_') == 0 :
            Control["value"] = value 
def SetCurrentIndex(uiName,elementName,index):
    """设置ListBox、ComboBox、Navigation的选中索引值。参数1 :界面类名, 参数2:控件名称,参数3:索引值。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control != None:
        if elementName.find('ComboBox_') == 0 :
            Control.current(index)
        elif elementName.find('ListBox_') == 0 :
            Control.selection_set(index)
        elif elementName.find('Navigation_') == 0 :
            Control.SetCurrentIndex(index)
def SetScale(uiName,elementName,from_,to,tickinterval):
    """设置Slider"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control != None:
        Control.configure(from_=from_)
        Control.configure(to=to)
        Control.configure(tickinterval=tickinterval)
def SetProgress(uiName,elementName,maximum,value=0):
    """设置进度条Progress:参数1 :界面类名, 参数2:控件名称, 参数3:最大值 参数4: 当前值 。"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control != None:
        if elementName.find("ProgressDial_") >= 0:
            Control.SetMaxValue(maximum)
            Control.GetCurrValue(value)
        else:
            Control.configure(maximum=maximum)
            Control.configure(value=value)
def MovingChildPageXViewOffset(uiName,elementName,step=1):
    """面板内视野横向移动指定步长:参数1 :界面类名, 参数2:控件名称, 参数3:滑动块移动步长值"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control:
        elementName = elementName + "_Child"
        ChildPage = GetElement(uiName,elementName)
        if ChildPage:
            ChildPage.xview("scroll",step,"units")
def MovingChildPageYViewOffset(uiName,elementName,step=1):
    """面板内视野纵向移动指定步长:参数1 :界面类名, 参数2:控件名称, 参数3:滑动块移动步长值"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control:
        elementName = elementName + "_Child"
        ChildPage = GetElement(uiName,elementName)
        if ChildPage:
            ChildPage.yview("scroll",step,"units")
def MovingChildPageXViewTo(uiName,elementName,x=1.0):
    """面板内视野横向移动到目标位置:参数1 :界面类名, 参数2:控件名称, 参数3:滑动块目标位置"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control:
        elementName = elementName + "_Child"
        ChildPage = GetElement(uiName,elementName)
        if ChildPage:
            ChildPage.xview_moveto(x)
def MovingChildPageYViewTo(uiName,elementName,y=1.0):
    """面板内视野纵向移动到目标位置:参数1 :界面类名, 参数2:控件名称, 参数3:滑动块目标位置"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control:
        elementName = elementName + "_Child"
        ChildPage = GetElement(uiName,elementName)
        if ChildPage:
            ChildPage.yview_moveto(y)
def GetDate(uiName,elementName):
    """取得选择的日期"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control != None:
        return Control.GetDate()
    return None
def SetDate(uiName,elementName,year,month,day):
    """设置当前的日期"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control != None:
        return Control.SetDate(year,month,day)
    return None
def InitElementData(uiName):
    """初始化界面各控件初始数。参数1 :界面类名。"""
    global G_UIElementUserDataArray
    global G_ResourcesFileList
    if uiName in G_UIElementUserDataArray:
        for elementName in G_UIElementUserDataArray[uiName].keys():
            for EBData in G_UIElementUserDataArray[uiName][elementName]:
                if EBData[3] == 1:
                    SetText(uiName,elementName,EBData[2])
                    SetText(uiName,elementName,EBData[2])
    LoadCanvasRecord(uiName)
def InitElementStyle(uiName,Style):
    """初始化界面各控件初始样式。参数1 :界面类名, 参数2:样式名称。"""
    StyleArray = ReadStyleFile(Style+".py")
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        Root = GetElement(uiName,'root')
        TFormKey = '.TForm'
        if TFormKey in StyleArray:
            if 'background' in StyleArray[TFormKey]:
                Root['background'] = StyleArray[TFormKey]['background']
        for elementName in G_UIElementDictionary[uiName].keys():
            Widget = G_UIElementDictionary[uiName][elementName]
            if elementName != "UIClass" and elementName != "root":
                try:
                    if hasattr(Widget,"GetWidget") == True:
                        Widget = Widget.GetWidget()
                    if  Widget.winfo_exists() == 1:
                        WinClass = Widget.winfo_class()
                        StyleName = ".T"+WinClass
                        if StyleName in StyleArray.keys():
                            for attribute in StyleArray[StyleName].keys():
                                Widget[attribute] = StyleArray[StyleName][attribute]
                except Exception as ex:
                    print(ex)
def GetUIDataDictionary(uiName):
    """取得界面的所有控件数据。参数1 :界面类名。"""
    global G_UIElementDictionary
    global G_UIInputDataArray
    global G_UIElementVariableArray
    G_UIInputDataArray.clear()
    if uiName in G_UIElementDictionary:
        for elementName in G_UIElementDictionary[uiName].keys():
            if elementName == "UIClass":
                G_UIInputDataArray[elementName] = [uiName]
            else:
                G_UIInputDataArray[elementName] = []
            Widget = G_UIElementDictionary[uiName][elementName]
            if elementName.find('Label_') >= 0:
                text = Widget.cget('text')
                G_UIInputDataArray[elementName].append(text)
            elif elementName.find('Text_') >= 0:
                if elementName.find('Scroll') >= 0:
                    continue
                text = Widget.get('0.0', tkinter.END)
                G_UIInputDataArray[elementName].append(text)
            elif elementName.find('Entry_') >= 0:
                if elementName in  G_UIElementVariableArray[uiName]:
                    text = G_UIElementVariableArray[uiName][elementName].get()
                else:
                    text = Widget.GetText()
                G_UIInputDataArray[elementName].append(text)
            elif elementName.find('RadioButton_') == 0 :
                value = GetTKVariable(uiName,elementName)
                G_UIInputDataArray[elementName].append(value)
            elif elementName.find('CheckButton_') == 0 :
                value = GetTKVariable(uiName,elementName)
                G_UIInputDataArray[elementName].append(value)
            elif elementName.find('Spinbox_') >= 0:
                text = Widget.get()
                G_UIInputDataArray[elementName].append(text)
            elif elementName.find('ComboBox_') >= 0:
                text = Widget.get()
                G_UIInputDataArray[elementName].append(text)
            elif elementName.find('Scale_') >= 0:
                value = Widget.get()
                G_UIInputDataArray[elementName].append(value)
            elif elementName.find('Progress_') == 0 :
                value = Widget["value"]
                G_UIInputDataArray[elementName].append(value)
            elif elementName.find('ListBox_') >= 0:
                if elementName.find('Scroll') >= 0:
                    continue
                currIndex = Widget.curselection()
                if len(currIndex) > 0 and currIndex[0] >= 0:
                    text = Widget.get(currIndex[0])
                    G_UIInputDataArray[elementName].append(text)
    if uiName in G_UIElementVariableArray:
        for elementName in G_UIElementVariableArray[uiName].keys():
           if elementName.find('Group_') >= 0:
                ElementIntValue = G_UIElementVariableArray[uiName][elementName].get()
                G_UIInputDataArray[elementName] = []
                G_UIInputDataArray[elementName].append(ElementIntValue)
    return G_UIInputDataArray
def GoToUIDialog(uiName,targetUIName):
    """从当前界面跳转到另一个界面"""
    global G_ExeDir
    global G_ResDir
    root = GetElement(uiName,'root')
    Form1 = GetElement(uiName,'Form_1')
    if Form1:
        Form1.pack_forget()
    import importlib
    from   importlib import import_module
    try:
        importModule = importlib.import_module("Compile_"+targetUIName)
        importModule = importlib.reload(importModule)
        if hasattr(importModule,"Fun") == True:
            importModule.Fun.G_ExeDir = G_ExeDir
            importModule.Fun.G_ResDir = G_ResDir
            if hasattr(importModule,"EXUIControl") == True:
                importModule.EXUIControl.G_ExeDir = G_ExeDir
                importModule.EXUIControl.G_ResDir = G_ResDir
        if hasattr(importModule,targetUIName) == True:
            uiClass = getattr(importModule,targetUIName)
            MyDlg = uiClass(root)
    except ModuleNotFoundError:
        try:
            importModule = importlib.import_module(targetUIName)
            importModule = importlib.reload(importModule)
            if hasattr(importModule,"Fun") == True:
                importModule.Fun.G_ExeDir = G_ExeDir
                importModule.Fun.G_ResDir = G_ResDir
                if hasattr(importModule,"EXUIControl") == True:
                    importModule.EXUIControl.G_ExeDir = G_ExeDir
                    importModule.EXUIControl.G_ResDir = G_ResDir
            if hasattr(importModule,targetUIName) == True:
                uiClass = getattr(importModule,targetUIName)
                MyDlg = uiClass(root)
        except Exception as ex:
            MessageBox(ex)
    except Exception as ex:
        MessageBox(ex)
def PlayCallUIDialogAction(topLevel,uiInstance,animation='zoomin'):
    def FadeIn(topLevel,uiInstance,alpha):
        try :
            import ctypes
            from ctypes import windll
            hwnd = windll.user32.GetParent(topLevel.winfo_id())
            _winlib = ctypes.windll.user32
            style = _winlib.GetWindowLongA( hwnd, 0xffffffec ) | 0x00080000
            _winlib.SetWindowLongA( hwnd, 0xffffffec, style )
            _winlib.SetLayeredWindowAttributes( hwnd, 0, alpha+1, 2 )
            alpha = alpha + 1
        except ImportError:
            pass
        if alpha < 255:
            topLevel.after(1,lambda:FadeIn(topLevel = topLevel,uiInstance = uiInstance,alpha = alpha))
        else:
            print("结束")
    def ZoomIn(topLevel,uiInstance,zoom,width,height):
        try :
            import ctypes
            user32 = ctypes.windll.user32
            sw = user32.GetSystemMetrics(0)
            sh = user32.GetSystemMetrics(1)
            zw = int(width * zoom)
            zh = int(height * zoom)
            zx = int((sw-zw)/2) 
            zy = int((sh-zh)/2)
            topLevel.geometry('%dx%d+%d+%d'%(zw,zh,zx,zy))
            zoom = zoom + 0.01
        except ImportError:
            pass
        if zoom < 1.0:
            topLevel.after(1,lambda:ZoomIn(topLevel = topLevel,uiInstance = uiInstance,zoom = zoom ,width=width,height=height))
        else:
            print("结束")
    animation = animation.lower()
    if animation == "fadein":
        try :
            import ctypes
            from ctypes import windll
            hwnd = windll.user32.GetParent(topLevel.winfo_id())
            _winlib = ctypes.windll.user32
            style = _winlib.GetWindowLongA( hwnd, 0xffffffec ) | 0x00080000
            _winlib.SetWindowLongA( hwnd, 0xffffffec, style )
            _winlib.SetLayeredWindowAttributes( hwnd, 0, 0, 2 )
            topLevel.deiconify()
            topLevel.after(1,lambda:FadeIn(topLevel = topLevel,uiInstance = uiInstance,alpha = 0))
        except ImportError:
            pass
    elif animation == "zoomin":
        try :
            import ctypes
            user32 = ctypes.windll.user32
            sw = user32.GetSystemMetrics(0)
            sh = user32.GetSystemMetrics(1)
            topLevel.geometry('%dx%d+%d+%d'%(0,0,int(sw/2),int(sh/2)))
            form1_width,form1_height = uiInstance.GetRootSize()
            topLevel.deiconify()
            topLevel.after(1,lambda:ZoomIn(topLevel = topLevel,uiInstance = uiInstance,zoom = 0.0,width=form1_width,height=form1_height))
        except ImportError:
            pass
def CallUIDialog(uiName,topmost = 1,toolwindow = 1,grab_set = 1,animation=''):
    """调用显示一个界面对话框并返回所有控件的输入值。参数1 :界面类名 ,参数2 :是否置最前,参数3:是否有标题栏,参数4:只有当前界面接收消息。参数5:动画类型fadein - 渐显动画,zoomin - 缩放动画。"""
    global G_ExeDir
    global G_ResDir
    import importlib
    from   importlib import import_module
    try:
        importModule = importlib.import_module("Compile_"+uiName)
        importModule = importlib.reload(importModule)
        if hasattr(importModule,"Fun") == True:
            importModule.Fun.G_ExeDir = G_ExeDir
            importModule.Fun.G_ResDir = G_ResDir
            if hasattr(importModule,"EXUIControl") == True:
                importModule.EXUIControl.G_ExeDir = G_ExeDir
                importModule.EXUIControl.G_ResDir = G_ResDir
        if hasattr(importModule,uiName) == True and hasattr(importModule,"Fun") == True :
            uiClass = getattr(importModule,uiName)
            funClass = getattr(importModule,"Fun")
            topLevel = tkinter.Toplevel()
            topLevel.attributes("-toolwindow", toolwindow)
            topLevel.wm_attributes("-topmost", topmost)
            if grab_set == 1:
                topLevel.grab_set()
            if animation !='':
                topLevel.withdraw()
            uiInstance = uiClass(topLevel,True)
            def CloseWindow():
                funClass.GetUIDataDictionary(uiName)
                topLevel.destroy()
            topLevel.protocol('WM_DELETE_WINDOW', CloseWindow)
            if animation !='':
                PlayCallUIDialogAction(topLevel,uiInstance,animation)
            tkinter.Tk.wait_window(topLevel)
            return funClass.G_UIInputDataArray
    except ModuleNotFoundError:
        try:
            importModule = importlib.import_module(uiName)
            importModule = importlib.reload(importModule)
            if hasattr(importModule,"Fun") == True:
                importModule.Fun.G_ExeDir = G_ExeDir
                importModule.Fun.G_ResDir = G_ResDir
                if hasattr(importModule,"EXUIControl") == True:
                    importModule.EXUIControl.G_ExeDir = G_ExeDir
                    importModule.EXUIControl.G_ResDir = G_ResDir
            if hasattr(importModule,uiName) == True and hasattr(importModule,"Fun") == True :
                uiClass = getattr(importModule,uiName)
                funClass = getattr(importModule,"Fun")
                topLevel = tkinter.Toplevel()
                topLevel.attributes("-toolwindow", toolwindow)
                topLevel.wm_attributes("-topmost", topmost)
                if grab_set == 1:
                    topLevel.grab_set()
                if animation !='':
                    topLevel.withdraw()
                uiInstance = uiClass(topLevel,True)
                def CloseWindow():
                    funClass.GetUIDataDictionary(uiName)
                    topLevel.destroy()
                topLevel.protocol('WM_DELETE_WINDOW',CloseWindow)
                if animation !='':
                    PlayCallUIDialogAction(topLevel,uiInstance,animation)
                tkinter.Tk.wait_window(topLevel)
                return funClass.G_UIInputDataArray
        except Exception as ex:
            MessageBox(ex)
    except Exception as ex:
        MessageBox(ex)
    return None
def LoadUIDialog(uiName,elementName,targetUIName):
    """在指定控件上加载一个界面"""
    global G_ExeDir
    currUIDialog = GetUserData(uiName,elementName,"CurrUI")
    lastLoadTime = GetUserData(uiName,elementName,"LoadTime")
    if currUIDialog is None:
        AddUserData(uiName,elementName,"CurrUI","string",targetUIName,0)
        AddUserData(uiName,elementName,"LoadTime","long",time.time())
    else:
        if currUIDialog == targetUIName:
            currLoadTime = time.time()
            if  (currLoadTime - lastLoadTime) < 1:
                print("忽略重复加载"+":"+targetUIName)
                return 
        SetUserData(uiName,elementName,"CurrUI",targetUIName)
        SetUserData(uiName,elementName,"LoadTime",time.time())
    print("LoadUIDialog %s,%s => %s"%(uiName,elementName,targetUIName))
    Root = GetElement(uiName,'root')
    ParentFrame = GetElement(uiName,elementName)
    ParentFrame_Child = GetElement(uiName,elementName+"_Child")
    if ParentFrame_Child:
        ParentFrame = ParentFrame_Child
    for child in ParentFrame.winfo_children():
        child.destroy()  
    import importlib
    from   importlib import import_module
    try:
        UIPath, UIFile = os.path.split(targetUIName)
        if UIPath.find(":") < 0:
            UIPath = os.path.join(G_ExeDir,UIPath)
        UIName, extension = os.path.splitext(UIFile)
        import sys
        sys.path.append(UIPath)
        importModule = importlib.import_module(UIName)
        importModule = importlib.reload(importModule)
        if hasattr(importModule,"Fun") == True:
            importModule.Fun.G_ExeDir = G_ExeDir
            importModule.Fun.G_ResDir = G_ResDir
            if hasattr(importModule,"EXUIControl") == True:
                importModule.EXUIControl.G_ExeDir = G_ExeDir
                importModule.EXUIControl.G_ResDir = G_ResDir
        if hasattr(importModule,UIName) == True:
            uiClass = getattr(importModule,UIName)
            uiDialog = uiClass(ParentFrame,False)
            if ParentFrame_Child:
                uiDialogWidth = uiDialog.root.winfo_width()
                uiDialogHeight = uiDialog.root.winfo_height()
                uiDialogForm1 = None
                ChildWidgetList = uiDialog.root.children
                for widgetName in ChildWidgetList.keys():
                    uiDialogForm1  = ChildWidgetList[widgetName]
                    ChildHandle = ParentFrame.create_window(0,0, window=uiDialogForm1, anchor=tkinter.NW,tag="Form_1")
                    ParentFrame.itemconfig(ChildHandle,width=uiDialogWidth,height=uiDialogHeight)
            uiDialog.root = Root
            G_UIElementDictionary[UIName]['root'] = Root
            ReDrawCanvasRecord(targetUIName,True)
            return uiDialog
    except ModuleNotFoundError:
        try:
            UIPath, UIFile = os.path.split(targetUIName)
            if UIPath.find(":") < 0:
                UIPath = os.path.join(G_ExeDir,UIPath)
            UIName, extension = os.path.splitext(UIFile)
            import sys
            sys.path.append(UIPath)
            importModule = importlib.import_module("Compile_"+UIName)
            importModule = importlib.reload(importModule)
            if hasattr(importModule,"Fun") == True:
                importModule.Fun.G_ExeDir = G_ExeDir
                importModule.Fun.G_ResDir = G_ResDir
                if hasattr(importModule,"EXUIControl") == True:
                    importModule.EXUIControl.G_ExeDir = G_ExeDir
                    importModule.EXUIControl.G_ResDir = G_ResDir
            if hasattr(importModule,UIName) == True:
                uiClass = getattr(importModule,UIName)
                uiDialog = uiClass(ParentFrame,False)
                if ParentFrame_Child:
                    uiDialogWidth = uiDialog.root.winfo_width()
                    uiDialogHeight = uiDialog.root.winfo_height()
                    uiDialogForm1 = None
                    ChildWidgetList = uiDialog.root.children
                    for widgetName in ChildWidgetList.keys():
                        uiDialogForm1  = ChildWidgetList[widgetName]
                        ChildHandle = ParentFrame.create_window(0,0, window=uiDialogForm1, anchor=tkinter.NW,tag="Form_1")
                        ParentFrame.itemconfig(ChildHandle,width=uiDialogWidth,height=uiDialogHeight)
                uiDialog.root = Root
                G_UIElementDictionary[UIName]['root'] = Root
                ReDrawCanvasRecord(targetUIName,True)
                return uiDialog
        except Exception as ex:
            MessageBox(ex)
    except Exception as ex:
        MessageBox(ex)
def ShowWindow(uiName,WindowState):
    """设置窗口显示状态(0:隐藏,1:正常显示,2:最小化,3最大化)"""
    root = GetElement(uiName,'root')
    import ctypes
    from ctypes import windll
    import pywintypes
    import win32gui
    hwnd = windll.user32.GetParent(root.winfo_id())
    win32gui.ShowWindow(hwnd,WindowState)
def CenterDlg(uiName,popupDlg,dw=0,dh=0):
    """将弹出界面对话框居中。参数1 :界面类名, 参数2:对话框窗体,参数3:窗体宽度,参数4:窗体高度。"""
    if dw == 0:
        dw = popupDlg.winfo_width()
    if dh == 0:
        dh = popupDlg.winfo_height()
    root = GetElement(uiName,'root')
    if root != None and popupDlg != root:
        sw = root.winfo_width()
        sh = root.winfo_height()
        sx = root.winfo_x()
        sy = root.winfo_y()
        x = sx+(sw-dw)/2
        if x < 0:
            x = 0
        y = sy+(sh-dh)/2
        if y < 0:
            y = 0
        popupDlg.geometry('%dx%d+%d+%d'%(dw,dh,x,y))
    else:
        import ctypes
        user32 = ctypes.windll.user32
        sw = user32.GetSystemMetrics(0)
        sh = user32.GetSystemMetrics(1)
        sx = 0
        sy = 0
        x = sx+(sw-dw)/2
        if x < 0:
            x = 0
        y = sy+(sh-dh)/2
        if y < 0:
            y = 0
        popupDlg.geometry('%dx%d+%d+%d'%(dw,dh,x,y))
        popupDlg.attributes('-topmost', 1)
        popupDlg.attributes('-topmost', 0)
def MaximizeUI(uiName):
    """最大化窗口"""
    root = GetElement(uiName,'root')
    if 'root' not in G_UIElementPlaceDictionary[uiName]:
        G_UIElementPlaceDictionary[uiName]['root'] = {}
    G_UIElementPlaceDictionary[uiName]['root']['x'] = root.winfo_x()
    G_UIElementPlaceDictionary[uiName]['root']['y'] = root.winfo_y()
    G_UIElementPlaceDictionary[uiName]['root']['width'] = root.winfo_width()
    G_UIElementPlaceDictionary[uiName]['root']['height'] = root.winfo_height()
    import ctypes
    user32 = ctypes.windll.user32
    sw = user32.GetSystemMetrics(0)
    sh = user32.GetSystemMetrics(1)
    while root.master:
        root = root._nametowidget(root.winfo_parent())
    root.geometry('%dx%d+%d+%d'%(sw,sh,0,0))
    ReDrawCanvasRecord(uiName,True)
def MinimizeUI(uiName):
    """最小化窗口"""
    root = GetElement(uiName,'root')
    import ctypes
    from ctypes import windll
    import pywintypes
    import win32gui
    hwnd = windll.user32.GetParent(root.winfo_id())
    win32gui.ShowWindow(hwnd,2)
def RestoreUI(uiName):
    """恢复窗口"""
    root = GetElement(uiName,'root')
    if 'root' in G_UIElementPlaceDictionary[uiName]:
        root.geometry('%dx%d+%d+%d'%(G_UIElementPlaceDictionary[uiName]['root']['width'],G_UIElementPlaceDictionary[uiName]['root']['height'],G_UIElementPlaceDictionary[uiName]['root']['x'],G_UIElementPlaceDictionary[uiName]['root']['y']))
def HideUI(uiName):
    """隐藏窗口"""
    root = GetElement(uiName,'root')
    import ctypes
    from ctypes import windll
    import pywintypes
    import win32gui
    hwnd = windll.user32.GetParent(root.winfo_id())
    win32gui.ShowWindow(hwnd,0)
def SetRoundedRectangle(Control,WidthEllipse=20,HeightEllipse=20):
    """在界面布局文件中调用设置控件的圆角属性,但由于尚未创建接口,因此有必要在两次之后调用ShowRoundedRectangle。注意 :此功能不跨平台。参数1 :控件, 参数2:圆角宽度,参数3:圆角高度。"""
    if Control != None:
        if hasattr(Control,"GetWidget") == True:
            Control = Control.GetWidget()
        Control.after(10, lambda: ShowRoundedRectangle(Control,WidthEllipse,HeightEllipse))
def ShowRoundedRectangle(control,WidthEllipse,HeightEllipse):
    """立即设置控件的圆角属性。注意 :此功能不跨平台。参数1 :控件, 参数2:圆角宽度,参数3:圆角高度。"""
    import pywintypes
    import win32gui
    control_width = control.winfo_width()
    control_height = control.winfo_height()
    if control_width > 1 and control_height > 1:
        HRGN = win32gui.CreateRoundRectRgn(0,0,control_width,control_height,WidthEllipse,HeightEllipse)
        win32gui.SetWindowRgn(control.winfo_id(), HRGN,1)
    else:
        control.after(10, lambda: ShowRoundedRectangle(control,WidthEllipse,HeightEllipse))
def SetTransparencyFunction(root,alpha):
    """设置窗体透明值。注意 :此功能不跨平台。"""
    if root != None:
        try :
            import ctypes
            from ctypes import windll
            hwnd = windll.user32.GetParent(root.winfo_id())
            _winlib = ctypes.windll.user32
            style = _winlib.GetWindowLongA( hwnd, 0xffffffec ) | 0x00080000
            _winlib.SetWindowLongA( hwnd, 0xffffffec, style )
            _winlib.SetLayeredWindowAttributes( hwnd, 0, alpha, 2 )
        except ImportError:
            pass
def SetCursor(uiName,elementName,cursor):
    """设置光标"""
    element = GetElement(uiName,elementName)
    if element:
       element.configure(cursor=cursor)
def ExpandAllTreeItem(targetTree,isOpen,parentItem = None):
    """展开或关闭树项"""
    ParentItemArray = [parentItem]
    if parentItem == None:
        ParentItemArray = targetTree.get_children()
    for Item in ParentItemArray:
        targetTree.item(Item,open=isOpen)
        for childItem in targetTree.get_children(Item):
            targetTree.item(childItem,open=isOpen)
            ExpandAllTreeItem(targetTree,isOpen,childItem)
def MessageBox(text="",title="info",type="info"):
    """弹出一个信息对话框。参数1 :对话框显示文字 ,参数1:显示文字,参数2:标题文字,参数3:对话框类型,可选:info、warning、error"""
    if type == "info":
        tkinter.messagebox.showinfo(title,text)
    elif type == "error":
        tkinter.messagebox.showerror(title,text)
    else:
        tkinter.messagebox.showwarning(title,text)
def InputBox(title,text):
    """弹出一个输入对话框。参数1 :对话框标题文字 ,参数2:对话框默认框输入文字 。"""
    res = tkinter.simpledialog.askstring(title,'Input Box',initialvalue=text)
    return res
def AskBox(title,text):
    """弹出一个选择对话框,你需要选择YES或NO。参数1 :对话框标题文字 ,参数2 :对话框显示文字 。"""
    res = tkinter.messagebox.askyesno(title,text)
    return res
def SelectDirectory(title="选择路径",initDir = os.path.abspath('.')):
    """打开查找目录对话框"""
    import tkinter.filedialog
    openPath = tkinter.filedialog.askdirectory(title=title,initialdir=initDir)
    return openPath
def SelectColor(title="请选择颜色"):
    """打开选取颜色对话框"""
    import tkinter.colorchooser
    color = tkinter.colorchooser.askcolor(title=title)
    return color
def EnumFontName():
    """罗列当前系统的所有文字"""
    import tkinter.font
    return tkinter.font.families()
def WalkAllResFiles(parentPath,alldirs=True,extName=None):
    """返回对应目录的所有指定类型文件。参数1 :目录名称 ,参数2 :是否进入子目录,参数3:是否有扩展名筛选 。"""
    ResultFilesArray = []
    if os.path.exists(parentPath) == True:
        for fileName in os.listdir(parentPath):
            if '__pycache__' not in fileName:
                if '.git' not in fileName:
                    newPath = parentPath +'\\'+ fileName
                    if os.path.isdir(newPath):
                        if extName == None:
                           ResultFilesArray.append(newPath)
                        if alldirs == True:
                            ResultFilesArray.extend(WalkAllResFiles(newPath,alldirs,extName))
                    else:
                        if extName == None:
                            ResultFilesArray.append(newPath)
                        else:
                            file_extension = os.path.splitext(fileName)[1].replace('.','')
                            file_extension_lower = file_extension.lower().strip()
                            file_extName_lower = extName.lower().strip()
                            if file_extension_lower == file_extName_lower:
                                ResultFilesArray.append(newPath)
    return ResultFilesArray
def CopyFile(srcFile,dstFile,coverMode=True):
    """复制文件"""
    try:
        if os.path.exists(dstFile) == True and coverMode == True:
            os.remove(dstFile)
        def CreateParentDir(PathName):
            ParentPath,DirName = os.path.split(PathName)
            if os.path.exists(ParentPath) == False:
                CreateParentDir(ParentPath)
            os.mkdir(PathName)
        dstPathName,dstFileName = os.path.split(dstFile)
        if os.path.exists(dstPathName) == False:
            CreateParentDir(dstPathName)
        shutil.copyfile(srcFile,dstFile)
        return True
    except Exception as ex:
        print(ex)
    return False
def MoveFile(srcFile,dstFile,coverMode=True):
    """移动文件"""
    try:
        if os.path.exists(dstFile) == True and coverMode == True:
            os.remove(dstFile)
        shutil.move(srcFile,dstFile)
        return True
    except Exception as ex:
        print(ex)
    return False
def DeleteFile(dstFile):
    """删除文件"""
    if os.path.exists(dstFile) == True:
        os.remove(dstFile)
def GetFileMD5(srcFile):
    """取得文件MD5码"""
    import hashlib
    try:
        if os.path.exists(srcFile) == True:
            with open(srcFile, 'rb') as file:
                data = file.read()
                md5_hash = hashlib.md5(data).hexdigest()
                return md5_hash
    except Exception as ex:
        print(ex)
    return None
def CompareFileMD5(srcFile,dstFile):
    """比较两个文件是否一致"""
    MD51 = GetFileMD5(srcFile)
    MD52 = GetFileMD5(dstFile) 
    return MD51 != None and MD51 == MD52
def CreateDir(dstDir,coverMode=True):
    """创建目录"""
    try:
        if os.path.exists(dstDir) == True:
            if coverMode == True:
                shutil.rmtree(dstDir)
            else:
                return True
        def CreateParentDir(PathName):
            ParentPath,DirName = os.path.split(PathName)
            if os.path.exists(ParentPath) == False:
                CreateParentDir(ParentPath)
            os.mkdir(PathName)
        CreateParentDir(dstDir)
        return True
    except Exception as ex:
        print(ex)
    return False
def CopyDir(srcDir,dstDir,coverMode=True):
    """复制目录"""
    try:
        if os.path.exists(dstDir) == True and coverMode == True:
            shutil.rmtree(dstDir)
        shutil.copytree(srcDir, dstDir)
        return True
    except Exception as ex:
        print(ex)
    return False
def MoveDir(srcDir,dstDir,coverMode=True):
    """移动目录"""
    try:
        if os.path.exists(dstDir) == True and coverMode == True:
            shutil.rmtree(dstDir)
        shutil.copytree(srcDir, dstDir)
        shutil.rmtree(srcDir)
        return True
    except Exception as ex:
        print(ex)
    return False
def DeleteDir(srcDir):
    """删除目录"""
    return shutil.rmtree(srcDir)
def CheckIsDir(srcDir):
    """判断是否是目录"""
    return os.path.isdir(srcDir)
def CheckExist(srcDir):
    """判断文件或目录是否存在"""
    return os.path.exists(srcDir)
def EventFunction_Adaptor(fun,  **params):
    """重新定义消息映射函数,自定义参数。"""
    return lambda event, fun=fun, params=params: fun(event, **params)
def EventTwoFunction_Adaptor(fun1,fun2, **params):
    """重新定义消息映射函数,自定义参数。"""
    return lambda event, fun1=fun1,fun2=fun2, params=params: (fun1(event, **params),fun2(event, **params))
def MenuFunction_Adaptor(fun,  **params):
    """重新定义消息映射函数,自定义参数。"""
    return lambda event, fun=fun, params=params: fun(**params)
class   PyMeEvent():
    def __init__(self,x,y,tag=None):
        self.x = x
        self.y = y
        self.tag = tag
def SetControlPack(uiName,elementName,fill,side,padx,pady,expand):
    """设置控件的打包布局。参数1 :界面类名, 参数2:控件名称 ,参数3 :填充方式,参数4:方位 ,参数5 :横向边距,参数6:纵向边距。"""
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if hasattr(Control,"GetWidget") == True:
        Control = Control.GetWidget()
    if Control != None:
        Control.pack(fill = fill,side = side,padx = padx,pady = pady,expand = expand)
        PackDictionary = {}
        PackDictionary["type"] = "pack"
        PackDictionary["fill"] = fill
        PackDictionary["side"] = side
        PackDictionary["padx"] = padx
        PackDictionary["pady"] = pady
        PackDictionary["expand"] = expand
        PackDictionary["visible"] = True
        G_UIElementPlaceDictionary[uiName][elementName]=PackDictionary
def SetControlGrid(uiName,elementName,row,column,rowspan,columnspan):
    """设置控件的表格布局。参数1 :界面类名, 参数2:控件名称 ,参数3 :行位置,参数4:列位置 ,参数5 :合并行数,参数6:合并列数。"""
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if hasattr(Control,"GetWidget") == True:
        Control = Control.GetWidget()
    if Control != None:
        Control.grid(row = row,column = column,rowspan = rowspan,columnspan = columnspan)
        GridDictionary = {}
        GridDictionary["type"] = "grid"
        GridDictionary["row"] = row
        GridDictionary["column"] = column
        GridDictionary["rowspan"] = rowspan
        GridDictionary["columnspan"] = columnspan
        GridDictionary["visible"] = True
        G_UIElementPlaceDictionary[uiName][elementName]=GridDictionary
def SetControlPlace(uiName,elementName,x,y,w,h,anchorpoint='nw'):
    """设置控件的绝对或相对位置。参数1 :界面类名, 参数2:控件名称 ,参数3 :x位置,参数4:y位置 ,参数5 :宽度,参数6:高度 。"""
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if hasattr(Control,"GetWidget") == True:
        Control = Control.GetWidget()
    def getXW(value):
        if value >= 0 or G_RootSize is None:
            return value
        return G_RootSize[0]+value
    def getYH(value):
        if value >= 0 or G_RootSize is None:
            return value
        return G_RootSize[1]+value
    def getAnchorXY(x,y,width,height,parentWidth,parentHeight,anchorpoint):
        if width =='' or height == '':
            return x,y
        centerX = x + width * 0.5
        centerY = y + height * 0.5
        anchorX = x
        anchorY = y
        if anchorpoint == 'nw':
            anchorX = x /parentWidth
            anchorY = y /parentHeight
        elif anchorpoint == 'n':
            anchorX = centerX /parentWidth
            anchorY = y /parentHeight
        elif anchorpoint == 'ne':
            anchorX = (x + width) /parentWidth
            anchorY = y /parentHeight
        elif anchorpoint == 'w':
            anchorX = x /parentWidth
            anchorY = centerY /parentHeight
        elif anchorpoint == 'center':
            anchorX = centerX /parentWidth
            anchorY = centerY /parentHeight
        elif anchorpoint == 'e':
            anchorX = (x + width) /parentWidth
            anchorY = centerY /parentHeight
        elif anchorpoint == 'sw':
            anchorX = anchorX = x /parentWidth
            anchorY = (y + height) /parentHeight
        elif anchorpoint == 's':
            anchorX = centerX /parentWidth
            anchorY = (y + height) /parentHeight
        elif anchorpoint == 'se':
            anchorX = (x + width) /parentWidth
            anchorY = (y + height) /parentHeight
        return anchorX,anchorY
    if Control != None:
        ParentWidth = G_RootSize[0]
        ParentHeight = G_RootSize[1]
        Control.place_forget()
        if type(x) == type(1.0):
            if type(y) == type(1.0):
                if type(w) == type(1.0):
                    if type(h) == type(1.0):
                        Control.place(relx=x,rely=y,relwidth=w,relheight=h)
                        PlaceDictionary = {}
                        PlaceDictionary["type"] = "place"
                        PlaceDictionary["relx"] = x
                        PlaceDictionary["rely"] = y
                        PlaceDictionary["relwidth"] = w
                        PlaceDictionary["relheight"] = h
                        PlaceDictionary["visible"] = True
                        G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
                    else:
                        Control.place(relx=x,rely=y,relwidth=w,height=getYH(h))
                        PlaceDictionary = {}
                        PlaceDictionary["type"] = "place"
                        PlaceDictionary["relx"] = x
                        PlaceDictionary["rely"] = y
                        PlaceDictionary["relwidth"] = w
                        PlaceDictionary["height"] = getYH(h)
                        PlaceDictionary["visible"] = True
                        G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
                else:
                    if type(h) == type(1.0):
                        Control.place(relx=x,rely=y,width=getXW(w),relheight=h)
                        PlaceDictionary = {}
                        PlaceDictionary["type"] = "place"
                        PlaceDictionary["relx"] = x
                        PlaceDictionary["rely"] = y
                        PlaceDictionary["width"] = getXW(w)
                        PlaceDictionary["relheight"] = h
                        PlaceDictionary["visible"] = True
                        G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
                    else:
                        Control.place(relx=x,rely=y,width=getXW(w),height=getYH(h))
                        PlaceDictionary = {}
                        PlaceDictionary["type"] = "place"
                        PlaceDictionary["relx"] = x
                        PlaceDictionary["rely"] = y
                        PlaceDictionary["width"] = getXW(w)
                        PlaceDictionary["height"] = getYH(h)
                        PlaceDictionary["visible"] = True
                        G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
            else:
                if type(w) == type(1.0):
                    if type(h) == type(1.0):
                        Control.place(relx=x,y=getYH(y),relwidth=w,relheight=h)
                        PlaceDictionary = {}
                        PlaceDictionary["type"] = "place"
                        PlaceDictionary["relx"] = x
                        PlaceDictionary["y"] = getYH(y)
                        PlaceDictionary["relwidth"] = w
                        PlaceDictionary["relheight"] = h
                        PlaceDictionary["visible"] = True
                        G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
                    else:
                        Control.place(relx=x,y=getYH(y),relwidth=w,height=getYH(h))
                        PlaceDictionary = {}
                        PlaceDictionary["type"] = "place"
                        PlaceDictionary["relx"] = x
                        PlaceDictionary["y"] = getYH(y)
                        PlaceDictionary["relwidth"] = w
                        PlaceDictionary["height"] = getYH(h)
                        PlaceDictionary["visible"] = True
                        G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
                else:
                    if type(h) == type(1.0):
                        Control.place(relx=x,y=getYH(y),width=w,relheight=h)
                        PlaceDictionary = {}
                        PlaceDictionary["type"] = "place"
                        PlaceDictionary["relx"] = x
                        PlaceDictionary["y"] = getYH(y)
                        PlaceDictionary["relwidth"] = w
                        PlaceDictionary["relheight"] = h
                        PlaceDictionary["visible"] = True
                        G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
                    else:
                        Control.place(relx=x,y=getYH(y),width=w,height=getYH(h))
                        PlaceDictionary = {}
                        PlaceDictionary["type"] = "place"
                        PlaceDictionary["relx"] = x
                        PlaceDictionary["y"] = getYH(y)
                        PlaceDictionary["relwidth"] = w
                        PlaceDictionary["height"] = getYH(h)
                        PlaceDictionary["visible"] = True
                        G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
        else:
            if type(y) == type(1.0):
                if type(w) == type(1.0):
                    if type(h) == type(1.0):
                        Control.place(x=getXW(x),rely=y,relwidth=w,relheight=h)
                        PlaceDictionary = {}
                        PlaceDictionary["type"] = "place"
                        PlaceDictionary["x"] = getXW(x)
                        PlaceDictionary["rely"] = y
                        PlaceDictionary["relwidth"] = w
                        PlaceDictionary["relheight"] = h
                        PlaceDictionary["visible"] = True
                        G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
                    else:
                        Control.place(x=getXW(x),rely=y,relwidth=w,height=getYH(h))
                        PlaceDictionary = {}
                        PlaceDictionary["type"] = "place"
                        PlaceDictionary["x"] = getXW(x)
                        PlaceDictionary["rely"] = y
                        PlaceDictionary["relwidth"] = w
                        PlaceDictionary["height"] = getYH(h)
                        PlaceDictionary["visible"] = True
                        G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
                else:
                    if type(h) == type(1.0):
                        Control.place(x=getXW(x),rely=y,width=getXW(w),relheight=h)
                        PlaceDictionary = {}
                        PlaceDictionary["type"] = "place"
                        PlaceDictionary["x"] = getXW(x)
                        PlaceDictionary["rely"] = y
                        PlaceDictionary["width"] = getXW(w)
                        PlaceDictionary["relheight"] = h
                        PlaceDictionary["visible"] = True
                        G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
                    else:
                        Control.place(x=getXW(x),rely=y,width=getXW(w),height=getYH(h))
                        PlaceDictionary = {}
                        PlaceDictionary["type"] = "place"
                        PlaceDictionary["x"] = getXW(x)
                        PlaceDictionary["rely"] = y
                        PlaceDictionary["width"] = getXW(w)
                        PlaceDictionary["height"] = getYH(h)
                        PlaceDictionary["visible"] = True
                        G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
            else:
                if type(w) == type(1.0):
                    if type(h) == type(1.0):
                        Control.place(x=getXW(x),y=getYH(y),relwidth=w,relheight=h)
                        PlaceDictionary = {}
                        PlaceDictionary["type"] = "place"
                        PlaceDictionary["x"] = getXW(x)
                        PlaceDictionary["y"] = getYH(y)
                        PlaceDictionary["relwidth"] = w
                        PlaceDictionary["relheight"] = h
                        PlaceDictionary["visible"] = True
                        G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
                    else:
                        Control.place(x=getXW(x),y=getYH(y),relwidth=w,height=getYH(h))
                        PlaceDictionary = {}
                        PlaceDictionary["type"] = "place"
                        PlaceDictionary["x"] = getXW(x)
                        PlaceDictionary["y"] = getYH(y)
                        PlaceDictionary["relwidth"] = w
                        PlaceDictionary["height"] = getYH(h)
                        PlaceDictionary["visible"] = True
                        G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
                else:
                    if type(h) == type(1.0):
                        Control.place(x=getXW(x),y=getYH(y),width=getXW(w),relheight=h)
                        PlaceDictionary = {}
                        PlaceDictionary["type"] = "place"
                        PlaceDictionary["x"] = getXW(x)
                        PlaceDictionary["y"] = getYH(y)
                        PlaceDictionary["width"] = getXW(w)
                        PlaceDictionary["relheight"] = h
                        PlaceDictionary["visible"] = True
                        G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
                    else:
                        PlaceDictionary = {}
                        if h == '' and w == '':
                            Control.place(x=getXW(x),y=getYH(y))
                            PlaceDictionary["width"] = ''
                            PlaceDictionary["height"] = ''
                        elif h == '':
                            Control.place(x=getXW(x),y=getYH(y),width=getXW(w))
                            PlaceDictionary["width"] = getXW(w)
                            PlaceDictionary["height"] = ''
                        elif w == '':
                            Control.place(x=getXW(x),y=getYH(y),height=getYH(h))
                            PlaceDictionary["width"] = ''
                            PlaceDictionary["height"] = getYH(h)
                        else:
                            Control.place(x=getXW(x),y=getYH(y),width=getXW(w),height=getYH(h))
                            PlaceDictionary["width"] =  getXW(w)
                            PlaceDictionary["height"] = getYH(h)
                        PlaceDictionary["type"] = "place"
                        PlaceDictionary["x"] = getXW(x)
                        PlaceDictionary["y"] = getYH(y)
                        PlaceDictionary["visible"] = True
                        px,py = getAnchorXY(PlaceDictionary["x"],PlaceDictionary["y"],PlaceDictionary["width"],PlaceDictionary["height"],ParentWidth,ParentHeight,anchorpoint)
                        PlaceDictionary["anchorpoint"] = [anchorpoint,px,py]
                        G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
def UpdateElementPlace(uiName,ParentWidth,ParentHeight):
    """按参考位置更新控件位置"""
    if uiName not in G_UIElementPlaceDictionary:
        return
    for elementName in G_UIElementPlaceDictionary[uiName]:
        if elementName == "Form_1":
            continue
        Control = GetElement(uiName,elementName)
        if hasattr(Control,"GetWidget") == True:
            Control = Control.GetWidget()
        Visible = G_UIElementPlaceDictionary[uiName][elementName]["visible"]
        PlaceType = G_UIElementPlaceDictionary[uiName][elementName]["type"]
        if Visible == True and PlaceType == "place":
            x = G_UIElementPlaceDictionary[uiName][elementName]["x"]
            y = G_UIElementPlaceDictionary[uiName][elementName]["y"]
            w = G_UIElementPlaceDictionary[uiName][elementName]["width"]
            h = G_UIElementPlaceDictionary[uiName][elementName]["height"]
            anchorpoint = G_UIElementPlaceDictionary[uiName][elementName]["anchorpoint"]
            if anchorpoint[0] == "n":
                x = int(anchorpoint[1] * ParentWidth - w * 0.5)
            elif anchorpoint[0] == "ne":
                x = int(anchorpoint[1] * ParentWidth - w)
            elif anchorpoint[0] == "w":
                y = int(anchorpoint[2] * ParentHeight - h * 0.5)
            elif anchorpoint[0] == "center":
                x = int(anchorpoint[1] * ParentWidth - w * 0.5)
                y = int(anchorpoint[2] * ParentHeight - h * 0.5)
            elif anchorpoint[0] == "e":
                x = int(anchorpoint[1] * ParentWidth - w)
                y = int(anchorpoint[2] * ParentHeight - h * 0.5)
            elif anchorpoint[0] == "sw":
                y = int(anchorpoint[2] * ParentHeight - h)
            elif anchorpoint[0] == "s":
                x = int(anchorpoint[1] * ParentWidth - w * 0.5)
                y = int(anchorpoint[2] * ParentHeight - h)
            elif anchorpoint[0] == "se":
                x = int(anchorpoint[1] * ParentWidth - w)
                y = int(anchorpoint[2] * ParentHeight - h)
            try:
                Control.place(x=x,y=y,width=w,height=h)
            except Exception as ex:
                print(ex)
def DoCanvasRecord(drawCanvas,shapeType,x,y,x2,y2,fillcolor,outlinecolor,fillwidth,dash1=0,dash2=0,newImage=None,text='',textFont = None,textColor='',shapeTag=''):
    """画板动作处理函数"""
    if  drawCanvas != None:
        if shapeType == 'line' or shapeType == 'pen'  :
            if  dash1 > 0 :
                drawCanvas.create_line(x, y, x2, y2, fill=fillcolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
            else:
                drawCanvas.create_line(x, y, x2, y2,fill=fillcolor, width = fillwidth,tag=shapeTag)
        elif shapeType == 'arrow':
            if  dash1 > 0 :
                drawCanvas.create_line(x, y, x2, y2, arrow=tkinter.LAST,fill=fillcolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
            else:
                drawCanvas.create_line(x, y, x2, y2,arrow=tkinter.LAST,fill=fillcolor, width = fillwidth,tag=shapeTag)
        elif shapeType.find('triangle') == 0:
            width = x2 - x
            height = y2 - y
            direction = 'up'
            if shapeType.find('_left')>0:
                direction = 'left'
            elif shapeType.find('_right')>0:
                direction = 'right'
            elif shapeType.find('_down')>0:
                direction = 'down'
            if direction == 'left':
                points = [
                    x,
                    y + int(height/2),
                    x + width,
                    y ,
                    x + width,
                    y + height,
                    x,
                    y + int(height/2),]
            elif direction == 'right':
                points = [
                    x,
                    y,
                    x + width,
                    y + int(height/2) ,
                    x,
                    y + height,
                    x,
                    y,]
            elif direction == 'down':
                points = [
                    x,
                    y,
                    x + width,
                    y,
                    x + int(width/2),
                    y + height,
                    x,
                    y,]
            else:
                points = [
                    x,
                    y + height,
                    x + int(width/2),
                    y ,
                    x + width,
                    y + height,
                    x,
                    y + height,]
            if  fillcolor == 'None':
                if  dash1 > 0 :
                    drawCanvas.create_polygon(
                        points,
                        outline=outlinecolor, 
                        width= fillwidth,
                        dash=(dash1,dash2),
                        tag=shapeTag)
                else :
                    drawCanvas.create_polygon(
                        points,
                        outline=outlinecolor, 
                        width= fillwidth,
                        tag=shapeTag)
            else:
                if  dash1 > 0 :
                    drawCanvas.create_polygon(
                        points,
                        fill=fillcolor,
                        outline=outlinecolor, 
                        width= fillwidth,
                        dash=(dash1,dash2),
                        tag=shapeTag)
                else :
                    drawCanvas.create_polygon(
                        points,
                        fill=fillcolor,
                        outline=outlinecolor, 
                        width= fillwidth,
                        tag=shapeTag)
        elif shapeType == 'diamond':
            width = x2 - x
            height = y2 - y
            points = [
                x,
                y + int(height/2),
                x + int(width/2),
                y ,
                x + width,
                y + int(height/2),
                x + int(width/2),
                y + height,]
            if  fillcolor == 'None':
                if  dash1 > 0 :
                    drawCanvas.create_polygon(
                        points,
                        outline=outlinecolor, 
                        width= fillwidth,
                        dash=(dash1,dash2),
                        tag=shapeTag)
                else :
                    drawCanvas.create_polygon(
                        points,
                        outline=outlinecolor, 
                        width= fillwidth,
                        tag=shapeTag)
            else:
                if  dash1 > 0 :
                    drawCanvas.create_polygon(
                        points,
                        fill=fillcolor,
                        outline=outlinecolor, 
                        width= fillwidth,
                        dash=(dash1,dash2),
                        tag=shapeTag)
                else :
                    drawCanvas.create_polygon(
                        points,
                        fill=fillcolor,
                        outline=outlinecolor, 
                        width= fillwidth,
                        tag=shapeTag)
        elif shapeType == 'rect':
            if  fillcolor == 'None':
                if  dash1 > 0 :
                    drawCanvas.create_rectangle(x, y, x2, y2, outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                else:
                    drawCanvas.create_rectangle(x, y, x2, y2,outline=outlinecolor, width = fillwidth,tag=shapeTag)
            else:
                if  dash1 > 0 :
                    drawCanvas.create_rectangle(x, y, x2, y2, fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                else:
                    drawCanvas.create_rectangle(x, y, x2, y2,fill=fillcolor,outline=outlinecolor, width = fillwidth,tag=shapeTag)
        elif shapeType == 'roundrect':
            width = x2 - x
            height = y2 - y
            if newImage:
                roundRadius = int(newImage)
            else:
                roundRadius = int(0.2 * height)
            if roundRadius == 0:
                if  dash1 > 0 :
                    drawCanvas.create_rectangle(x, y, x2, y2, fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                else:
                    drawCanvas.create_rectangle(x, y, x + width,y + height,fill=fillcolor, outline=outlinecolor,width = fillwidth,tag=shapeTag)
            else:
                drawCanvas.create_rectangle(x+roundRadius,y+roundRadius,x+width-roundRadius, y+height-roundRadius,fill=fillcolor, width = 0,tag=shapeTag)
                drawCanvas.create_rectangle(x+roundRadius,y,x+width-roundRadius,y+roundRadius,fill=fillcolor, width=0,tag=shapeTag)
                drawCanvas.create_rectangle(x+roundRadius,y+height-roundRadius,x+width-roundRadius,y+height,fill=fillcolor, width=0,tag=shapeTag)
                drawCanvas.create_rectangle(x,y+roundRadius,x+roundRadius,y+height-roundRadius,fill=fillcolor,width=0,tag=shapeTag)
                drawCanvas.create_rectangle(x+width-roundRadius,y+roundRadius,x+width,y+height-roundRadius,fill=fillcolor,width=0,tag=shapeTag)
            OutLineTag = shapeTag+"_outline"
            if fillwidth > 0:
                if  dash1 > 0:
                    drawCanvas.create_line(x+roundRadius,y,x+width-roundRadius,y,fill=outlinecolor,dash=(dash1,dash2),tag=OutLineTag,width=fillwidth)
                    drawCanvas.create_line(x+roundRadius,y+height,x+width-roundRadius,y+height,fill=outlinecolor,dash=(dash1,dash2),tag=OutLineTag,width=fillwidth)
                    drawCanvas.create_line(x,y+roundRadius,x,y+height-roundRadius,fill=outlinecolor,tag=OutLineTag,dash=(dash1,dash2),width=fillwidth)
                    drawCanvas.create_line(x+width,y+roundRadius,x+width,y+height-roundRadius,fill=outlinecolor,dash=(dash1,dash2),tag=OutLineTag,width=fillwidth)
                else:
                    drawCanvas.create_line(x+roundRadius,y,x+width-roundRadius,y,fill=outlinecolor,tag=OutLineTag,width=fillwidth)
                    drawCanvas.create_line(x+roundRadius,y+height,x+width-roundRadius,y+height,fill=outlinecolor,tag=OutLineTag,width=fillwidth)
                    drawCanvas.create_line(x,y+roundRadius,x,y+height-roundRadius,fill=outlinecolor,tag=OutLineTag,width=fillwidth)
                    drawCanvas.create_line(x+width,y+roundRadius,x+width,y+height-roundRadius,fill=outlinecolor,tag=OutLineTag,width=fillwidth)
            drawCanvas.create_arc(x,y,x+2*roundRadius,y+2*roundRadius,start=180,extent=-90,fill=fillcolor,outline=fillcolor,width=0,tag=shapeTag)
            drawCanvas.create_arc(x+width-2*roundRadius,y,x+width,y+2*roundRadius,extent=90,fill=fillcolor,outline=fillcolor,width=0,tag=shapeTag)
            drawCanvas.create_arc(x+width-2*roundRadius,y+height-2*roundRadius,x+width,y+height,extent=-90,fill=fillcolor,outline=fillcolor,width=0,tag=shapeTag)
            drawCanvas.create_arc(x,y+height-2*roundRadius,x+2*roundRadius,y+height,start=180,extent=90,fill=fillcolor,outline=fillcolor,width=0,tag=shapeTag)
            OutArcTag = shapeTag+"_arc"
            if fillwidth > 0:
                if  dash1 > 0:
                    drawCanvas.create_arc(x,y,x+2*roundRadius,y+2*roundRadius,start=180,extent=-90,outline=outlinecolor,dash=(dash1,dash2),width=fillwidth, style='arc',tag=OutArcTag)
                    drawCanvas.create_arc(x+width-2*roundRadius,y,x+width,y+2*roundRadius,extent=90,outline=outlinecolor,dash=(dash1,dash2),width=fillwidth, style='arc',tag=OutArcTag)
                    drawCanvas.create_arc(x+width-2*roundRadius,y+height-2*roundRadius,x+width,y+height,extent=-90,outline=outlinecolor,dash=(dash1,dash2),width=fillwidth, style='arc',tag=OutArcTag)
                    drawCanvas.create_arc(x,y+height-2*roundRadius,x+2*roundRadius,y+height,start=180,extent=90,outline=outlinecolor,dash=(dash1,dash2),width=fillwidth, style='arc',tag=OutArcTag)
                else:
                    drawCanvas.create_arc(x,y,x+2*roundRadius,y+2*roundRadius,start=180,extent=-90,outline=outlinecolor,width=fillwidth, style='arc',tag=OutArcTag)
                    drawCanvas.create_arc(x+width-2*roundRadius,y,x+width,y+2*roundRadius,extent=90,outline=outlinecolor,width=fillwidth, style='arc',tag=OutArcTag)
                    drawCanvas.create_arc(x+width-2*roundRadius,y+height-2*roundRadius,x+width,y+height,extent=-90,outline=outlinecolor,width=fillwidth, style='arc',tag=OutArcTag)
                    drawCanvas.create_arc(x,y+height-2*roundRadius,x+2*roundRadius,y+height,start=180,extent=90,outline=outlinecolor,width=fillwidth, style='arc',tag=OutArcTag)
        elif shapeType == 'circle':
            if  fillcolor == 'None':
                if  dash1 > 0 :
                    drawCanvas.create_oval(x, y, x2, y2, outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                else:
                    drawCanvas.create_oval(x, y, x2, y2,outline=outlinecolor, width = fillwidth,tag=shapeTag)
            else:
                if  dash1 > 0 :
                    drawCanvas.create_oval(x, y, x2, y2, fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                else:
                    drawCanvas.create_oval(x, y, x2, y2,fill=fillcolor,outline=outlinecolor, width = fillwidth,tag=shapeTag)
        elif shapeType == 'cylinder':
            width = x2 - x
            height = y2 - y
            OvalHeight = height * 0.2
            OvalHeight_Half = height * 0.1
            OutLineTag = shapeTag+"_outline"
            if  dash1 > 0 :
                drawCanvas.create_oval(x,y2-OvalHeight,x2,y2,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                drawCanvas.create_rectangle(x,y+OvalHeight_Half,x2,y2-OvalHeight_Half,fill=fillcolor,width=0,tag=shapeTag)
                drawCanvas.create_oval(x,y,x2,y+OvalHeight,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                drawCanvas.create_line(x,y+OvalHeight_Half,x,y2-OvalHeight_Half,fill=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=OutLineTag)
                drawCanvas.create_line(x2,y+OvalHeight_Half,x2,y2-OvalHeight_Half,fill=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=OutLineTag)
            else:
                drawCanvas.create_oval(x,y2-OvalHeight,x2,y2,fill=fillcolor,outline=outlinecolor,width = fillwidth,tag=shapeTag)
                drawCanvas.create_rectangle(x,y+OvalHeight_Half,x2,y2-OvalHeight_Half,fill=fillcolor,width=0,tag=shapeTag)
                drawCanvas.create_oval(x,y,x2,y+OvalHeight,fill=fillcolor,outline=outlinecolor,width = fillwidth,tag=shapeTag)
                drawCanvas.create_line(x,y+OvalHeight_Half,x,y2-OvalHeight_Half,fill=outlinecolor,width = fillwidth,tag=OutLineTag)
                drawCanvas.create_line(x2,y+OvalHeight_Half,x2,y2-OvalHeight_Half,fill=outlinecolor,width = fillwidth,tag=OutLineTag)
        elif shapeType == 'star':
            center_x = (x + x2)/2
            center_y = (y + y2)/2
            rx = (x2 - x)/2
            ry = (y2 - y)/2
            points = [
                center_x - int(rx * math.sin(2 * math.pi / 5)),
                center_y - int(ry * math.cos(2 * math.pi / 5)),
                center_x + int(rx * math.sin(2 * math.pi / 5)),
                center_y - int(ry * math.cos(2 * math.pi / 5)),
                center_x - int(rx * math.sin(math.pi / 5)),
                center_y + int(ry * math.cos(math.pi / 5)),
                center_x,
                center_y - ry,
                center_x + int(rx * math.sin(math.pi / 5)),
                center_y + int(ry * math.cos(math.pi / 5)),
                ]
            if  dash1 > 0 :
                drawCanvas.create_polygon(
                    points,
                    fill=fillcolor,
                    outline=outlinecolor, 
                    width= fillwidth,
                    dash=(dash1,dash2),
                    tag=shapeTag)
            else :
                drawCanvas.create_polygon(
                    points,
                    fill=fillcolor,
                    outline=outlinecolor, 
                    width= fillwidth,
                    tag=shapeTag)
        elif shapeType == 'eraser':
            drawCanvas.create_rectangle(x, y, x2, y2,fill=fillcolor, width = 0,tag=shapeTag) 
        elif shapeType == 'text':
            drawCanvas.create_text(x, y,fill=fillcolor,text=text,font = textFont,anchor='nw',tag=shapeTag)
        elif shapeType == 'button':
            center_x = (x + x2)/2
            center_y = (y + y2)/2
            if newImage:
                drawCanvas.create_image(x, y,image=newImage,anchor='nw',tag=shapeTag)
            else:
                oval_rx = 20
                OutLineTag = shapeTag+"_outline"
                half_width = int((fillwidth+1)/2)
                if  dash1 > 0 :
                    drawCanvas.create_oval(x,y,x+2*oval_rx,y2,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                    drawCanvas.create_oval(x2-2*oval_rx,y,x2,y2,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                    drawCanvas.create_rectangle(x+oval_rx, y, x2-oval_rx, y2+1,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2), width = fillwidth,tag=shapeTag)
                    drawCanvas.create_line(x+oval_rx, y+half_width, x+oval_rx, y2-half_width,fill=fillcolor,width = fillwidth,tag=OutLineTag)
                    drawCanvas.create_line(x2-oval_rx, y+half_width, x2-oval_rx, y2-half_width,fill=fillcolor,width = fillwidth,tag=OutLineTag)
                else:
                    drawCanvas.create_oval(x,y,x+2*oval_rx,y2,fill=fillcolor,outline=outlinecolor,width = fillwidth,tag=shapeTag)
                    drawCanvas.create_oval(x2-2*oval_rx,y,x2,y2,fill=fillcolor,outline=outlinecolor,width = fillwidth,tag=shapeTag)
                    drawCanvas.create_rectangle(x+oval_rx, y, x2-oval_rx, y2+1,fill=fillcolor,outline=outlinecolor, width = fillwidth,tag=shapeTag)
                    drawCanvas.create_line(x+oval_rx, y+half_width, x+oval_rx, y2-half_width,fill=fillcolor,width = fillwidth,tag=OutLineTag)
                    drawCanvas.create_line(x2-oval_rx, y+half_width, x2-oval_rx, y2-half_width,fill=fillcolor,width = fillwidth,tag=OutLineTag)
            if len(text) > 0:
                drawCanvas.create_text(center_x, center_y,fill=textColor,text=text,font = textFont,anchor='center',tag=shapeTag+"_text")
        elif shapeType == 'image':
            if type(newImage) == type([]):
                drawCanvas.create_image(x, y,image=newImage[0][0],anchor='nw',tag=shapeTag)
            else:
                drawCanvas.create_image(x, y,image=newImage,anchor='nw',tag=shapeTag)
        elif shapeType == 'switch':
            SwitchWidth = x2 - x
            SwitchHeight = y2 - y
            Switch_radius = int(SwitchHeight/2)
            fillcolor = '#777777'
            drawCanvas.create_oval(x, y, x+SwitchHeight, y+SwitchHeight-1,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
            drawCanvas.create_oval(x+(SwitchWidth-SwitchHeight), y, x+SwitchWidth,y+ SwitchHeight-1,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
            drawCanvas.create_rectangle(x+Switch_radius,y,x+(SwitchWidth-Switch_radius),y+SwitchHeight,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
            drawCanvas.create_oval(x+2, y+2, x+(SwitchHeight-3), y+(SwitchHeight-3),fill=outlinecolor,width=0,tag=shapeTag)
            drawCanvas.create_text(x+(SwitchWidth-int(1.0*SwitchHeight)), y+int(SwitchHeight/2), text="Off",font = ("System",int(SwitchHeight/2)),anchor='center',fill=outlinecolor,width=0,tag=shapeTag)
        elif shapeType == 'listmenu':
            if  dash1 > 0 :
                drawCanvas.create_rectangle(x, y, x2, y2,fill='#FFFFFF', outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
            else:
                drawCanvas.create_rectangle(x, y, x2, y2,fill='#FFFFFF', outline=outlinecolor,width = fillwidth,tag=shapeTag)
            MenuInfo = newImage
            SubMenus = MenuInfo['SubMenus']
            ListMenuWidth = x2 - x
            ListMenuHeight = y2 - y
            SubMenuTitleHeight = 24
            SubMenuTitleSpacingX = 2
            SubMenuTitleSpacingY = 5
            SubMenuItemHeight = 22
            SubMenuItemSpacingX = 2
            SubMenuItemSpacingY = 4
            centerX = x + int(ListMenuWidth/2)
            SubMeshX = x + SubMenuTitleSpacingX
            SubMenuTitleHeight_Half = int(SubMenuTitleHeight/2)
            IconX = x+int(0.25 * ListMenuWidth)
            ListMenuTop = y + SubMenuTitleSpacingY
            for subMenu in SubMenus:
                titleText = subMenu[0]
                bgImgFile = subMenu[1]
                itemList = subMenu[2]
                subMeshTag = shapeTag + "_"+titleText
                drawCanvas.create_oval(SubMeshX, ListMenuTop, SubMeshX + SubMenuTitleHeight, ListMenuTop+SubMenuTitleHeight-1,fill=fillcolor,outline=outlinecolor,width=0, tag=subMeshTag)
                drawCanvas.create_oval(x2-SubMenuTitleHeight, ListMenuTop, x2,ListMenuTop+ SubMenuTitleHeight-1,fill=fillcolor,outline=outlinecolor,width=0, tag=subMeshTag)
                drawCanvas.create_rectangle(x+SubMenuTitleHeight_Half,ListMenuTop,x2-SubMenuTitleHeight_Half,ListMenuTop+SubMenuTitleHeight,fill=fillcolor,outline=outlinecolor,width=0, tag=subMeshTag)
                centerY = ListMenuTop + int(SubMenuTitleHeight/2)
                drawCanvas.create_text(centerX ,centerY,text=titleText,anchor=tkinter.CENTER,font=('Arial',14,'bold'),fill = outlinecolor,tag=subMeshTag) 
                ListMenuTop = ListMenuTop + (SubMenuTitleHeight + SubMenuTitleSpacingY)
                if subMenu[3] == True:
                    for itemInfo in itemList:
                        titleText = itemInfo[0]
                        centerY = ListMenuTop + int(SubMenuItemHeight/2)
                        drawCanvas.create_oval(IconX-5, centerY-5, IconX+5, centerY+5,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
                        drawCanvas.create_text(centerX ,centerY,text=titleText,anchor=tkinter.CENTER,font=('Arial',10,'bold'),fill = outlinecolor,tag=shapeTag) 
                        ListMenuTop = ListMenuTop + (SubMenuItemHeight + SubMenuItemSpacingY)
        elif shapeType == 'table':
            if  dash1 > 0 :
                drawCanvas.create_rectangle(x, y, x2, y2,fill='#FFFFFF', outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
            else:
                drawCanvas.create_rectangle(x, y, x2, y2,fill='#FFFFFF', outline=outlinecolor,width = fillwidth,tag=shapeTag)
            TableInfo = newImage
            TableWidth = x2- x
            TableHeight = y2 - y
            TableName = TableInfo['info'][0]
            TableCow = TableInfo['info'][1]
            TableRow = TableInfo['info'][2]
            TableRowHeight = TableHeight / (TableRow + 2)
            TableCowWidth = TableWidth / TableCow
            TableTopY = y
            TableBottomY = y2
            if y2 < y:
                TableTopY = y2
                TableBottomY = y
            #行
            RowLineY = TableBottomY
            for row in range(0,TableRow+1):
                RowLineY = int(TableBottomY - row * TableRowHeight)
                drawCanvas.create_line(x,RowLineY,x2,RowLineY,fill='#000000',width = 1,tag=shapeTag)
            #标题
            TableHeadCenterX = int((x + x2)/2)
            TableHeadCenterY = int((TableTopY + RowLineY)/2)
            drawCanvas.create_rectangle(x, TableTopY, x2, RowLineY,fill=outlinecolor,tag=shapeTag)
            drawCanvas.create_text(TableHeadCenterX,TableHeadCenterY,fill='#FFFFFF',text=TableName, font=('System',int(TableRowHeight)),anchor='center',tag=shapeTag)
            #列
            CowLeft = x
            for cow in range(0,TableCow):
                TableCowWidth = int(TableWidth * TableInfo['cow'][cow])
                drawCanvas.create_line(CowLeft,RowLineY,CowLeft,TableBottomY,fill='#000000',width = 1,tag=shapeTag)
                CowCenteX = int(CowLeft + TableCowWidth/2)
                CowCenterY = int(RowLineY + TableRowHeight/2)
                TitleText = TableInfo['title'][cow]
                drawCanvas.create_text(CowCenteX,CowCenterY,fill='#000000',text=TitleText, font=('System',int(TableRowHeight/2)),anchor='center',tag=shapeTag)
                CowLeft = CowLeft + TableCowWidth
            #填充其它数据
            for row in range(0,TableRow):
                RowTop = int(RowLineY + (row + 1) * TableRowHeight)
                CowLeft = x
                for cow in range(0,TableCow):
                    if str(row) in TableInfo:
                        CowText = TableInfo[str(row)][cow]
                        TableCowWidth = int(TableWidth * TableInfo['cow'][cow])
                        if CowText != '':
                            CowCenteX = int(CowLeft + TableCowWidth/2)
                            CowCenterY = int(RowTop + TableRowHeight/2)
                            drawCanvas.create_text(CowCenteX,CowCenterY,fill='#000000',text=CowText, font=('System',int(TableRowHeight/2-2)),anchor='center',tag=shapeTag)
                        CowLeft = CowLeft + TableCowWidth
def DrawLine(uiName,drawCanvasName,x1,y1,x2,y2,color,width=1,dash=(0,0),shapeTag=''):
    """在画布上画线"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag == '':
        Index = 0
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            if ShepTagName.find('line_') == 0:
                NameSplitArray = ShepTagName.partition('line_')
                if NameSplitArray[2].isdigit() == True:
                    Number = int(NameSplitArray[2])
                    if Number > Index:
                        Index = Number
        Index = Index + 1
        shapeTag = str("line_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=['line',x1,y1,x2,y2,color,color,width,dash[0],dash[1]]
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,color,width,dash[0],dash[1],None,'',None,'']
    DoCanvasRecord(drawCanvas,'line',x1,y1,x2,y2,color,color,width,dash1=dash[0],dash2=dash[1],newImage=None,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag
def DrawArrow(uiName,drawCanvasName,x1,y1,x2,y2,color,width=1,dash=(0,0),shapeTag=''):
    """在画布上画箭头"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag == '':
        Index = 0
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            if ShepTagName.find('arrow_') == 0:
                NameSplitArray = ShepTagName.partition('arrow_')
                if NameSplitArray[2].isdigit() == True:
                    Number = int(NameSplitArray[2])
                    if Number > Index:
                        Index = Number
        Index = Index + 1
        shapeTag = str("arrow_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=['arrow',x1,y1,x2,y2,color,color,width,dash[0],dash[1]]
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,color,width,dash[0],dash[1],None,'',None,'']
    DoCanvasRecord(drawCanvas,'arrow',x1,y1,x2,y2,color,color,width,dash1=dash[0],dash2=dash[1],newImage=None,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag
def DrawTriangle(uiName,drawCanvasName,direction,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):
    """在画布上画矩形"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    TriangleType = "triangle_up"
    if direction == "down":
        TriangleType = "triangle_down"
    if direction == "left":
        TriangleType = "triangle_left"
    if direction == "right":
        TriangleType = "triangle_right"
    if shapeTag == '':
        Index = 0
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            if ShepTagName.find('triangle_') == 0:
                NameSplitArray = ShepTagName.partition('triangle_')
                if NameSplitArray[2].isdigit() == True:
                    Number = int(NameSplitArray[2])
                    if Number > Index:
                        Index = Number
        Index = Index + 1
        shapeTag = str("triangle_%d"%Index)
    G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[TriangleType,x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,outlinecolor,outlinewidth,dash[0],dash[1],None,'',None,'']
    DoCanvasRecord(drawCanvas,TriangleType,x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash1=dash[0],dash2=dash[1],newImage=None,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag
def DrawRectangle(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):
    """在画布上显示圆角矩形"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag == '':
        Index = 0
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            if ShepTagName.find('roundrect_') == 0:
                NameSplitArray = ShepTagName.partition('roundrect_')
                if NameSplitArray[2].isdigit() == True:
                    Number = int(NameSplitArray[2])
                    if Number > Index:
                        Index = Number
        Index = Index + 1
        shapeTag = str("roundrect_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=['roundrect',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,outlinecolor,outlinewidth,dash[0],dash[1],None,'',None,'']
    DoCanvasRecord(drawCanvas,'roundrect',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash1=dash[0],dash2=dash[1],newImage=None,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag
def DrawRoundedRectangle(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),roundRadius=10,shapeTag=''):
    """在画布上画三角形"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag == '':
        Index = 0
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            if ShepTagName.find('rect_') == 0:
                NameSplitArray = ShepTagName.partition('rect_')
                if NameSplitArray[2].isdigit() == True:
                    Number = int(NameSplitArray[2])
                    if Number > Index:
                        Index = Number
        Index = Index + 1
        shapeTag = str("rect_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=['rect',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,outlinecolor,outlinewidth,dash[0],dash[1],None,'',None,'']
    DoCanvasRecord(drawCanvas,'rect',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash1=dash[0],dash2=dash[1],newImage=roundRadius,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag
def DrawCircle(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):
    """在画布上画圆"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag == '':
        Index = 0
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            if ShepTagName.find('circle_') == 0:
                NameSplitArray = ShepTagName.partition('circle_')
                if NameSplitArray[2].isdigit() == True:
                    Number = int(NameSplitArray[2])
                    if Number > Index:
                        Index = Number
        Index = Index + 1
        shapeTag = str("circle_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=['circle',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,outlinecolor,outlinewidth,dash[0],dash[1],None,'',None,'']
    DoCanvasRecord(drawCanvas,'circle',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash1=dash[0],dash2=dash[1],newImage=None,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag
def DrawDiamond(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):
    """在画布上画菱形"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag == '':
        Index = 0
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            if ShepTagName.find('diamond_') == 0:
                NameSplitArray = ShepTagName.partition('diamond_')
                if NameSplitArray[2].isdigit() == True:
                    Number = int(NameSplitArray[2])
                    if Number > Index:
                        Index = Number
        Index = Index + 1
        shapeTag = str("diamond_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=['diamond',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,outlinecolor,outlinewidth,dash[0],dash[1],None,'',None,'']
    DoCanvasRecord(drawCanvas,'diamond',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash1=dash[0],dash2=dash[1],newImage=None,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag
def DrawCylinder(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):
    """在画布上画圆柱"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag == '':
        Index = 0
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            if ShepTagName.find('cylinder_') == 0:
                NameSplitArray = ShepTagName.partition('cylinder_')
                if NameSplitArray[2].isdigit() == True:
                    Number = int(NameSplitArray[2])
                    if Number > Index:
                        Index = Number
        Index = Index + 1
        shapeTag = str("cylinder_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=['cylinder',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,outlinecolor,outlinewidth,dash[0],dash[1],None,'',None,'']
    DoCanvasRecord(drawCanvas,'cylinder',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash1=dash[0],dash2=dash[1],newImage=None,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag
def DrawStar(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):
    """在画布上画星星"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag == '':
        Index = 0
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            if ShepTagName.find('star_') == 0:
                NameSplitArray = ShepTagName.partition('star_')
                if NameSplitArray[2].isdigit() == True:
                    Number = int(NameSplitArray[2])
                    if Number > Index:
                        Index = Number
        Index = Index + 1
        shapeTag = str("star_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=['star',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,outlinecolor,outlinewidth,dash[0],dash[1],None,'',None,'']
    DoCanvasRecord(drawCanvas,'star',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash1=dash[0],dash2=dash[1],newImage=None,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag
def DrawText(uiName,drawCanvasName,x,y,text,textFont=None,color='#FFFFFF',anchor='nw',shapeTag=''):
    """在画布上写字"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag == '':
        Index = 0
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            if ShepTagName.find('text_') == 0:
                NameSplitArray = ShepTagName.partition('text_')
                if NameSplitArray[2].isdigit() == True:
                    Number = int(NameSplitArray[2])
                    if Number > Index:
                        Index = Number
        Index = Index + 1
        shapeTag = str("text_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=['text',x,y,x,y,text,textFont,color]
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,color,0,0,0,None,text,textFont,color]
    drawCanvas.create_text(x, y,fill=color,text=text,font = textFont,anchor=anchor,tag=shapeTag)
    return shapeTag
def DrawImage(uiName,drawCanvasName,x1,y1,x2,y2,imagefile,shapeTag=''):
    """在画布上显示图片"""
    global G_ResDir
    global G_ResourcesFileList
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    newImage = None
    hasGIFAnimation = False
    w = x2 - x1
    h = y2 - y1
    if uiName and uiName in G_CanvasImageDictionary:
        if drawCanvasName and drawCanvasName in G_CanvasImageDictionary[uiName]:
            for ImageInfo in G_CanvasImageDictionary[uiName][drawCanvasName]:
                if ImageInfo[0] == imagefile and ImageInfo[2] == w and ImageInfo[3] == h :
                    newImage = ImageInfo[1]
                    break
    else:
        return
    if shapeTag == '':
        Index = 0
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            if ShepTagName.find('image_') == 0:
                NameSplitArray = ShepTagName.partition('image_')
                if NameSplitArray[2].isdigit() == True:
                    Number = int(NameSplitArray[2])
                    if Number > Index:
                        Index = Number
        Index = Index + 1
        shapeTag = str("image_%d"%Index)
    if newImage == None:
        resourPath = imagefile
        if imagefile in G_ResourcesFileList:
            resourPath = G_ResourcesFileList[imagefile]
        if type(resourPath) == type(""):
            if os.path.exists(resourPath) == True:
                try:
                    if imagefile.find('.gif') >= 0:
                        GifData = Image.open(resourPath)
                        seq = []
                        try:
                            while 1:
                                imageRGBA = GifData.copy().convert('RGBA')
                                resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
                                newImage = ImageTk.PhotoImage(resizeImage)
                                seq.append(newImage)
                                GifData.seek(len(seq))
                        except EOFError:
                            pass
                        delay = 100
                        try:
                            delay = GifData.info['duration']
                        except KeyError:
                            delay = 100
                        if delay == 0:
                            delay = 100
                        newImage = [seq,delay,0]
                        hasGIFAnimation = True
                    else:
                        imageRGBA = Image.open(resourPath).convert('RGBA')
                        resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
                        newImage = ImageTk.PhotoImage(resizeImage)
                    if drawCanvasName not in G_CanvasImageDictionary[uiName]:
                        G_CanvasImageDictionary[uiName][drawCanvasName] = []
                    G_CanvasImageDictionary[uiName][drawCanvasName].append([imagefile,newImage,w,h])
                except:
                    return 
        elif type(imagefile) == type(Image):
            imageRGBA = imagefile
            resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
            newImage = ImageTk.PhotoImage(resizeImage)
            if drawCanvasName not in G_CanvasImageDictionary[uiName]:
                G_CanvasImageDictionary[uiName][drawCanvasName] = []
            G_CanvasImageDictionary[uiName][drawCanvasName].append([imagefile,newImage,w,h])
    if newImage:
        if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=['image',x1,y1,x2,y2,newImage,imagefile]
        if drawCanvasName not in G_CanvasParamDictionary[uiName]:
            G_CanvasParamDictionary[uiName][drawCanvasName] = {}
        G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=['#FFFFFF','#FFFFFF',0,0,0,newImage,'',None,'#FFFFFF']
        DoCanvasRecord(drawCanvas,'image',x1,y1,x2,y2,'#FFFFFF','#FFFFFF',0,dash1=0,dash2=0,newImage=newImage,text='',textFont = None,textColor='',shapeTag=shapeTag)
        if hasGIFAnimation == True:
            drawCanvas.after(100,updateGIFFrame(uiName))
def DrawButton(uiName,drawCanvasName,x1,y1,x2,y2,text='',textcolor='#000000',textFont = None,fillcolor='#FFFFFF',outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):
    """在画布上显示圆角按钮"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    center_x = (x1 + x2)/2
    center_y = (y1 + y2)/2
    oval_rx = 20
    dash1=dash[0],dash2=dash[1]
    OutLineTag = shapeTag+"_outline"
    half_width = int((outlinewidth+1)/2)
    if shapeTag == '':
        Index = 0
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            if ShepTagName.find('button_') == 0:
                NameSplitArray = ShepTagName.partition('button_')
                if NameSplitArray[2].isdigit() == True:
                    Number = int(NameSplitArray[2])
                    if Number > Index:
                        Index = Number
        Index = Index + 1
        shapeTag = str("button_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=['button',x1,y1,x2,y2,text,textcolor,textFont,fillcolor,outlinecolor,outlinewidth,dash[0],dash[1],None]
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[fillcolor,outlinecolor,outlinewidth,dash[0],dash[1],None,text,textFont,textcolor]
    if  dash1 > 0 :
        drawCanvas.create_oval(x1,y1,x1+2*oval_rx,y2,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = outlinewidth,tag=shapeTag)
        drawCanvas.create_oval(x2-2*oval_rx,y1,x2,y2,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = outlinewidth,tag=shapeTag)
        drawCanvas.create_rectangle(x1+oval_rx, y1, x2-oval_rx, y2,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2), width = outlinewidth,tag=shapeTag)
        drawCanvas.create_line(x1+oval_rx, y1+half_width, x1+oval_rx, y2-half_width,fill=fillcolor,width = outlinewidth,tag=OutLineTag)
        drawCanvas.create_line(x2-oval_rx, y1+half_width, x2-oval_rx, y2-half_width,fill=fillcolor,width = outlinewidth,tag=OutLineTag)
    else:
        drawCanvas.create_oval(x1,y1,x1+2*oval_rx,y2,fill=fillcolor,outline=outlinecolor,width = outlinewidth,tag=shapeTag)
        drawCanvas.create_oval(x2-2*oval_rx,y1,x2,y2,fill=fillcolor,outline=outlinecolor,width = outlinewidth,tag=shapeTag)
        drawCanvas.create_rectangle(x1+oval_rx, y1, x2-oval_rx, y2,fill=fillcolor,outline=outlinecolor, width = outlinewidth,tag=shapeTag)
        drawCanvas.create_line(x1+oval_rx, y1+half_width, x1+oval_rx, y2-half_width,fill=fillcolor,width = outlinewidth,tag=OutLineTag)
        drawCanvas.create_line(x2-oval_rx, y1+half_width, x2-oval_rx, y2-half_width,fill=fillcolor,width = outlinewidth,tag=OutLineTag)
    if len(text) > 0:
        drawCanvas.create_text(center_x, center_y,text=text,fill=textcolor,anchor='center',tag=shapeTag+"_text")
def EraserCanvas(uiName,drawCanvasName,x1,y1,x2,y2):
    """在画布上檫去区域"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    bgcolor = drawCanvas.cget('bg')
    DoCanvasRecord(drawCanvas,'eraser',x1,y1,x2,y2,bgcolor,bgcolor,0,dash1=0,dash2=0,newImage=None,text='',textFont = None,textColor='',shapeTag='')
def checkPtInRect(x,y,left,right,top,bottom):
    if x < left:return 0
    if x > right:return 0
    if y < top:return 0
    if y > bottom:return 0
    return 1
def Shape_MouseEvent(event,uiName,canvasName,shapeTag,eventName):
    if eventName == 'MouseLeave':
        x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]
        y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]
        x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]
        y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]
        if type(x1) == type(1.0):
            x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
        if type(y1) == type(1.0):
            y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
        if type(x2) == type(1.0):
            if x2 <= 1.0:
                x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
            else:
                x2 = x1 + int(x2)
        if type(y2) == type(1.0):
            if y2 <= 1.0:
                y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
            else:
                y2 = y1 + int(y2)
        borderwidth = 0
        if G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0] == 'button':
            borderwidth = 1 + G_CanvasShapeDictionary[uiName][canvasName][shapeTag][10]
        if checkPtInRect(event.x,event.y,x1+borderwidth,x2-borderwidth,y1+borderwidth,y2-borderwidth) == 1:
            return 
    if shapeTag not in G_CanvasEventDictionary[uiName][canvasName]:
        return
    if eventName not in G_CanvasEventDictionary[uiName][canvasName][shapeTag]:
        return
    for actionInfo in G_CanvasEventDictionary[uiName][canvasName][shapeTag][eventName]:
        if actionInfo[0] == "SetShapeRect":
            SetShapeRect(uiName ,canvasName,actionInfo[1],actionInfo[2],actionInfo[3],actionInfo[4],actionInfo[5])
        elif actionInfo[0] == "SetFillColor":
            SetShapeFillColor(uiName ,canvasName,actionInfo[1],actionInfo[2])
        elif actionInfo[0] == "SetOutlineColor":
            SetShapeOutlineColor(uiName ,canvasName,actionInfo[1],actionInfo[2])
        elif actionInfo[0] == "ChangeImage":
            SetShapeImage(uiName ,canvasName,actionInfo[1],actionInfo[2])
        elif actionInfo[0] == "ChangeText":
            SetShapeText(uiName ,canvasName,actionInfo[1],actionInfo[2],actionInfo[3])
        elif actionInfo[0] == "JumpToUI":
            UIPath, UIFile = os.path.split(actionInfo[2])
            UIName, extension = os.path.splitext(UIFile)
            if len(UIPath) > 0:
                import sys
                sys.path.append(UIPath)
            GoToUIDialog(uiName,UIName)
        elif actionInfo[0] == "LoadUI":
            WidgetName = actionInfo[2]
            UIPath, UIFile = os.path.split(actionInfo[3])
            UIName, extension = os.path.splitext(UIFile)
            if len(UIPath) > 0:
                import sys
                sys.path.append(UIPath)
            if WidgetName == "Form_1":
                WidgetName == "root"
            LoadUIDialog(uiName,WidgetName,UIName)
        elif actionInfo[0] == "DeleteShape":
            DeleteShape(uiName ,canvasName,actionInfo[1])
        elif actionInfo[0] == "OnSwitch":
            OnSwitch(uiName ,canvasName,actionInfo[1],actionInfo)
        elif actionInfo[0] == "OnExpandOrShrink":
            OnExpandOrShrink(uiName ,canvasName,actionInfo[1],actionInfo)
        elif actionInfo[0] == "CallFunction":
            if actionInfo[1]:
                if actionInfo[2]:
                   actionInfo[1](event,uiName,canvasName,actionInfo[2])
                else:
                   actionInfo[1](event,uiName,canvasName)
def updateGIFFrame(uiName):
    """更新GIF动画"""
    global G_CanvasShapeDictionary
    global G_CanvasImageDictionary
    for drawCanvasName in G_CanvasShapeDictionary[uiName]:
        drawCanvas = GetElement(uiName,drawCanvasName)
        for shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            ShapeInfo = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]
            if ShapeInfo[0] == 'image':
                if type(ShapeInfo[5]) == type([]):
                    FrameIndex = ShapeInfo[5][2]
                    FrameImages = ShapeInfo[5][0]
                    x = ShapeInfo[1]
                    y = ShapeInfo[2]
                    newImage = FrameImages[FrameIndex]
                    drawCanvas.delete(shapeTag)
                    drawCanvas.create_image(x, y,image=newImage,anchor='nw',tag=shapeTag)
                    FrameIndex = FrameIndex + 1
                    if FrameIndex == len(FrameImages):
                         FrameIndex = 0
                    ShapeInfo[5][2] = FrameIndex
        drawCanvas.after(100,lambda: updateGIFFrame(uiName))
    if uiName in G_CanvasImageDictionary:
        for elementName in G_CanvasImageDictionary[uiName]:   
            if elementName.find('Label_') == 0 or elementName.find('Button_') == 0 or elementName.find('RadioButton_') == 0 or elementName.find('CheckButton_') == 0:
                Control = GetElement(uiName,elementName)
                if Control != None:     
                    for imageInfo in G_CanvasImageDictionary[uiName][elementName]:
                        if type(imageInfo) == type([]):
                            GifData = imageInfo[1]
                            FrameSequ = GifData[0]
                            FrameIndex = GifData[2]
                            Control.configure(image = FrameSequ[FrameIndex])
                            FrameIndex = FrameIndex + 1
                            if FrameIndex == len(FrameSequ):
                                FrameIndex = 0
                            GifData[2] = FrameIndex
                    Control.after(100,lambda: updateGIFFrame(uiName))
def LoadCanvasRecord(uiName):
    """读取画板动作记录"""
    global G_ExeDir
    global G_ResDir
    global G_ResourcesFileList
    drawCanvasName = None
    drawCanvas = None
    drawCanvas_width = 0
    drawCanvas_height = 0
    canvasFile = os.path.join(G_ResDir,uiName + ".cav")
    if os.path.exists(canvasFile) == False:
        file_path = os.path.abspath(__file__)
        G_ExeDir = os.path.dirname(file_path)
        G_ResDir = os.path.join(G_ExeDir,"Resources")
        canvasFile = os.path.join(G_ResDir,uiName + ".cav")
    if os.path.exists(canvasFile) == True:
        f = open(canvasFile,encoding='utf-8')
        line ="" 
        while True:
            line = f.readline()
            if not line:
                break
            text = line.strip()
            if not text:
                continue
            if text.find('Canvas:') >= 0:
                splitArray = text.split(':')
                drawCanvasName = splitArray[1].strip()
                drawCanvas = GetElement(uiName,drawCanvasName)
                drawCanvas_width = drawCanvas.winfo_width()
                drawCanvas_height = drawCanvas.winfo_height()
                if drawCanvasName == "Form_1":
                    root = GetElement(uiName,"root")
                    drawCanvas_width = root.winfo_width()
                    drawCanvas_height = root.winfo_height()
                G_CanvasSizeDictionary[uiName][drawCanvasName] = [drawCanvas_width,drawCanvas_height]
                G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
                G_CanvasParamDictionary[uiName][drawCanvasName] = {}
                G_CanvasFontDictionary[uiName][drawCanvasName] = []
                G_CanvasImageDictionary[uiName][drawCanvasName] = []
                G_CanvasPointDictionary[uiName][drawCanvasName] = {}
                G_CanvasEventDictionary[uiName][drawCanvasName] = {}
                continue
            elif text.find(',') >= 0:
                if drawCanvas != None:
                    splitArray = text.split(',')
                    splitCount = len(splitArray)
                    ShapeType = splitArray[0]
                    if ShapeType == 'image':
                        if splitArray[1].find('.') > 0:
                            x1 = float(splitArray[1])
                        else:
                            x1 = int(splitArray[1])
                        if splitArray[2].find('.') > 0:
                            y1 = float(splitArray[2])
                        else:
                            y1 = int(splitArray[2])
                        if splitArray[3].find('.') > 0:
                            x2 = float(splitArray[3])
                        else:
                            x2 = int(splitArray[3])
                        if splitArray[4].find('.') > 0:
                            y2 = float(splitArray[4])
                        else:
                            y2 = int(splitArray[4])
                        w = int(x2 - x1)
                        if w < 1:
                            w = 1
                        h = int(y2 - y1)
                        if h < 1:
                            h = 1
                        fill = splitArray[5]
                        outline = splitArray[6]
                        width = int(splitArray[7])
                        dashx = int(splitArray[8])
                        dashy = int(splitArray[9])
                        imagefile = splitArray[10]
                        newImage = None
                        newtext = ''
                        textFont = None
                        textColor=''
                        shapeTag = ''
                        if len(splitArray) > 12:
                            shapeTag = splitArray[11]
                        for ImageInfo in G_CanvasImageDictionary[uiName][drawCanvasName]:
                            if ImageInfo[0] == imagefile and ImageInfo[2] == w and ImageInfo[3] == h :
                                newImage = ImageInfo[1]
                                continue
                        if newImage == None:
                            if imagefile in G_ResourcesFileList:
                                resourPath = G_ResourcesFileList[imagefile]
                                if os.path.exists(resourPath) == True:
                                    try:
                                        imageRGBA = Image.open(resourPath).convert('RGBA')
                                        resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
                                        newImage = ImageTk.PhotoImage(resizeImage)
                                    except:
                                        pass 
                            G_CanvasImageDictionary[uiName][drawCanvasName].append([imagefile,newImage,w,h])
                        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,newImage,imagefile]
                        G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
                    elif ShapeType == 'text':
                        if splitArray[1].find('.') > 0:
                            x1 = float(splitArray[1])
                        else:
                            x1 = int(splitArray[1])
                        if splitArray[2].find('.') > 0:
                            y1 = float(splitArray[2])
                        else:
                            y1 = int(splitArray[2])
                        if splitArray[3].find('.') > 0:
                            x2 = float(splitArray[3])
                        else:
                            x2 = int(splitArray[3])
                        if splitArray[4].find('.') > 0:
                            y2 = float(splitArray[4])
                        else:
                            y2 = int(splitArray[4])
                        w = x2 - x1
                        h = y2 - y1
                        fill = splitArray[5]
                        outline = splitArray[6]
                        width = int(splitArray[7])
                        dashx = int(splitArray[8])
                        dashy = int(splitArray[9])
                        imagefile = ''
                        newImage = None
                        shapeTag = ''
                        newtext = splitArray[10]
                        for i in range(11,splitCount-8):
                            newtext = newtext + ","+splitArray[i]
                        familytext = splitArray[-8]
                        sizetext = splitArray[-7]
                        weighttext = splitArray[-6]
                        slanttext = splitArray[-5]
                        underlinetext = splitArray[-4]
                        overstriketext = splitArray[-3]
                        textColor=''
                        textFont = tkinter.font.Font(family=familytext, size=sizetext,weight=weighttext,slant=slanttext,underline=underlinetext,overstrike=overstriketext)
                        shapeTag = splitArray[-2]
                        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,newtext,textFont,fill]
                        #字体
                        fontFind = False
                        for fontInfo in G_CanvasFontDictionary[uiName][drawCanvasName]:
                            if fontInfo[1] == familytext and fontInfo[2] == sizetext and fontInfo[3] == weighttext and fontInfo[4] == slanttext and fontInfo[5] == underlinetext and fontInfo[6] == overstriketext:
                                fontFind = True
                                continue
                        if fontFind == False:
                            G_CanvasFontDictionary[uiName][drawCanvasName].append([textFont,familytext,sizetext,weighttext,slanttext,underlinetext,overstriketext])
                        G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
                    elif ShapeType == 'button':
                        if splitArray[1].find('.') > 0:
                            x1 = float(splitArray[1])
                        else:
                            x1 = int(splitArray[1])
                        if splitArray[2].find('.') > 0:
                            y1 = float(splitArray[2])
                        else:
                            y1 = int(splitArray[2])
                        if splitArray[3].find('.') > 0:
                            x2 = float(splitArray[3])
                        else:
                            x2 = int(splitArray[3])
                        if splitArray[4].find('.') > 0:
                            y2 = float(splitArray[4])
                        else:
                            y2 = int(splitArray[4])
                        w = x2 - x1
                        h = y2 - y1
                        fill = splitArray[5]
                        outline = splitArray[6]
                        width = int(splitArray[7])
                        dashx = int(splitArray[8])
                        dashy = int(splitArray[9])
                        shapeTag = ''
                        newtext = splitArray[10]
                        for i in range(11,splitCount-11):
                            newtext = newtext + ","+splitArray[i]
                        familytext = splitArray[-11]
                        sizetext = splitArray[-10]
                        weighttext = splitArray[-9]
                        slanttext = splitArray[-8]
                        underlinetext = splitArray[-7]
                        overstriketext = splitArray[-6]
                        textColor = splitArray[-5]
                        textFont = None
                        if len(familytext) > 0:
                            textFont = tkinter.font.Font(family=familytext, size=sizetext,weight=weighttext,slant=slanttext,underline=underlinetext,overstrike=overstriketext)
                            #字体
                            fontFind = False
                            for fontInfo in G_CanvasFontDictionary[uiName][drawCanvasName]:
                                if fontInfo[1] == familytext and fontInfo[2] == sizetext and fontInfo[3] == weighttext and fontInfo[4] == slanttext and fontInfo[5] == underlinetext and fontInfo[6] == overstriketext:
                                    fontFind = True
                                    continue
                            if fontFind == False:
                                G_CanvasFontDictionary[uiName][drawCanvasName].append([textFont,familytext,sizetext,weighttext,slanttext,underlinetext,overstriketext])
                        imagefile = splitArray[-4]
                        newImage = None
                        if imagefile != "":
                            for ImageInfo in G_CanvasImageDictionary[uiName][drawCanvasName]:
                                if ImageInfo[0] == imagefile and ImageInfo[2] == w and ImageInfo[3] == h :
                                    newImage = ImageInfo[1]
                                    continue
                            if newImage == None:
                                if imagefile in G_ResourcesFileList:
                                    resourPath = G_ResourcesFileList[imagefile]
                                    if os.path.exists(resourPath) == True:
                                        try:
                                            imageRGBA = Image.open(resourPath).convert('RGBA')
                                            resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
                                            newImage = ImageTk.PhotoImage(resizeImage)
                                        except:
                                            return 
                                G_CanvasImageDictionary[uiName][drawCanvasName].append([imagefile,newImage,w,h])
                        shapeTag = splitArray[-2]
                        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,newtext,textColor,textFont,fill,outline,width,dashx,dashy,newImage]
                        G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
                    elif ShapeType == 'roundrect':
                        if len(splitArray) > 11:
                            if splitArray[1].find('.') > 0:
                                x1 = float(splitArray[1])
                            else:
                                x1 = int(splitArray[1])
                            if splitArray[2].find('.') > 0:
                                y1 = float(splitArray[2])
                            else:
                                y1 = int(splitArray[2])
                            if splitArray[3].find('.') > 0:
                                x2 = float(splitArray[3])
                            else:
                                x2 = int(splitArray[3])
                            if splitArray[4].find('.') > 0:
                                y2 = float(splitArray[4])
                            else:
                                y2 = int(splitArray[4])
                            w  = x2 - x1
                            h  = y2 - y1
                            fill = splitArray[5]
                            outline = splitArray[6]
                            width = int(splitArray[7])
                            dashx = int(splitArray[8])
                            dashy = int(splitArray[9])
                            imagefile = int(splitArray[10])
                            newImage = imagefile
                            newtext = ''
                            textFont = None
                            textColor = ''
                            shapeTag = splitArray[11]
                            G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy]
                            G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]
                            DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
                    elif ShapeType == 'point':
                        if splitArray[1].find('.') > 0:
                            x1 = float(splitArray[1])
                        else:
                            x1 = int(splitArray[1])
                        if splitArray[2].find('.') > 0:
                            y1 = float(splitArray[2])
                        else:
                            y1 = int(splitArray[2])
                        if splitArray[3].find('.') > 0:
                            x2 = float(splitArray[3])
                        else:
                            x2 = int(splitArray[3])
                        if splitArray[4].find('.') > 0:
                            y2 = float(splitArray[4])
                        else:
                            y2 = int(splitArray[4])
                        w  = x2 - x1
                        h  = y2 - y1
                        fill = splitArray[5]
                        outline = splitArray[6]
                        width = int(splitArray[7])
                        dashx = int(splitArray[8])
                        dashy = int(splitArray[9])
                        parentShapeTag = splitArray[10]
                        imagefile = ''
                        newImage = None
                        newtext = ''
                        textFont = None
                        textColor = ''
                        shapeTag = ''
                        centerX = (x1 + x2)*0.5
                        if centerX  > 1.0:
                            centerX = int(centerX)
                        centerY = (y1 + y2)*0.5
                        if centerY  > 1.0:
                            centerY = int(centerY)
                        if len(splitArray) > 12:
                            shapeTag = splitArray[11]
                            G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=(ShapeType,x1,y1,x2,y2)
                        if parentShapeTag not in G_CanvasPointDictionary[uiName][drawCanvasName]:
                            G_CanvasPointDictionary[uiName][drawCanvasName][parentShapeTag] = {}
                        G_CanvasPointDictionary[uiName][drawCanvasName][parentShapeTag][shapeTag] = [centerX,centerY]
                        G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
                    elif ShapeType == 'SetShapeRect':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = splitArray[3]
                        if splitArray[4].find('.') > 0:
                            x = float(splitArray[4])
                        else:
                            x = int(splitArray[4])
                        if splitArray[5].find('.') > 0:
                            y = float(splitArray[5])
                        else:
                            y = int(splitArray[5])
                        if splitArray[6].find('.') > 0:
                            w = float(splitArray[6])
                        else:
                            w = int(splitArray[6])
                        if splitArray[7].find('.') > 0:
                            h = float(splitArray[7])
                        else:
                            h = int(splitArray[7])
                        actionInfo = ["SetShapeRect",TargetShapeTag,x,y,w,h]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'SetFillColor':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = splitArray[3]
                        Color = splitArray[4]   
                        actionInfo = ["SetFillColor",TargetShapeTag,Color]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'SetOutlineColor':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = splitArray[3]
                        Color = splitArray[4]   
                        actionInfo = ["SetOutlineColor",TargetShapeTag,Color]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'ChangeImage':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = splitArray[3]
                        ImageFile = splitArray[4]
                        actionInfo = ["ChangeImage",TargetShapeTag,ImageFile]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'ChangeText':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = splitArray[3]
                        Text = splitArray[4]
                        TextColor = splitArray[5]
                        actionInfo = ["ChangeText",TargetShapeTag,Text,TextColor]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'JumpToUI':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetUIName = splitArray[3]
                        actionInfo = ["JumpToUI",shapeTag,TargetUIName]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'LoadUI':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        WidgetName = splitArray[3]
                        TargetUIName = splitArray[4]
                        actionInfo = ["LoadUI",shapeTag,WidgetName,TargetUIName]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'DeleteShape':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = splitArray[3]
                        actionInfo = ["DeleteShape",TargetShapeTag]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'OnSwitch':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = shapeTag
                        actionInfo = ["OnSwitch",TargetShapeTag,True]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'CallFunction':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        FunctionName = drawCanvasName+"_"+shapeTag+"_on"+EventName
                        CallBackFunc = None
                        if hasattr(G_UICommandDictionary[uiName],FunctionName) == True:
                            CallBackFunc = getattr(G_UICommandDictionary[uiName],FunctionName)
                        actionInfo = ["CallFunction",CallBackFunc,None]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    else:
                        if len(splitArray) > 11:
                            if splitArray[1].find('.') > 0:
                                x1 = float(splitArray[1])
                            else:
                                x1 = int(splitArray[1])
                            if splitArray[2].find('.') > 0:
                                y1 = float(splitArray[2])
                            else:
                                y1 = int(splitArray[2])
                            if splitArray[3].find('.') > 0:
                                x2 = float(splitArray[3])
                            else:
                                x2 = int(splitArray[3])
                            if splitArray[4].find('.') > 0:
                                y2 = float(splitArray[4])
                            else:
                                y2 = int(splitArray[4])
                            w  = x2 - x1
                            h  = y2 - y1
                            fill = splitArray[5]
                            outline = splitArray[6]
                            width = int(splitArray[7])
                            dashx = int(splitArray[8])
                            dashy = int(splitArray[9])
                            imagefile = ''
                            newImage = None
                            newtext = ''
                            textFont = None
                            textColor = ''
                            shapeTag = splitArray[10]
                            G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy]
                            G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]
                            DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
                continue
        f.close()  
        if uiName in G_CanvasEventDictionary:
            for drawCanvasName in G_CanvasEventDictionary[uiName].keys():
                drawCanvas = GetElement(uiName,drawCanvasName)
                for shapeTag in G_CanvasEventDictionary[uiName][drawCanvasName].keys():
                    for EventName in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                        if EventName == "MouseEnter":
                            drawCanvas.tag_bind(shapeTag, "<Any-Enter>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="MouseEnter"))
                            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName] and G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                                TextTag = shapeTag+"_text"
                                drawCanvas.tag_bind(TextTag, "<Any-Enter>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="MouseEnter"))
                        elif EventName == "MouseLeave":
                            drawCanvas.tag_bind(shapeTag, "<Any-Leave>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="MouseLeave"))
                            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName] and G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                                TextTag = shapeTag+"_text"
                                drawCanvas.tag_bind(TextTag, "<Any-Leave>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="MouseLeave"))
                        elif EventName == "ButtonDown":
                            drawCanvas.tag_bind(shapeTag, "<Button-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonDown"))
                            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName] and G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                                TextTag = shapeTag+"_text"
                                drawCanvas.tag_bind(TextTag, "<Button-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonDown"))
                        elif EventName == "ButtonMotion":
                            drawCanvas.tag_bind(shapeTag, "<B1-Motion>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonMotion"))
                            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName] and G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                                TextTag = shapeTag+"_text"
                                drawCanvas.tag_bind(TextTag, "<B1-Motion>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonMotion"))
                        elif EventName == "ButtonUp":
                            drawCanvas.tag_bind(shapeTag, "<ButtonRelease-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonUp"))
                            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName] and G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                                TextTag = shapeTag+"_text"
                                drawCanvas.tag_bind(TextTag, "<ButtonRelease-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonUp"))
                        elif EventName == "DoubleClick":
                            drawCanvas.tag_bind(shapeTag, "<Double-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="DoubleClick"))
                            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName] and G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                                TextTag = shapeTag+"_text"
                                drawCanvas.tag_bind(TextTag, "<Double-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="DoubleClick"))
def GetShapePoint(uiName,drawCanvasName,shapeTag,pointTag,absoluteMode=True):
    """获取绑定点位置"""
    if uiName not in G_CanvasShapeDictionary:
        return None
    if drawCanvasName in G_CanvasShapeDictionary[uiName]:
        if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            if shapeTag in G_CanvasPointDictionary[uiName][drawCanvasName]:
                parentX1,parentY1,parentX2,parentY2 = GetShapeRect(uiName,drawCanvasName,shapeTag)
                if pointTag in G_CanvasPointDictionary[uiName][drawCanvasName][shapeTag]:
                    shapeX = G_CanvasPointDictionary[uiName][drawCanvasName][shapeTag][pointTag][0]
                    shapeY = G_CanvasPointDictionary[uiName][drawCanvasName][shapeTag][pointTag][1]
                    if type(shapeX) == type(1.0):
                        shapeX = int(shapeX * (parentX2-parentX1))
                    if type(shapeY) == type(1.0):
                        shapeY = int(shapeY * (parentX2-parentX1))
                    if absoluteMode == True:
                        shapeX = shapeX + parentX1
                        shapeY = shapeY + parentY1
                    return (shapeX,shapeY)
    return None
def SetShapeRect(uiName,canvasName,shapeTag,x1,y1,x2,y2):
    """设置矩形位置大小"""
    if uiName in G_CanvasShapeDictionary:
        drawCanvas = GetElement(uiName,canvasName)
        if canvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:
                if shapeTag.find('text_') >= 0:
                    drawCanvas.coords(shapeTag, x1,y1) 
                else:
                    try:
                        drawCanvas.coords(shapeTag, x1,y1,x2,y2) 
                    except:
                        drawCanvas.coords(shapeTag, x1,y1) 
                G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1] = x1
                G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2] = y1
                G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3] = x2
                G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4] = y2
def GetShapeRect(uiName,canvasName,shapeTag):
    """取得画布图形矩形位置大小"""
    if uiName in G_CanvasShapeDictionary:
        drawCanvas = GetElement(uiName,canvasName)
        if canvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:
                x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]
                if type(x1) == type(1.0):
                    x1 = round(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]
                if type(y1) == type(1.0):
                    y1 = round(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]
                if type(x2) == type(1.0):
                    x2 = round(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]
                if type(y2) == type(1.0):
                    y2 = round(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                return (x1,y1,x2,y2)
    return None
def SetShapeFillColor(uiName,canvasName,shapeTag,color):
    """设置图形填充颜色"""
    if uiName in G_CanvasShapeDictionary:
        if canvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:
                if G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0] == 'button':
                    if G_CanvasShapeDictionary[uiName][canvasName][shapeTag][-1] == None:
                        drawCanvas = GetElement(uiName,canvasName)
                        drawCanvas.itemconfig(shapeTag, fill=color)
                        OutlineTag = shapeTag+"_outline"
                        drawCanvas.itemconfig(OutlineTag, fill=color)
                        G_CanvasParamDictionary[uiName][canvasName][shapeTag][0]=color
                elif G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0] == 'text':
                    drawCanvas = GetElement(uiName,canvasName)
                    drawCanvas.itemconfig(shapeTag, fill=color)
                    G_CanvasParamDictionary[uiName][canvasName][shapeTag][0]=color
                    G_CanvasParamDictionary[uiName][canvasName][shapeTag][8]=color
                else:
                    drawCanvas = GetElement(uiName,canvasName)
                    drawCanvas.itemconfig(shapeTag, fill=color)
                    G_CanvasParamDictionary[uiName][canvasName][shapeTag][0]=color
def GetShapeFillColor(uiName,canvasName,shapeTag):
    """取得画布图形颜色"""
    if uiName in G_CanvasShapeDictionary:
        if canvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:
                return G_CanvasShapeDictionary[uiName][canvasName][shapeTag][5]
    return None
def SetShapeOutlineColor(uiName,canvasName,shapeTag,color):
    """设置图形边框颜色"""
    if uiName in G_CanvasShapeDictionary:
        if canvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:
                if G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0] == 'cylinder':
                    drawCanvas = GetElement(uiName,canvasName)
                    drawCanvas.itemconfig(shapeTag, outline=color)
                    OutlineTag = shapeTag+"_outline"
                    drawCanvas.itemconfig(OutlineTag, fill=color)
                    G_CanvasParamDictionary[uiName][canvasName][shapeTag][1]=color
                elif G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0] == 'roundrect':
                    OutlineTag = shapeTag+"_outline"
                    ArcTag = shapeTag+"_arc"
                    drawCanvas = GetElement(uiName,canvasName)
                    drawCanvas.itemconfig(OutlineTag, fill=color)
                    drawCanvas.itemconfig(ArcTag, outline=color)
                    G_CanvasParamDictionary[uiName][canvasName][shapeTag][1]=color
                else:
                    drawCanvas = GetElement(uiName,canvasName)
                    drawCanvas.itemconfig(shapeTag, outline=color)
                    G_CanvasParamDictionary[uiName][canvasName][shapeTag][1]=color
def GetShapeOutlineColor(uiName,canvasName,shapeTag):
    """取得画布图形边框颜色"""
    if uiName in G_CanvasShapeDictionary:
        if canvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:
                return G_CanvasShapeDictionary[uiName][canvasName][shapeTag][6]
        return None
def SetShapeLineWidth(uiName,canvasName,shapeTag,width):
    """设置图形线条宽度"""
    if uiName in G_CanvasShapeDictionary:
        if canvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:
                if G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0] == 'button':
                    if G_CanvasShapeDictionary[uiName][canvasName][shapeTag][-1] == None:
                        drawCanvas = GetElement(uiName,canvasName)
                        drawCanvas.itemconfig(shapeTag, width=width)
                        G_CanvasParamDictionary[uiName][canvasName][shapeTag][2]=width
                elif G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0] == 'roundrect':
                    OutlineTag = shapeTag+"_outline"
                    ArcTag = shapeTag+"_arc"
                    drawCanvas = GetElement(uiName,canvasName)
                    drawCanvas.itemconfig(OutlineTag, width=width)
                    G_CanvasParamDictionary[uiName][canvasName][shapeTag][2]=width
                else:
                    drawCanvas = GetElement(uiName,canvasName)
                    drawCanvas.itemconfig(shapeTag, width=width)
                    G_CanvasParamDictionary[uiName][canvasName][shapeTag][2]=width
def SetShapeImage(uiName,canvasName,shapeTag,imageFile):
    """更换图片文件"""
    global G_ResourcesFileList
    if uiName in G_CanvasShapeDictionary:
        drawCanvas = GetElement(uiName,canvasName)
        if canvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:
                x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]
                y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]
                x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]
                y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]
                if type(x1) == type(1.0):
                    x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                if type(y1) == type(1.0):
                    y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                if type(x2) == type(1.0):
                    if x2 <= 1.0:
                        x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                    else:
                        x2 = x1 + int(x2)
                if type(y2) == type(1.0):
                    if y2 <= 1.0:
                        y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                    else:
                        y2 = y1 + int(y2)
                w = x2 - x1
                h = y2 - y1
                newImage = None
                for ImageInfo in G_CanvasImageDictionary[uiName][canvasName]:
                    if ImageInfo[0] == imageFile and ImageInfo[2] == w and ImageInfo[3] == h :
                        newImage = ImageInfo[1]
                        continue
                if newImage == None:
                    if imageFile in G_ResourcesFileList:
                        resourPath = G_ResourcesFileList[imageFile]
                        if os.path.exists(resourPath) == True:
                            try:
                                imageRGBA = Image.open(resourPath).convert('RGBA')
                                resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
                                newImage = ImageTk.PhotoImage(resizeImage)
                            except:
                                return 
                    G_CanvasImageDictionary[uiName][canvasName].append([imageFile,newImage,w,h])
                G_CanvasShapeDictionary[uiName][canvasName][shapeTag][5] = newImage
                G_CanvasShapeDictionary[uiName][canvasName][shapeTag][6] = imageFile
                drawCanvas.itemconfig(shapeTag, image=newImage) 
def GetShapeImage(uiName,canvasName,shapeTag):
    """取得画布图形图片文件"""
    if uiName in G_CanvasShapeDictionary:
        if canvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:
                return G_CanvasShapeDictionary[uiName][canvasName][shapeTag][5]
    return None
def SetShapeText(uiName,drawCanvasName,shapeTag,text,color = None):
    """设置画布文字及颜色"""
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:
                drawCanvas = GetElement(uiName,drawCanvasName)
                G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][5] = text
                shapeTextTag = shapeTag
                textcolor = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][7]
                if G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                    shapeTextTag = shapeTag+"_text"
                    textcolor = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][6]
                if color:
                    textcolor = color
                G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag][6] = text
                G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag][8] = textcolor
                drawCanvas.itemconfigure(shapeTextTag,text=text)
                drawCanvas.itemconfigure(shapeTextTag,fill=textcolor)
def GetShapeText(uiName,drawCanvasName,shapeTag):
    """取得画布图形文字与颜色"""
    if uiName not in G_CanvasShapeDictionary:
        return None
    if drawCanvasName in G_CanvasParamDictionary[uiName]:
        if shapeTag in G_CanvasParamDictionary[uiName][drawCanvasName]:
            text = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag][6]
            textColor = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag][8]
            return (text,textColor)
    return None
def BindShapeEvent_SetShapeRect(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,x,y,w,h):
    """绑定事件-设置图形位置与大小"""
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:
                actionInfo = ["SetShapeRect",targetShapeTag,x,y,w,h]
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeEvent_SetFillColor(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,color):
    """绑定事件-设置图形颜色"""
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:
                actionInfo = ["SetFillColor",targetShapeTag,color]
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeEvent_SetOutlineColor(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,color):
    """绑定事件-设置图形边框颜色"""
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:
                actionInfo = ["SetOutlineColor",targetShapeTag,color]
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeEvent_ChangeImage(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,ImageFile):
    """绑定事件-更换图形图片"""
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:
                actionInfo = ["ChangeImage",targetShapeTag,ImageFile]
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeEvent_ChangeText(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,Text,TextColor):
    """绑定事件-设置图形文字"""
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:
                actionInfo = ["ChangeText",targetShapeTag,Text,TextColor]
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeEvent_JumpToUI(uiName,drawCanvasName,shapeTag,bindEvent,targetUIName):
    """绑定事件-跳转其它界面"""
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:
                actionInfo = ["JumpToUI",shapeTag,targetUIName]
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeEvent_LoadUI(uiName,drawCanvasName,shapeTag,bindEvent,widgetName,targetUIName):
    """绑定事件-嵌入界面"""
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:
                actionInfo = ["LoadUI",shapeTag,widgetName,targetUIName]
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeEvent_DeleteShape(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag):
    """绑定事件-删除图形"""
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:
                actionInfo = ["DeleteShape",targetShapeTag]
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeEvent_CallFunction(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,callBackFuncton,param = None):
    """绑定事件-调用函数"""
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:
                actionInfo = ["CallFunction",callBackFuncton,param]
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo):
    """对绑定事件进行处理"""
    if uiName in G_CanvasShapeDictionary:
        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
        if bindEvent not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][bindEvent] = []
        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][bindEvent].append(actionInfo)
        drawCanvas = GetElement(uiName,drawCanvasName)
        if bindEvent == "MouseEnter":
            drawCanvas.tag_bind(shapeTag, "<Any-Enter>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="MouseEnter"))
            if G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                TextTag = shapeTag+"_text"
                drawCanvas.tag_bind(TextTag, "<Any-Enter>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="MouseEnter"))
        elif bindEvent == "MouseLeave":
            drawCanvas.tag_bind(shapeTag, "<Any-Leave>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="MouseLeave"))
            if G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                TextTag = shapeTag+"_text"
                drawCanvas.tag_bind(TextTag, "<Any-Leave>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="MouseLeave"))
        elif bindEvent == "ButtonDown":
            drawCanvas.tag_bind(shapeTag, "<Button-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonDown"))
            if G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                TextTag = shapeTag+"_text"
                drawCanvas.tag_bind(TextTag, "<Button-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonDown"))
        elif bindEvent == "ButtonMotion":
            drawCanvas.tag_bind(shapeTag, "<B1-Motion>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonMotion"))
            if G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                TextTag = shapeTag+"_text"
                drawCanvas.tag_bind(TextTag, "<B1-Motion>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonMotion"))
        elif bindEvent == "ButtonUp":
            drawCanvas.tag_bind(shapeTag, "<ButtonRelease-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonUp"))
            if G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                TextTag = shapeTag+"_text"
                drawCanvas.tag_bind(TextTag, "<ButtonRelease-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonUp"))
        elif bindEvent == "DoubleClick":
            drawCanvas.tag_bind(shapeTag, "<Double-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="DoubleClick"))
            if G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                TextTag = shapeTag+"_text"
                drawCanvas.tag_bind(TextTag, "<Double-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="DoubleClick"))
def OnSwitch(uiName,drawCanvasName,shapeTag,actionInfo):
    """切换开关"""
    if uiName not in G_CanvasShapeDictionary:
        return None
    if drawCanvasName in G_CanvasShapeDictionary[uiName]:
        if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            drawCanvas = GetElement(uiName,drawCanvasName)
            drawCanvas.delete(shapeTag)
            x1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][1]
            y1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][2]
            x2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][3]
            y2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][4]
            SwitchWidth = x2 - x1
            SwitchHeight = y2 - y1
            Switch_radius = int(SwitchHeight/2)
            fillcolor = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][5]
            outlinecolor = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][6]
            if actionInfo[2] == False:
                fillcolor = '#777777'
                drawCanvas.create_oval(x1, y1, x1+SwitchHeight, y1+SwitchHeight-1,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
                drawCanvas.create_oval(x1+(SwitchWidth-SwitchHeight), y1, x1+SwitchWidth,y1+ SwitchHeight-1,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
                drawCanvas.create_rectangle(x1+Switch_radius,y1,x1+(SwitchWidth-Switch_radius),y1+SwitchHeight,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
                drawCanvas.create_oval(x1+2, y1+2, x1+(SwitchHeight-3), y1+(SwitchHeight-3),fill=outlinecolor,width=0,tag=shapeTag)
                drawCanvas.create_text(x1+(SwitchWidth-int(1.0*SwitchHeight)), y1+int(SwitchHeight/2), text="Off",font = ("System",int(SwitchHeight/2)),anchor='center',fill=outlinecolor,width=0,tag=shapeTag)
                actionInfo[2] = True
            else:
                drawCanvas.create_oval(x1, y1, x1+SwitchHeight, y1+SwitchHeight-1,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
                drawCanvas.create_oval(x1+(SwitchWidth-SwitchHeight), y1, x1+SwitchWidth,y1+ SwitchHeight-1,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
                drawCanvas.create_rectangle(x1+Switch_radius,y1,x1+(SwitchWidth-Switch_radius),y1+SwitchHeight,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
                drawCanvas.create_oval(x1+(SwitchWidth-SwitchHeight)-2, y1+2, x1+SwitchWidth-3, y1+(SwitchHeight-3),fill=outlinecolor,width=0,tag=shapeTag)
                drawCanvas.create_text(x1+int(0.8*SwitchHeight), y1+int(SwitchHeight/2), text="On",font = ("System",int(SwitchHeight/2)),anchor='center',fill=outlinecolor,width=0,tag=shapeTag)
                actionInfo[2] = False
def OnExpandOrShrink(uiName,drawCanvasName,shapeTag,actionInfo):
    """展开或收缩菜单"""
    if uiName not in G_CanvasShapeDictionary:
        return None
    if drawCanvasName in G_CanvasShapeDictionary[uiName]:
        listmenuNameIndex = shapeTag.rfind('_')
        listmenuName = shapeTag[0:listmenuNameIndex]
        if listmenuName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            drawCanvas = GetElement(uiName,drawCanvasName)
            drawCanvas.delete('drawing_shape')
            drawInfo = G_CanvasShapeDictionary[uiName][drawCanvasName][listmenuName]
            MenuInfo = drawInfo[10]
            SubMenus = MenuInfo['SubMenus']
            x1 = drawInfo[1]
            y1 = drawInfo[2]
            x2 = drawInfo[3]
            y2 = drawInfo[4]
            fillcolor = drawInfo[5]
            outlinecolor = drawInfo[6]
            fillwidth = int(drawInfo[7])
            dashx = int(drawInfo[8])
            dashy = int(drawInfo[9])
            for subMenu in SubMenus:
                titleText = subMenu[0]
                bgImgFile = subMenu[1]
                itemList = subMenu[2]
                subMenuTag = listmenuName +"_"+titleText
                drawCanvas.delete(subMenuTag)
                if shapeTag == subMenuTag:
                    if subMenu[3] == True:
                        subMenu[3] = False
                    else:
                        subMenu[3] = True
            DoCanvasRecord(drawCanvas,"listmenu",x1,y1,x2,y2,fillcolor,outlinecolor,fillwidth,dash1=0,dash2=0,newImage=MenuInfo,text='',textFont = None,textColor='',shapeTag=listmenuName)
            for subMenu in SubMenus:
                titleText = subMenu[0]
                subMenuTag = listmenuName +"_"+titleText
                drawCanvas.tag_bind(subMenuTag, "<Button-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=subMenuTag,eventName="ButtonDown"))
def DeleteShape(uiName,drawCanvasName,shapeTag):
    """删除画布中的画形"""
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:
                drawCanvas = GetElement(uiName,drawCanvasName)
                drawCanvas.delete(shapeTag)
                OutLineTag = shapeTag+"_outline"
                drawCanvas.delete(OutLineTag)
                G_CanvasShapeDictionary[uiName][drawCanvasName].pop(shapeTag)
                if drawCanvasName in G_CanvasEventDictionary[uiName]:
                    if shapeTag in G_CanvasEventDictionary[uiName][drawCanvasName]:
                        G_CanvasEventDictionary[uiName][drawCanvasName].pop(shapeTag)
                if drawCanvasName in G_CanvasParamDictionary[uiName]:
                    if shapeTag in G_CanvasParamDictionary[uiName][drawCanvasName]:
                        G_CanvasParamDictionary[uiName][drawCanvasName].pop(shapeTag)
def ReDrawCanvasShape(uiName,canvasName):
    global G_ResourcesFileList
    global G_CanvasSizeDictionary
    global G_CanvasShapeDictionary
    global G_UIElementAliasDictionary
    hasGIFAnimation = False
    if uiName in G_UIElementAliasDictionary.keys() and canvasName in G_UIElementAliasDictionary[uiName].keys():
        canvasName = G_UIElementAliasDictionary[uiName][canvasName]
    drawCanvas = GetElement(uiName,canvasName)
    if drawCanvas:
        if uiName in G_CanvasSizeDictionary:
            if  canvasName in G_CanvasSizeDictionary[uiName]:
                for shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:
                    ShapeType = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0]
                    if ShapeType == 'image':
                        x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]
                        y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]
                        x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]
                        y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]
                        image_handle = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][5]
                        image_filename = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][6]
                        if type(x1) == type(1.0):
                            x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                        if type(y1) == type(1.0):
                            y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                        if type(x2) == type(1.0):
                            if x2 <= 1.0:
                                x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                            else:
                                x2 = x1 + int(x2)
                        if type(y2) == type(1.0):
                            if y2 <= 1.0:
                                y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                            else:
                                y2 = y1 + int(y2)
                        w = x2 - x1
                        h = y2 - y1
                        if w == 1 and h == 1:
                            continue
                        newImage = None
                        if newImage == None:
                            if image_filename in G_ResourcesFileList:
                                resourPath = G_ResourcesFileList[image_filename]
                                if os.path.exists(resourPath) == True:
                                    try:
                                        if image_filename.find('.gif') >= 0:
                                            GifData = Image.open(resourPath)
                                            seq = []
                                            try:
                                                while 1:
                                                    imageRGBA = GifData.copy().convert('RGBA')
                                                    resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
                                                    newImage = ImageTk.PhotoImage(resizeImage)
                                                    seq.append(newImage)
                                                    GifData.seek(len(seq))
                                            except EOFError:
                                                pass
                                            delay = 100
                                            try:
                                                delay = GifData.info['duration']
                                            except KeyError:
                                                delay = 100
                                            if delay == 0:
                                                delay = 100
                                            newImage = [seq,delay,0]
                                            hasGIFAnimation = True
                                        else:
                                            imageRGBA = Image.open(resourPath).convert('RGBA')
                                            resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
                                            newImage = ImageTk.PhotoImage(resizeImage)
                                    except Exception as Ex:
                                        OutputText = resourPath + ":"+str(Ex)
                                        print(OutputText)
                                        return 
                                else:
                                    print("找不到"+resourPath)
                            else:
                                print("Resources目录找不到"+image_filename)
                            #G_CanvasImageDictionary[uiName][canvasName].append([imagefile,newImage,w,h])
                            #G_CanvasShapeDictionary[uiName][canvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,newImage,image_filename]
                            G_CanvasShapeDictionary[uiName][canvasName][shapeTag][5] = newImage
                            G_CanvasParamDictionary[uiName][canvasName][shapeTag][5] = newImage
                            drawCanvas.delete(shapeTag)
                            Params = G_CanvasParamDictionary[uiName][canvasName][shapeTag]
                            DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                    elif ShapeType == 'text':
                        x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]
                        y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]
                        x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]
                        y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]
                        if type(x1) == type(1.0):
                            x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                        if type(y1) == type(1.0):
                            y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                        if type(x2) == type(1.0):
                            if x2 <= 1.0:
                                x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                            else:
                                x2 = x1 + int(x2)
                        if type(y2) == type(1.0):
                            if y2 <= 1.0:
                                y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                            else:
                                y2 = y1 + int(y2)
                        w = x2 - x1
                        h = y2 - y1
                        drawCanvas.delete(shapeTag)
                        Params = G_CanvasParamDictionary[uiName][canvasName][shapeTag]
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                    elif ShapeType == 'button':
                        x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]
                        y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]
                        x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]
                        y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]
                        if type(x1) == type(1.0):
                            x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                        if type(y1) == type(1.0):
                            y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                        if type(x2) == type(1.0):
                            if x2 <= 1.0:
                                x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                            else:
                                x2 = x1 + int(x2)
                        if type(y2) == type(1.0):
                            if y2 <= 1.0:
                                y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                            else:
                                y2 = y1 + int(y2)
                        w = x2 - x1
                        h = y2 - y1
                        drawCanvas.delete(shapeTag)
                        Params = G_CanvasParamDictionary[uiName][canvasName][shapeTag]
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                    elif ShapeType == 'point':
                        x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]
                        y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]
                        x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]
                        y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]
                        if type(x1) == type(1.0):
                            x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                        if type(y1) == type(1.0):
                            y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                        if type(x2) == type(1.0):
                            if x2 <= 1.0:
                                x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                            else:
                                x2 = x1 + int(x2)
                        if type(y2) == type(1.0):
                            if y2 <= 1.0:
                                y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                            else:
                                y2 = y1 + int(y2)
                        w = x2 - x1
                        h = y2 - y1
                        drawCanvas.delete(shapeTag)
                        Params = G_CanvasParamDictionary[uiName][canvasName][shapeTag]
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                    elif ShapeType == 'SetShapeRect':
                        pass
                    elif ShapeType == 'SetFillColor':
                        pass
                    elif ShapeType == 'SetOutlineColor':
                        pass
                    elif ShapeType == 'ChangeImage':
                        pass
                    elif ShapeType == 'ChangeText':
                        pass
                    elif ShapeType == 'JumpToUI':
                        pass
                    elif ShapeType == 'LoadUI':
                        pass
                    elif ShapeType == 'DeleteShape':
                        pass
                    elif ShapeType == 'OnSwitch':
                        pass
                    elif ShapeType == 'CallFunction':
                        pass
                    else:
                        x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]
                        y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]
                        x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]
                        y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]
                        if type(x1) == type(1.0):
                            x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                        if type(y1) == type(1.0):
                            y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                        if type(x2) == type(1.0):
                            if x2 <= 1.0:
                                x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                            else:
                                x2 = x1 + int(x2)
                        if type(y2) == type(1.0):
                            if y2 <= 1.0:
                                y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                            else:
                                y2 = y1 + int(y2)
                        w = x2 - x1
                        h = y2 - y1
                        drawCanvas.delete(shapeTag)
                        Params = G_CanvasParamDictionary[uiName][canvasName][shapeTag]
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
        drawCanvas.update()
        if hasGIFAnimation == True:
            drawCanvas.after(100,updateGIFFrame(uiName))
def ReDrawCanvasRecord(uiName,ForceReDraw=False):
    global G_ResourcesFileList
    global G_CanvasSizeDictionary
    ReDraw = False
    if uiName in G_CanvasSizeDictionary:
        for canvasName in G_CanvasSizeDictionary[uiName]:
            drawCanvas = GetElement(uiName,canvasName)
            drawCanvas_width = drawCanvas.winfo_width()
            drawCanvas_height = drawCanvas.winfo_height()
            if canvasName == "Form_1":
                root = GetElement(uiName,"root")
                drawCanvas_width = root.winfo_width()
                drawCanvas_height = root.winfo_height()
            if ForceReDraw == True or G_CanvasSizeDictionary[uiName][canvasName][0] != drawCanvas_width or G_CanvasSizeDictionary[uiName][canvasName][1] != drawCanvas_height:
                ReDraw = True
            G_CanvasSizeDictionary[uiName][canvasName] = [drawCanvas_width,drawCanvas_height]
    if ReDraw == True:
        if G_CanvasSizeDictionary[uiName][canvasName][0] == 1 and G_CanvasSizeDictionary[uiName][canvasName][1] == 1:
            return 
        print("ReDrawCanvasRecord")
        if uiName in G_CanvasShapeDictionary:
            for canvasName in G_CanvasSizeDictionary[uiName]:
                ReDrawCanvasShape(uiName,canvasName)
class FrameDraggable():
    """定义一个可拖拽的子窗口类"""
    def __init__(self,widget,hasChildren = True):
        if hasChildren == True:
            self.root = widget.root
            ChildWidgetList = widget.root.children
            for childKey in ChildWidgetList.keys():
                Form_1 = ChildWidgetList[childKey]
                Form_1.bind('<Button-1>',self.BeginDrag)
                Form_1.bind('<ButtonRelease-1>',self.EndDrag)
                Form_1.bind('<B1-Motion>',self.Draging)
        else:
            self.root = widget
            self.root.bind('<Button-1>',self.BeginDrag)
            self.root.bind('<ButtonRelease-1>',self.EndDrag)
            self.root.bind('<B1-Motion>',self.Draging)
    def BeginDrag(self,event):
        self.beginx = event.x_root
        self.beginy = event.y_root
    def Draging(self,event):
        offsetx = event.x_root - self.beginx 
        offsety = event.y_root - self.beginy
        x = self.root.winfo_x() + offsetx
        y = self.root.winfo_y() + offsety
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        self.root.place(x = x,y=y,width = w,height=h)
        self.beginx = event.x_root
        self.beginy = event.y_root
    def EndDrag(self,event):
        self.beginx = event.x_root
        self.beginy = event.y_root
class WindowDraggable():
    """定义一个可拖拽移动和拖拽边框大小的窗口类。"""
    def __init__(self,widget,dragmove=False,bordersize = 6,bordercolor = '#444444'):
        self.widget = widget
        if dragmove == True:
            widget.bind('<Enter>',self.Enter)
            widget.bind('<Motion>',self.Motion)
            widget.bind('<Leave>',self.Leave)
            widget.bind('<ButtonPress-1>',self.StartDrag)
            widget.bind('<ButtonRelease-1>',self.StopDrag)
            widget.bind('<B1-Motion>',self.MoveDragPos)
            widget.after(10, lambda: self.ShowWindowIcoToBar(widget))
        self.bordersize = bordersize
        self.bordercolor = bordercolor
        self.x = None
        self.y = None
        self.top_drag = None
        self.left_drag = None
        self.right_drag = None
        self.bottom_drag = None
        self.topleft_drag = None
        self.bottomleft_drag = None
        self.topright_drag = None
        self.bottomright_drag = None
    def ShowWindowIcoToBar(self,widget):
        GWL_EXSTYLE=-20
        WS_EX_APPWINDOW=0x00040000
        WS_EX_TOOLWINDOW=0x00000080
        from ctypes import windll
        hwnd = windll.user32.GetParent(widget.winfo_id())
        _winlib = windll.user32
        try :
            style = _winlib.GetWindowLongPtrW(hwnd, GWL_EXSTYLE)
            style = style & ~WS_EX_TOOLWINDOW
            style = style | WS_EX_APPWINDOW
            res =_winlib.SetWindowLongPtrW(hwnd, GWL_EXSTYLE, style)
        except :
            try :
                style = _winlib.GetWindowLongA(hwnd, GWL_EXSTYLE)
                style = style & ~WS_EX_TOOLWINDOW
                style = style | WS_EX_APPWINDOW
                _winlib.SetWindowLongA(hwnd, GWL_EXSTYLE, style)
            except :
                pass
    def Enter(self,event):
        if self.widget == event.widget or event.widget.winfo_class() =="Canvas":
            formx = self.widget.winfo_x() 
            formy = self.widget.winfo_y() 
            formw = self.widget.winfo_width() 
            formh = self.widget.winfo_height()
            x = event.x_root - formx
            y = event.y_root - formy
    def Motion(self,event):
        if self.widget == event.widget or event.widget.winfo_class() =="Canvas":
            formx = self.widget.winfo_x() 
            formy = self.widget.winfo_y() 
            formw = self.widget.winfo_width() 
            formh = self.widget.winfo_height()
            x = event.x_root - formx
            y = event.y_root - formy
            if ((x >= 0) and (x <= self.bordersize) and (y >= 0) and (y <= self.bordersize)):
                if self.top_drag == None:
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder_TL)
                if self.left_drag == None:
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder_TL)
                self.top_drag.place(x = 0,y = 0,width = formw,height = self.bordersize)
                self.top_drag.configure(bg = self.bordercolor)
                self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = formh)
                self.left_drag.configure(bg = self.bordercolor)
            if ((y >= 0) and (y <= self.bordersize)):
                if self.top_drag == None:
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_V1)
                self.top_drag.bind('<Motion>',self.MotionDragBorder)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder)
                self.top_drag.place(x = 0,y = 0,width = formw,height = self.bordersize)
                self.top_drag.configure(bg = self.bordercolor)
            if ((y >= (formh - self.bordersize)) and (y <= formh)):
                if self.bottom_drag == None:
                    self.bottom_drag = tkinter.Label(self.widget)
                self.bottom_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.bottom_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.bottom_drag.bind('<B1-Motion>',self.MoveDragSize_V2)
                self.bottom_drag.bind('<Motion>',self.MotionDragBorder)
                self.bottom_drag.bind('<Leave>',self.LeaveDragBorder)
                self.bottom_drag.place(x = 0,y = (formh - self.bordersize),width = formw,height = self.bordersize)
                self.bottom_drag.configure(bg = self.bordercolor)
            if ((x >= 0 ) and (x <= self.bordersize)):
                if self.left_drag == None:
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_H1)
                self.left_drag.bind('<Motion>',self.MotionDragBorder)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder)
                self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = formh)
                self.left_drag.configure(bg = self.bordercolor)
            if ((x >= (formw - self.bordersize)) and (x <= formw)):
                if self.right_drag == None:
                    self.right_drag = tkinter.Label(self.widget)
                self.right_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.right_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.right_drag.bind('<B1-Motion>',self.MoveDragSize_H2)
                self.right_drag.bind('<Motion>',self.MotionDragBorder)
                self.right_drag.bind('<Leave>',self.LeaveDragBorder)
                self.right_drag.place(x = (formw - self.bordersize),y = 0,width = self.bordersize,height = formh)
                self.right_drag.configure(bg = self.bordercolor)
    def Leave(self,event):
        if self.widget == event.widget or event.widget.winfo_class() =="Canvas":
            pass
    def StartDrag(self,event):
        self.x = event.x_root
        self.y = event.y_root
    def StopDrag(self,event):
        self.x = None
        self.y = None
        self.widget.configure(cursor='arrow')
    def MoveDragPos(self,event):
        if self.widget == event.widget or event.widget.winfo_class() =="Canvas":
            formx = self.widget.winfo_x() 
            formy = self.widget.winfo_y() 
            formw = self.widget.winfo_width() 
            formh = self.widget.winfo_height()
            x = event.x_root - formx
            y = event.y_root - formy
            if self.x and self.y:
                deltaX = event.x_root - self.x
                deltaY = event.y_root - self.y
                newX = formx + deltaX
                newY = formy + deltaY
                geoinfo = str('%dx%d+%d+%d'%(formw,formh,newX,newY))
                self.widget.geometry(geoinfo)
            self.x = event.x_root
            self.y = event.y_root
    def MoveDragSize_H1(self,event):
        deltaX = event.x_root - self.x
        formx = self.widget.winfo_x() + deltaX
        newW = self.widget.winfo_width() - deltaX
        geoinfo = str('%dx%d+%d+%d'%(newW,self.widget.winfo_height(),formx,self.widget.winfo_y()))
        self.widget.geometry(geoinfo)
        self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = self.widget.winfo_height())
        self.x = event.x_root
        self.widget.configure(cursor='plus')
    def MoveDragSize_H2(self,event):
        deltaX = event.x_root - self.x
        formw = self.widget.winfo_width() 
        formh = self.widget.winfo_height()
        newW = self.widget.winfo_width() + deltaX
        geoinfo = str('%dx%d+%d+%d'%(newW,self.widget.winfo_height(),self.widget.winfo_x(),self.widget.winfo_y()))
        self.widget.geometry(geoinfo)
        self.right_drag.place(x = newW-self.bordersize,y = 0,width = self.bordersize,height = formh)
        self.x = event.x_root
        self.widget.configure(cursor='plus')
    def MoveDragSize_V1(self,event):
        deltaY = event.y_root - self.y
        formy = self.widget.winfo_y() + deltaY
        newH = self.widget.winfo_height() - deltaY
        geoinfo = str('%dx%d+%d+%d'%(self.widget.winfo_width() ,newH,self.widget.winfo_x(),formy))
        self.widget.geometry(geoinfo)
        self.top_drag.place(x = 0,y = 0,width = self.widget.winfo_width(),height = self.bordersize)
        self.y = event.y_root
        self.widget.configure(cursor='plus')
    def MoveDragSize_V2(self,event):
        deltaY = event.y_root - self.y
        newH = self.widget.winfo_height() + deltaY
        geoinfo = str('%dx%d+%d+%d'%(self.widget.winfo_width(),newH,self.widget.winfo_x(),self.widget.winfo_y()))
        self.widget.geometry(geoinfo)
        self.bottom_drag.place(x = 0,y = (newH - self.bordersize),width = self.widget.winfo_width(),height = self.bordersize)
        self.y = event.y_root
        self.widget.configure(cursor='plus')
    def MotionDragBorder(self,event):
        formx = self.widget.winfo_x() 
        formy = self.widget.winfo_y() 
        formw = self.widget.winfo_width() 
        formh = self.widget.winfo_height() 
        x = event.x_root - formx
        y = event.y_root - formy
        if event.widget == self.left_drag:
            if y >=0 and y <= self.bordersize:
                if self.top_drag == None:
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.place(x = 0,y = 0,width = formw,height = self.bordersize)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder_TL)
                if self.left_drag == None:
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder_TL)
            if y >=(formh-self.bordersize) and y <= formh:
                if self.bottom_drag == None:
                    self.bottom_drag = tkinter.Label(self.widget)
                self.bottom_drag.place(x = 0,y = formh-self.bordersize,width = formw,height = self.bordersize)
                self.bottom_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.bottom_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.bottom_drag.bind('<B1-Motion>',self.MoveDragSize_BL)
                self.bottom_drag.bind('<Leave>',self.LeaveDragBorder_BL)
                if self.left_drag == None:
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_BL)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder_BL)
        if event.widget == self.right_drag:
            if y >=0 and y <= self.bordersize:
                if self.top_drag == None:
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.place(x = 0,y = 0,width = formw,height = self.bordersize)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_TR)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder_TR)
                if self.right_drag == None:
                    self.right_drag = tkinter.Label(self.widget)
                self.right_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.right_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.right_drag.bind('<B1-Motion>',self.MoveDragSize_TR)
                self.right_drag.bind('<Leave>',self.LeaveDragBorder_TR)
            if y >=(formh-self.bordersize) and y <= formh:
                if self.bottom_drag == None:
                    self.bottom_drag = tkinter.Label(self.widget)
                self.bottom_drag.place(x = 0,y = formh-self.bordersize,width = formw,height = self.bordersize)
                self.bottom_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.bottom_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.bottom_drag.bind('<B1-Motion>',self.MoveDragSize_BR)
                self.bottom_drag.bind('<Leave>',self.LeaveDragBorder_BR)
                if self.right_drag == None:
                    self.right_drag = tkinter.Label(self.widget)
                self.right_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.right_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.right_drag.bind('<B1-Motion>',self.MoveDragSize_BR)
                self.right_drag.bind('<Leave>',self.LeaveDragBorder_BR)
        if event.widget == self.top_drag:
            if x >=0 and x <= self.bordersize:
                if self.top_drag == None:
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder_TL)
                if self.left_drag == None:
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = formh)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder_TL)
            if x >=(formw-self.bordersize) and x <= formw:
                if self.top_drag == None:
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_TR)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder_TR)
                if self.right_drag == None:
                    self.right_drag = tkinter.Label(self.widget)
                self.right_drag.place(x = formw-self.bordersize,y = 0,width = self.bordersize,height = formh)
                self.right_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.right_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.right_drag.bind('<B1-Motion>',self.MoveDragSize_TR)
                self.right_drag.bind('<Leave>',self.LeaveDragBorder_TR)
        if event.widget == self.bottom_drag:
            if x >=0 and x <= self.bordersize:
                if self.bottom_drag == None:
                    self.bottom_drag = tkinter.Label(self.widget)
                self.bottom_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.bottom_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.bottom_drag.bind('<B1-Motion>',self.MoveDragSize_BL)
                self.bottom_drag.bind('<Leave>',self.LeaveDragBorder_BL)
                if self.left_drag == None:
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = formh)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_BL)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder_BL)
            if x >=(formw-self.bordersize) and x <= formw:
                if self.bottom_drag == None:
                    self.bottom_drag = tkinter.Label(self.widget)
                self.bottom_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.bottom_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.bottom_drag.bind('<B1-Motion>',self.MoveDragSize_BR)
                self.bottom_drag.bind('<Leave>',self.LeaveDragBorder_BR)  
                if self.right_drag == None:
                    self.right_drag = tkinter.Label(self.widget)
                self.right_drag.place(x = formw-self.bordersize,y = 0,width = self.bordersize,height = formh)
                self.right_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.right_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.right_drag.bind('<B1-Motion>',self.MoveDragSize_BR)
                self.right_drag.bind('<Leave>',self.LeaveDragBorder_BR)
    def LeaveDragBorder(self,event):
        event.widget.place_forget()
    def MoveDragSize_TL(self,event):
        deltaX = event.x_root - self.x
        deltaY = event.y_root - self.y
        formx = self.widget.winfo_x() + deltaX
        newW = self.widget.winfo_width() - deltaX
        formy = self.widget.winfo_y() + deltaY
        newH = self.widget.winfo_height() - deltaY
        geoinfo = str('%dx%d+%d+%d'%(newW,newH,formx,formy))
        self.widget.geometry(geoinfo)
        self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = self.widget.winfo_height())
        self.top_drag.place(x = 0,y = 0,width = self.widget.winfo_width(),height = self.bordersize)
        self.x = event.x_root
        self.y = event.y_root
        self.widget.configure(cursor='plus')
    def LeaveDragBorder_TL(self,event):
        self.left_drag.place_forget()
        self.top_drag.place_forget()
        self.widget.configure(cursor='arrow')
    def MoveDragSize_TR(self,event):
        deltaX = event.x_root - self.x
        deltaY = event.y_root - self.y
        formx = self.widget.winfo_x()
        newW = self.widget.winfo_width() + deltaX
        formy = self.widget.winfo_y() + deltaY
        newH = self.widget.winfo_height() - deltaY
        geoinfo = str('%dx%d+%d+%d'%(newW,newH,formx,formy))
        self.widget.geometry(geoinfo)
        self.right_drag.place(x = newW-self.bordersize,y = 0,width = self.bordersize,height = self.widget.winfo_height())
        self.top_drag.place(x = 0,y = 0,width = self.widget.winfo_width(),height = self.bordersize)
        self.x = event.x_root
        self.y = event.y_root
        self.widget.configure(cursor='plus')
    def LeaveDragBorder_TR(self,event):
        self.right_drag.place_forget()
        self.top_drag.place_forget()
        self.widget.configure(cursor='arrow')
    def MoveDragSize_BL(self,event):
        deltaX = event.x_root - self.x
        deltaY = event.y_root - self.y
        formx = self.widget.winfo_x() + deltaX
        newW = self.widget.winfo_width() - deltaX
        formy = self.widget.winfo_y()
        newH = self.widget.winfo_height() + deltaY
        geoinfo = str('%dx%d+%d+%d'%(newW,newH,formx,formy))
        self.widget.geometry(geoinfo)
        self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = self.widget.winfo_height())
        self.bottom_drag.place(x = 0,y = newH-self.bordersize,width = self.widget.winfo_width(),height = self.bordersize)
        self.x = event.x_root
        self.y = event.y_root
        self.widget.configure(cursor='plus')
    def LeaveDragBorder_BL(self,event):
        self.left_drag.place_forget()
        self.bottom_drag.place_forget()
        self.widget.configure(cursor='arrow')
    def MoveDragSize_BR(self,event):
        deltaX = event.x_root - self.x
        deltaY = event.y_root - self.y
        formx = self.widget.winfo_x()
        newW = self.widget.winfo_width() + deltaX
        formy = self.widget.winfo_y()
        newH = self.widget.winfo_height() + deltaY
        geoinfo = str('%dx%d+%d+%d'%(newW,newH,formx,formy))
        self.widget.geometry(geoinfo)
        self.right_drag.place(x = newW-self.bordersize,y = 0,width = self.bordersize,height = self.widget.winfo_height())
        self.bottom_drag.place(x = 0,y = newH-self.bordersize,width = self.widget.winfo_width(),height = self.bordersize)
        self.x = event.x_root
        self.y = event.y_root
        self.widget.configure(cursor='plus')
    def LeaveDragBorder_BR(self,event):
        self.right_drag.place_forget()
        self.bottom_drag.place_forget() 
        self.widget.configure(cursor='arrow')
def PlayAction_MoveTo(uiName,elementName,targetX,targetY,duration = 1.0,fps = 50):
    """控件移动到指定位置"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control is None:
        return
    InitTime = time.time()
    InitX = Control.winfo_x()
    InitY = Control.winfo_y()
    InitW = Control.winfo_width()
    InitH = Control.winfo_height()
    Delay = int(1000 / fps)
    def MovingLoop():
        CurrTime = time.time() - InitTime
        Progress = CurrTime / duration 
        if Progress > 1.0:
            CurrX = targetX
            CurrY = targetY
            Control.place(x=int(CurrX),y=int(CurrY),width=InitW,height=InitH)
        else:
            CurrX = InitX + (targetX - InitX) * Progress 
            CurrY = InitY + (targetY - InitY) * Progress 
            Control.place(x=int(CurrX),y=int(CurrY),width=InitW,height=InitH)
            Control.after(Delay,MovingLoop)
    Control.after(Delay,MovingLoop)
def PlayAction_MoveBy(uiName,elementName,moveX=0,moveY=0,duration = 1.0,fps = 50):
    """控件移动一定距离"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control is None:
        return
    InitTime = time.time()
    InitX = Control.winfo_x()
    InitY = Control.winfo_y()
    InitW = Control.winfo_width()
    InitH = Control.winfo_height()
    targetX = InitX + moveX
    targetY = InitY + moveY
    Delay = int(1000 / fps)
    def MovingLoop():
        CurrTime = time.time() - InitTime
        Progress = CurrTime / duration 
        if Progress > 1.0:
            CurrX = targetX
            CurrY = targetY
            Control.place(x=int(CurrX),y=int(CurrY),width=InitW,height=InitH)
        else:
            CurrX = InitX + (targetX - InitX) * Progress 
            CurrY = InitY + (targetY - InitY) * Progress 
            Control.place(x=int(CurrX),y=int(CurrY),width=InitW,height=InitH)
            Control.after(Delay,MovingLoop)
    Control.after(Delay,MovingLoop)
def PlayAction_ScaleTo(uiName,elementName,anchor = "center",scaleW=1.0,scaleH=1.0,duration = 1.0,fps = 50):
    """控件缩放到指定大小"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control is None:
        return
    InitTime = time.time()
    InitX = Control.winfo_x()
    InitY = Control.winfo_y()
    InitW = Control.winfo_width()
    InitH = Control.winfo_height()
    CenterX = InitX + InitW * 0.5
    CenterY = InitY + InitH * 0.5
    targetW = InitW * scaleW
    targetH = InitH * scaleH
    if anchor == "nw":
        targetX = InitX
        targetY = InitY
    elif anchor == "n":
        targetX = int(CenterX-targetW * 0.5)
        targetY = InitY
    elif anchor == "ne":
        targetX = InitX + InitW - targetW
        targetY = InitY
    elif anchor == "w":
        targetX = InitX
        targetY = int(CenterY-targetH * 0.5)
    elif anchor == "e":
        targetX = InitX + InitW - targetW
        targetY = int(CenterY-targetH * 0.5)
    elif anchor == "sw":
        targetX = InitX
        targetY = InitY + InitH - targetH
    elif anchor == "s":
        targetX = int(CenterX-targetW * 0.5)
        targetY = InitY + InitH - targetH
    elif anchor == "se":
        targetX = InitX + InitW - targetW
        targetY = InitY + InitH - targetH
    else:
        targetX = int(CenterX - targetW*0.5)
        targetY = int(CenterY - targetH*0.5)
    Delay = int(1000 / fps)
    def ScalingLoop():
        CurrTime = time.time() - InitTime
        Progress = CurrTime / duration 
        if Progress > 1.0:
            Control.place(x=targetX,y=targetY,width=targetW,height=targetH)
        else:
            CurrX = InitX + (targetX - InitX) * Progress 
            CurrY = InitY + (targetY - InitY) * Progress 
            CurrW = InitW + (targetW - InitW) * Progress 
            CurrH = InitH + (targetH - InitH) * Progress 
            Control.place(x=int(CurrX),y=int(CurrY),width=CurrW,height=CurrH)
            Control.after(Delay,ScalingLoop)
    Control.after(Delay,ScalingLoop)
def SetRootRoundRectangle(canvas,x1, y1, x2, y2, radius=25,**kwargs):
    """使用TKinter方式设置窗口圆角, 支持跨平台。参数1:Canvas控件,参数2:左上x位置,参数3:左上y位置,参数4 :右下x位置,参数5:右下y位置,参数6:圆角半径。"""
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
    return canvas.create_polygon(points, smooth=True, **kwargs)
def ReadFromFile(filePath,encoding='utf-8',autoEval=False):
    """从一个文件中读取内容。参数1 :文件路径 。"""
    content = None
    if filePath != None:
        if os.path.exists(filePath) == True: 
            f = open(filePath,mode='r',encoding=encoding)
            if f != None:
                content = f.read()
                if autoEval == True:
                    content = eval(content)
                f.close()
    return content
def OpenFile(title="Open Python File",filetypes=[('Python File','*.py'),('All files','*')],initDir = ''):
    """调用打开文件框"""
    import tkinter.filedialog
    openPath = tkinter.filedialog.askopenfilename(initialdir=initDir,title=title,filetypes=filetypes)
    return openPath
def WriteToFile(filePath,content,encoding='utf-8'):
    """将内容写入到一个文件中。参数1 :文件路径,参数2 :写入的内容 。 """
    if filePath != None:
        f = open(filePath,mode='w',encoding=encoding)
        if f != None:
            if content != None:
                f.write(str(content))
            f.close()
            return True
    return False
def SaveFile(title="Save Python File",filetypes=[('Python File','*.py'),('All files','*')],initDir = '',defaultextension='py'):
    """调用保存文件框"""
    import tkinter.filedialog
    savePath = tkinter.filedialog.asksaveasfilename(initialdir=initDir,title=title,filetypes=filetypes,defaultextension=defaultextension)
    return savePath
def ReadStyleFile(filePath):
    """读取样式定义文件,返回样式列表。参数1 :文件路径 。"""
    global G_ExeDir
    StyleArray = {}
    if len(filePath)==0 :
        return StyleArray
    if os.path.exists(filePath) == False:
        PathName, FileName = os.path.split(filePath)
        filePath = os.path.join(G_ExeDir,FileName)
        if os.path.exists(filePath) == False:
            return StyleArray
    f = open(filePath,encoding='utf-8')
    line =""
    while True:
        line = f.readline()
        if not line:
            break
        text = line.strip()
        if not text:
            continue
        if text.find('style = tkinter.ttk.Style()') >= 0:
            continue
        if text.find('style.configure(') >= 0:
            splitarray1 = text.partition('style.configure(')
            stylename = None
            splitarray2 = None
            if splitarray1[2].find(',') >= 0:
                splitarray2 = splitarray1[2].partition(',')
                stylename = splitarray2[0].replace('"','')
            else:
                splitarray2 = splitarray1[2].partition(')')
                stylename = splitarray2[0].replace('"','')
            sytleValueText = splitarray2[2]
            fontindex_begin = sytleValueText.find('font=(')
            fontindex_end = fontindex_begin
            StyleArray[stylename] = {}
            othertext = sytleValueText
            if fontindex_begin >= 0:
                fontindex_end = sytleValueText.find(')')
                fonttext = sytleValueText[fontindex_begin+6:fontindex_end]
                fontsplitarray = fonttext.split(',')
                StyleArray[stylename]['font'] = tkinter.font.Font(family=fontsplitarray[0].replace('"','').strip(), size=int(fontsplitarray[1].replace('"','').strip()),weight=fontsplitarray[2].replace('"','').strip())
                othertext = sytleValueText[0:fontindex_begin] + sytleValueText[fontindex_end+1:-1]
            else:
                splitarray4 = sytleValueText.partition(')')
                othertext = splitarray4[0]
            splitarray3 = othertext.split(',')
            for stylecfgtext in splitarray3:
                if stylecfgtext.find('=') > 0:
                    splitarray4 = stylecfgtext.partition('=')
                    key = splitarray4[0].replace('"','').strip()
                    value = splitarray4[2].replace('"','').strip()
                    StyleArray[stylename][key] = value
            continue
        if text.find('style.map(') >= 0:
            continue
    f.close()
    return StyleArray 
ResourFileList = WalkAllResFiles(G_ResDir,True)
for FilePath in ResourFileList:
    PathName, FileName = os.path.split(FilePath)
    G_ResourcesFileList[FileName] = FilePath
    shotname, extension = os.path.splitext(FileName)
    extension_lower = extension.lower()
    if extension_lower == ".ttf" or extension_lower == ".otf":
        TTFFontPath = FilePath
        TTFFontPathBuf = create_unicode_buffer(TTFFontPath)
        AddFontResourceEx = windll.gdi32.AddFontResourceExW
        numFontsAdded = AddFontResourceEx(byref(TTFFontPathBuf), 0, 0)
def GetResourcePath(FileName):
    """查询一个资源文件的路径"""
    global G_ResourcesFileList
    if FileName in G_ResourcesFileList:
        return G_ResourcesFileList[FileName]
    return None
#下载进度对话框
class   DownLoadFileProgressDialog:
    def __init__(self,uiName,showDialog = True,title='正在下载文件',bgColor='#EFEFEF',fgColor='#000000'):
        self.FinishFlag = False
        self.LocalSaveFile = ""
        self.showDialog = showDialog
        if self.showDialog == True:
            self.root = GetElement(uiName,"root")
            self.Dialog = tkinter.Toplevel()
            self.Dialog.attributes("-toolwindow", 1)
            self.Dialog.resizable(0,0) 
            self.Dialog.wm_attributes("-topmost", 1)
            self.Title = title
            self.bgColor = bgColor
            self.fgColor = fgColor
            self.Dialog.title(self.Title)
            self.Form = tkinter.Canvas(self.Dialog,width = 280,height=140,bg = bgColor)
            self.Form.place(x=0, y=0,width=280,height=140)
            self.ShowDownLoadProgressDialog()
    #取得当前窗口句柄
    def GetWindHandle(self):
        _handle = None
        if self.showDialog == True:
            import win32gui
            _handle = win32gui.FindWindow(None,self.Title)
        return _handle
    def downloadFileFromURL(self,url,saveToDir=None,ReDownLoadIfExist = True,autoExtractZip = False,progressCallBack = None,finishCallBack = None,errorCallBack = None):
        """多线程下载单文件,url为远端文件网址,saveToDir为本地保存位置,None指项目所在目录,ReDownLoadIfExist为如果存在是否重新下载，progressCallBack进度函数:参数1：本地文件，参数2:进度值,finishCallBack完成函数，参数1：本地文件,errorCallBack错误函数，参数1：网址或本地文件，参数2：错误原因:1:文件下载失败 2:本地解压失败"""
        global G_ResDir
        self.URLFile = url
        self.LocalDir = saveToDir
        self.autoExtractZip = autoExtractZip
        self.progressCallBack = progressCallBack
        self.errorCallBack = errorCallBack
        self.finishCallBack = finishCallBack
        projpath, resdirname = os.path.split(G_ResDir)
        _handle = self.GetWindHandle()
        WebSite, FileName = os.path.split(self.URLFile)
        if self.LocalDir:
            self.LocalSaveFile = os.path.join(self.LocalDir,FileName)
        else:
            self.LocalSaveFile = os.path.join(projpath,FileName)
        IsZipFile = False
        if FileName.find(".zip") > 0 :
            IsZipFile = True
        if os.path.exists(self.LocalSaveFile) == True:
            if ReDownLoadIfExist == True:
                os.remove(self.LocalSaveFile)
            else:
                if IsZipFile == True and self.autoExtractZip == True:
                    if self.LocalDir:
                        LocalDir, LocalFile = os.path.split(self.LocalDir)
                        self.extractZipFile(self.LocalSaveFile,LocalDir)
                    else:
                        self.extractZipFile(self.LocalSaveFile,projpath)
                return 
        try:
            resp = requests.get(self.URLFile,stream=True)
            total_length = int(resp.headers.get('content-length',0))
            def handle_ThreadDownload(theResp,theTotallength):
                if resp.status_code == 404:
                    if self.showDialog == True:
                        MessageBox("文件异常,无法下载.",_handle)
                    if self.errorCallBack:
                        self.errorCallBack(self.URLFile,1)
                    self.cancle()
                else:
                    step = int(theTotallength / 100)
                    if step < 320:
                        step = 320
                    maximum = int (theTotallength/step)
                    if maximum == 0:
                        maximum = 1
                    if self.showDialog == True:
                        self.ProgressBar['maximum'] = maximum
                    self.FinishFlag = False
                    if os.path.exists(self.LocalSaveFile) == False:
                        with open(self.LocalSaveFile, 'wb') as f:
                            progress = 0
                            for i in theResp.iter_content(chunk_size=step):  
                                f.write(i)
                                progress = progress + 1
                                if progress <= maximum:
                                    if self.showDialog == True:
                                        self.ProgressBar['value'] = progress
                                        self.TitleLabel.configure(text="正在下载压缩包" + str("(%d%%)"%progress))
                                    if self.progressCallBack:
                                        self.progressCallBack(self.LocalSaveFile,progress)
                        #下载完毕后解压，并删除ZIP文件
                        if IsZipFile == True and self.autoExtractZip == True:
                            if self.showDialog == True:
                                self.TitleLabel.configure(text="下载完成,准备解压缩文件")
                            if self.LocalDir:
                                self.extractZipFile(self.LocalSaveFile,self.LocalDir)
                            else:
                                self.extractZipFile(self.LocalSaveFile,projpath)
                        else:
                            self.FinishFlag = True 
                            if self.showDialog == True:
                                self.TitleLabel.configure(text="下载完成")
                                self.OKButton.configure(text="确定")
                            if self.finishCallBack:
                                self.finishCallBack(self.LocalSaveFile)
            self.run_thread_download = threading.Thread(target=handle_ThreadDownload, args=[resp,total_length])
            self.run_thread_download.Daemon = True
            self.run_thread_download.start() 
        except Exception as Ex:
            if self.errorCallBack:
                self.errorCallBack(self.URLFile,1)
            if self.showDialog == True:
                MessageBox(str(Ex),_handle)
    def downloadFilesFromURLList(self,urllist,saveToDir,ReDownLoadIfExist = True,progressCallBack = None,finishCallBack = None,errorCallBack = None):
        """多线程下载多文件,urllist为远端文件网址列表,saveToDir为本地保存位置,None指项目所在目录,ReDownLoadIfExist为如果存在是否重新下载，progressCallBack进度函数:参数1：本地文件，参数2:进度值,finishCallBack完成函数，参数1：本地文件,errorCallBack错误函数，参数1：网址或本地文件，参数2：错误原因:1:文件下载失败 2:本地解压失败"""
        global G_ResDir
        self.URLFileList = urllist
        self.URLFile = ""
        self.LocalDir = saveToDir
        self.progressCallBack = progressCallBack
        self.errorCallBack = errorCallBack
        self.finishCallBack = finishCallBack
        self.FinishFlag = False
        projpath, resdirname = os.path.split(G_ResDir)
        _handle = self.GetWindHandle()
        if self.showDialog == True:
            self.ProgressBar['maximum'] = len(urllist)
        try:
            def handle_ThreadDownloadFiles():
                progress = 0
                for url in self.URLFileList:
                    self.URLFile = url
                    resp = requests.get(self.URLFile,stream=True)
                    total_length = int(resp.headers.get('content-length',0))
                    if resp.status_code == 404:
                        if self.showDialog == True:
                            MessageBox(self.URLFile+"文件异常,无法下载.",_handle)
                        if self.errorCallBack:
                            self.errorCallBack(self.URLFile,1)
                    else:
                        WebSite, FileName = os.path.split(self.URLFile)
                        if self.LocalDir:
                            self.LocalSaveFile = os.path.join(self.LocalDir,FileName)
                        else:
                            self.LocalSaveFile = os.path.join(projpath,FileName)
                        if os.path.exists(self.LocalSaveFile) == True:
                            if ReDownLoadIfExist == True:
                                 os.remove(self.LocalSaveFile)
                        if os.path.exists(self.LocalSaveFile) == False:
                            step = 1024
                            with open(self.LocalSaveFile, 'wb') as f:
                                for i in resp.iter_content(chunk_size=step):
                                    f.write(i)
                        progress = progress + 1
                        if self.showDialog == True:
                            self.ProgressBar['value'] = progress
                            self.TitleLabel.configure(text="正在下载文件" + str("(%d%%)"%progress))
                        if self.progressCallBack:
                            self.progressCallBack(self.LocalSaveFile,progress)
                self.FinishFlag = True 
                if self.showDialog == True:
                    self.TitleLabel.configure(text="下载完成")
                    self.OKButton.configure(text="确定")
                if self.finishCallBack:
                    self.finishCallBack(self.LocalSaveFile)
            self.run_thread_download = threading.Thread(target=handle_ThreadDownloadFiles, args=[])
            self.run_thread_download.Daemon = True
            self.run_thread_download.start() 
        except Exception as Ex:
            if self.errorCallBack:
                self.errorCallBack(self.URLFile,1)
            if self.showDialog == True:
                MessageBox(str(Ex),_handle)
    #解压
    def extractZipFile(self,ZipFile,ExtractDir):
        _handle = self.GetWindHandle()
        try:
            block_size = 8192
            z = zipfile.ZipFile(ZipFile)
            namecount = len(z.namelist())
            if self.showDialog == True:
                self.ProgressBar['maximum'] = namecount
            nameindex = 0
            for file_name in z.namelist():
                file_name_utf8 = file_name.encode('cp437').decode('gbk') 
                progress = int(nameindex / namecount * 100)
                if self.showDialog == True:
                    self.TitleLabel.configure(text="正在解压缩文件" + str("(%d%%)"%progress))
                entry_info = z.getinfo(file_name)
                i = z.open(file_name)
                print(file_name)
                if file_name[-1] != '/':
                    o = open(f"{ExtractDir}/{file_name_utf8}", "wb")
                    offset = 0
                    while True:
                        b = i.read(block_size)
                        offset += len(b)
                        if b == b'':
                            break
                        o.write(b)
                    o.close()
                else:
                    dir_name = os.path.dirname(file_name_utf8)
                    p = Path(f"{ExtractDir}/{dir_name}")
                    p.mkdir(parents=True, exist_ok=True)
                i.close()
                nameindex = nameindex + 1
                if self.showDialog == True:
                    self.ProgressBar['value'] = nameindex
            z.close()
            if self.autoExtractZip == True:
                os.remove(ZipFile)
            self.FinishFlag = True  
            if self.showDialog == True:
                self.TitleLabel.configure(text="完成解压缩")
                self.OKButton.configure(text="确定")
            if self.finishCallBack:
                self.finishCallBack(ExtractDir)
            return True
        except Exception as Ex:
            try:
                zip_1 = zipfile.ZipFile(ZipFile,'r')
                zip_1.extractall(path=ExtractDir)
                zip_1.close()
                os.remove(ZipFile)
                self.FinishFlag = True  
                if self.showDialog == True:
                    self.TitleLabel.configure(text="完成解压缩")
                    self.OKButton.configure(text="确定")
                if self.finishCallBack:
                    self.finishCallBack(ExtractDir)
                return True
            except Exception as Ex:
                if self.showDialog == True:
                    MessageBox(str(Ex),_handle)
                if self.errorCallBack:
                    self.errorCallBack(self.LocalSaveFile,2)
                return False
    #确定TitleLabel
    def submit(self):
        if self.showDialog == True:
            _handle = self.GetWindHandle()
            if self.FinishFlag == False:
                if  AskBox("正在下载，确定退出？",_handle) == False:
                    return 
                if self.LocalSaveFile:
                    if os.path.exists(self.LocalSaveFile) == True:
                        os.remove(self.LocalSaveFile)
            self.Dialog.destroy()
    #取消
    def cancle(self):
        if self.showDialog == True:
            self.Dialog.destroy()
    #显示设置列表
    def ShowDownLoadProgressDialog(self):
        if self.showDialog == True:
            self.TitleFont =tkinter.font.Font(family="Arial", size=10,weight='normal',slant='roman',underline=0,overstrike=0)
            self.TitleLabel = tkinter.Label(self.Form,anchor = tkinter.W,bg=self.bgColor,fg=self.fgColor,font = self.TitleFont,text=self.Title,width = 100,height = 1)
            self.TitleLabel.place(x = 10,y = 10,width = 260,height = 24)
            self.ProgressBar = tkinter.ttk.Progressbar(self.Form, length=200, mode='determinate',style="TProgressbar", orient=tkinter.HORIZONTAL)
            self.ProgressBar.place(x=10,y=40,width=260,height=15)
            self.ProgressBar['maximum'] = 100
            self.ProgressBar['value'] = 0
            self.OKButton = tkinter.Button(self.Form,anchor = tkinter.CENTER,text="取消",width = 100,height = 1,bg=self.bgColor,fg=self.fgColor,command=self.submit)
            self.OKButton.place(x = 180,y = 70,width = 80,height = 24) 
            #居中显示
            sx = self.root.winfo_x()
            sy = self.root.winfo_y()
            sw = self.root.winfo_width()
            sh = self.root.winfo_height()
            nx = sx + (sw - 280)/2
            ny = sy + (sh - 110)/2
            geoinfo = str('%dx%d+%d+%d'%(280,110,nx,ny))
            self.Dialog.geometry(geoinfo)   
