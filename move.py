import os

if __name__ == '__main__':
    
    pathTest = "./assets/vrac"
    PathLego = "./assets/Lego"

    # List all directories in PathLego
    dirInLego = os.listdir(PathLego)

    for dir in dirInLego:
        dirPath = os.path.join(PathLego, dir)
        # Check if the directory is empty
        if os.path.isdir(dirPath) and not os.listdir(dirPath):
            os.rmdir(dirPath)

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

#TODO: Add a progrramm to convert fbx file to fbx file with blender and do the tumnail to the file