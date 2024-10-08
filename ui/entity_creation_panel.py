import bpy
from bpy.types import Panel
from bpy.props import EnumProperty, StringProperty

from ..utils import entities

ALLOWED_SHAPE_TYPES = [
    'box',
    'sphere',
    'isosahedron',
    'hexagon',
    'octagon',
    'cylinder',
    'cone',
    'circle',
    'quad',
]

BLENDER_PRIMITIVES = [
    ('PLANE', 'Plane', ''),
    ('CUBE', 'Cube', ''),
    ('CIRCLE', 'Circle', ''),
    ('UVSPHERE', 'UV Sphere', ''),
    ('ICOSPHERE', 'Ico Sphere', ''),
    ('CYLINDER', 'Cylinder', ''),
    ('CONE', 'Cone', ''),
    ('TORUS', 'Torus', ''),
    ('MONKEY', 'Monkey', ''),
]

class VIRCADIA_PT_entity_creation(Panel):
    bl_label = "Create Vircadia Entity"
    bl_idname = "VIEW3D_PT_vircadia_entity_creation"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Vircadia"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 3

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.prop(scene, "vircadia_entity_type")

        if scene.vircadia_entity_type == 'shape':
            layout.prop(scene, "vircadia_shape_type")
        elif scene.vircadia_entity_type == 'model':
            layout.prop(scene, "vircadia_primitive_type")
        elif scene.vircadia_entity_type == 'zone':
            box = layout.box()
            box.label(text="Skybox Texture:")
            box.prop(scene, "vircadia_skybox_texture", text="")
            
            box.label(text="Environment Texture:")
            box.prop(scene, "vircadia_environment_texture", text="")

        layout.operator("vircadia.create_entity")

def get_entity_types(self, context):
    return [(t, t.capitalize(), "", i) for i, t in enumerate(entities.ENTITY_TYPES)]

def get_shape_types(self, context):
    return [(t, t.capitalize(), "", i) for i, t in enumerate(ALLOWED_SHAPE_TYPES)]

def register():
    bpy.types.Scene.vircadia_entity_type = EnumProperty(
        name="Entity Type",
        items=get_entity_types,
        default=0  # Set default to 0 (first item in the list)
    )

    bpy.types.Scene.vircadia_shape_type = EnumProperty(
        name="Shape Type",
        items=get_shape_types,
        default=0  # Index of 'box' in ALLOWED_SHAPE_TYPES
    )

    bpy.types.Scene.vircadia_primitive_type = EnumProperty(
        name="Primitive Type",
        items=BLENDER_PRIMITIVES,
        default='CUBE'
    )

    bpy.types.Scene.vircadia_skybox_texture = StringProperty(
        name="Skybox Texture",
        default="",
        subtype='FILE_PATH'
    )

    bpy.types.Scene.vircadia_environment_texture = StringProperty(
        name="Environment Texture",
        default="",
        subtype='FILE_PATH'
    )

    bpy.utils.register_class(VIRCADIA_PT_entity_creation)

def unregister():
    bpy.utils.unregister_class(VIRCADIA_PT_entity_creation)

    del bpy.types.Scene.vircadia_primitive_type
    del bpy.types.Scene.vircadia_shape_type
    del bpy.types.Scene.vircadia_entity_type
    del bpy.types.Scene.vircadia_skybox_texture
    del bpy.types.Scene.vircadia_environment_texture

if __name__ == "__main__":
    register()