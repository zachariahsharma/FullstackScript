#Author-
#Description-
import adsk.core, adsk.fusion, adsk.cam, traceback

def NewNCProgram():
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct

        # Ensure we are in the CAM workspace
        cam = adsk.cam.CAM.cast(design)
        if not cam:
            ui.messageBox("Switch to the CAM workspace.")
            return
        # Get all setups
        allSetups = cam.setups
        folderDlg = ui.createFolderDialog()
        folderDlg.title = "Select a folder"
        dialogResult = folderDlg.showDialog()
        if dialogResult == adsk.core.DialogResults.DialogOK:
            folder_path = folderDlg.folder

        for setup in allSetups:
            releventToolpaths = {"Drills": [], 'Profiles': adsk.core.ObjectCollection.create()}
            for toolpath in setup.operations:
                if toolpath.strategy == 'drill':
                    releventToolpaths['Drills'].append(toolpath)
                else:
                    releventToolpaths['Profiles'].add(toolpath)
            for toolpath in releventToolpaths['Drills']:
                postProcessInput = adsk.cam.PostProcessInput.create(setup.name[0] + str(toolpath.name).split(' ')[0], '/Users/zachsharma/Downloads/Laguna.cps', folder_path, adsk.cam.PostOutputUnitOptions.MillimetersOutput)
                postProcessInput.isOpenInEditor = False
                cam.postProcess(toolpath, postProcessInput)
            postProcessInput = adsk.cam.PostProcessInput.create(setup.name[0] + "Profile", '/Users/zachsharma/Downloads/Laguna.cps', folder_path, adsk.cam.PostOutputUnitOptions.MillimetersOutput)
            postProcessInput.isOpenInEditor = False
            cam.postProcess(releventToolpaths['Profiles'], postProcessInput)
        ui.messageBox('Done')
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
