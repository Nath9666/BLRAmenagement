import os
import shutil

if __name__ == '__main__':
    
    pathTest = "./assets/vrac"
    if not os.path.exists(pathTest):
        os.makedirs(pathTest)

    PathLego = "./assets/Lego"

    other = ['15573.fbx', '22885.fbx', '24246.fbx', '2431.fbx', '26603.fbx', '3003.fbx', '3004.fbx', '3005.fbx', '3010.fbx', '3020.fbx', '3021.fbx', '3022.fbx', '3023.fbx', '3024.fbx', '3031.fbx', '3032.fbx', '30414.fbx', '3068b.fbx', '3069b.fbx', '3070b.fbx', '32028.fbx', '3710.fbx', '3937.fbx', '4032a.fbx', '41588-1 - 98138pz0.fbx', '41589 - 2.fbx', '41590 - 2.fbx', '50746.fbx', '55707c.fbx', '6005.fbx', '63868.fbx', '85984.fbx', '87079.fbx', '92593.fbx', '99206.fbx', '99780.fbx', '99781.fbx']

    # Extract the base names without extension
    other_basenames = [os.path.splitext(f)[0] for f in other]

    # List all directories in PathLego
    dirInLego = os.listdir(PathLego)

    for dir in dirInLego:
        dirPath = os.path.join(PathLego, dir)
        # Check if the directory is in the list 'other'
        if dir in other_basenames:
            print("The directory is in other", dir)
            shutil.rmtree(dirPath)

    # List all files in the directory
    files = os.listdir(pathTest)
    print(files)

    for file in files:
        tempFile = file
        pathTempFile = os.path.join(pathTest, tempFile)
        pathFinalTempFile = os.path.join(PathLego, tempFile.split(".")[0])

        if not os.path.exists(pathFinalTempFile):
            os.makedirs(pathFinalTempFile)
            os.rename(pathTempFile, os.path.join(pathFinalTempFile, tempFile))
        else:
            print("The directory already exists", pathFinalTempFile)

    os.mkdir(pathTest)

#TODO: Add a program to convert fbx file to fbx file with blender and do the thumbnail to the file