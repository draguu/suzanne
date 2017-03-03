'''
Copyright (C) 2017 YOUR NAME
YOUR@MAIL.com

Created by YOUR NAME

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
    "name": "Suzzane",
    "description": "",
    "author": "Pratik Solanki",
    "version": (1,2),
    "blender": (2, 78, 0),
    "location": "View3D",
    "warning": "This addon is still in development.",
    "wiki_url": "",
    "category": "Object" }


import bpy
from bpy.props import (StringProperty,
                              BoolProperty,
                              IntProperty,
                              FloatProperty,
                              FloatVectorProperty,
                              EnumProperty,
                              PointerProperty,
                              )
from bpy.types import (Panel,
                              Operator,
                              AddonPreferences,
                              PropertyGroup,
                              )

import random
from . import addon_updater_ops



# load and reload submodules
##################################

import importlib
from . import opss
from . import developer_utils
from . import msgs
importlib.reload(developer_utils)
modules = developer_utils.setup_addon_modules(__path__, __name__, "bpy" in locals())


class icap(PropertyGroup):
    def testupdate(self, context):
        if self.com != None:
            ran = random.randrange(10)
            self.ran = (int(ran))
            
            
        
        if self.com =='morning':
            bpy.ops.morning.button()
            
            
        if self.com =='afternoon':
            bpy.ops.afternoon.button()
            
        if self.com =='night':
            bpy.ops.night.button()
            
        if self.com =='evening':
            bpy.ops.evening.button()
            
        if self.com =='automirror':
            bpy.ops.object.automirror()
        if 'uv' in self.com or 'unwrap' in self.com:
            bpy.ops.ss_unwrap.button()
            
            
            
            
            
            
            
            
        
        
        
            
            
       
            
                
        else:
            bpy.context.report({'INFO'}, "sucker")
            pass

       
            
        return None
    

    com = bpy.props.StringProperty(name = '',update = testupdate)
    ran = bpy.props.IntProperty(name = '')
    
def checkmsg(self, context):
    return msgs.process_messages(self, context)    
class test(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Suzanne"
    bl_category = "Assist"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    

    def draw(self, context):
        
        
       
        
        scn = bpy.context.scene
        set = scn.icap
        layout = self.layout
        layout.label('Suzanne', icon='KEYTYPE_EXTREME_VEC')
        row = layout.row(align = True)
        row.prop(set,'com')
        row = layout.row(align = True)
        
        row.label(checkmsg(self, context))

class su_prefrences(bpy.types.AddonPreferences):
    bl_idname = __package__
    # addon updater preferences from `__init__`, be sure to copy all of them
    auto_check_update = bpy.props.BoolProperty(
    name = "Auto-check for Update",
    description = "If enabled, auto-check for updates using an interval",
    default = False,
    )
    updater_intrval_months = bpy.props.IntProperty(
    name='Months',
    description = "Number of months between checking for updates",
    default=0,
    min=0
    )
    updater_intrval_days = bpy.props.IntProperty(
    name='Days',
    description = "Number of days between checking for updates",
    default=7,
    min=0,
    )
    updater_intrval_hours = bpy.props.IntProperty(
    name='Hours',
    description = "Number of hours between checking for updates",
    default=0,
    min=0,
    max=23
    )
    updater_intrval_minutes = bpy.props.IntProperty(
    name='Minutes',
    description = "Number of minutes between checking for updates",
    default=0,
    min=0,
    max=59
    )

    def draw(self, context):
        layout = self.layout
        
        addon_updater_ops.update_settings_ui(self,context)
        
        



# register
##################################

import traceback






def register():
    addon_updater_ops.register(bl_info)
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()
    

    print("Registered {} with {} modules".format(bl_info["name"], len(modules)))
    bpy.types.Scene.icap = PointerProperty(type=icap)

def unregister():
    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
    del bpy.types.Scene.icap

    print("Unregistered {}".format(bl_info["name"]))
