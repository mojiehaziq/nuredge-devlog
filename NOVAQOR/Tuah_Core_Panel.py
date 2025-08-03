bl_info = {
    "name": "Tuah Core Panel",
    "author": "NurEdge DevLog",
    "version": (1, 0),
    "blender": (4, 5, 0),
    "location": "View3D > Sidebar > Tuah Tab",
    "description": "Panel kawalan Tuah Core di Blender",
    "category": "3D View"
}

import bpy

# Panel Class
class TUAH_PT_CorePanel(bpy.types.Panel):
    bl_label = "Tuah Core Control"
    bl_idname = "TUAH_PT_core_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tuah"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Tuah Core Panel Active")
        layout.operator("tuah.test_operator")

# Operator Test
class TUAH_OT_TestOperator(bpy.types.Operator):
    bl_idname = "tuah.test_operator"
    bl_label = "Test Tuah Action"

    def execute(self, context):
        self.report({'INFO'}, "Tuah Core Activated!")
        return {'FINISHED'}

# Register
classes = (TUAH_PT_CorePanel, TUAH_OT_TestOperator)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
