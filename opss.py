import bpy

        
class ss_unwrap(bpy.types.Operator):
    bl_idname = "ss_unwrap.button"
    bl_label = "Testop"
    bl_description = ""
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        context = bpy.context
        #obj = context.object
        sel = context.selected_objects
        set = scn.icap
        icap = set.com
        icap = icap.lower()
        ran = set.ran
        
        
        for obj in sel:
            
            bpy.context.scene.objects.active = obj
            bpy.ops.object.mode_set(mode = 'EDIT')

            if bpy.context.object.data.uv_layers:
                print("We have UV's")
            else:
                
                bpy.ops.uv.smart_project()
                
                
                
                pass
        
        

        return {"FINISHED"}
    

    
    
