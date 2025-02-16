import bpy
import os

# Sélectionner tous les objets de type 'MESH'
bpy.ops.object.select_by_type(type='MESH')

# Joindre tous les objets sélectionnés
bpy.ops.object.join()

# Définir l'origine sur le curseur 3D
bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')

# Récupérer l'objet vide (Empty) à la racine de tous les objets
root_empty = None
for obj in bpy.context.scene.objects:
    if obj.type == 'EMPTY' and obj.parent is None:
        root_empty = obj
        break

# Modifier la couleur du matériau de l'objet mesh sélectionné
selected_object = bpy.context.view_layer.objects.active
if selected_object and selected_object.type == 'MESH':
    if selected_object.material_slots:
        material = selected_object.material_slots[0].material
        if material and material.node_tree:
            material.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (1, 1, 1, 1)
            
bpy.ops.object.light_add(type='SUN', radius=1, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))


# Ajouter une caméra
bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0.6, -0.65, 2), rotation=(0.389654, 0.00552858, 0.715481), scale=(1, 1, 1))
camera = bpy.context.object

# Définir la caméra ajoutée comme caméra active
bpy.context.scene.camera = camera

# Afficher le nom de l'objet vide (Empty) à la racine
if root_empty is not None:
    print(f"Nom de l'objet vide à la racine : {root_empty.name}")
    
    # Créer un dossier avec le nom de l'objet vide (Empty) à la racine
    pathTest = rf"C:\Users\Nathan MOREL\Documents\BLRAmenagement\assets\Lego\{root_empty.name}"
    try:
        if not os.path.exists(pathTest):
            os.makedirs(pathTest)
        print(f"Dossier créé : {pathTest}")
        
        name = root_empty.name
        
        # Enregistrer le fichier Blender actuel dans ce dossier
        save_path = os.path.join(pathTest, name + ".blend")
        bpy.ops.wm.save_as_mainfile(filepath=save_path)
        print(f"Fichier enregistré sous : {save_path}")
        
        # Exporter le fichier en FBX dans ce dossier
        export_path = os.path.join(pathTest, name + "_blend.fbx")
        bpy.ops.export_scene.fbx(filepath=export_path)
        print(f"Fichier exporté en FBX sous : {export_path}")
        
        # Lancer le rendu et enregistrer l'image dans ce dossier
        bpy.ops.render.render(write_still=True)
        render_path = os.path.join(pathTest, name + "_thumbnail.png")
        bpy.data.images['Render Result'].save_render(filepath=render_path)
        print(f"Rendu enregistré sous : {render_path}")
        
    except PermissionError as e:
        print(f"PermissionError: {e}")
else:
    print("Aucun objet vide à la racine trouvé.")