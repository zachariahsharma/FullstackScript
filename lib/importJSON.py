# Created by Portland CNC
# URL: https://pdxcnc.com

import adsk.core, adsk.fusion, traceback
import os
import json

def importJSON():
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct
        rootComp = design.rootComponent

        # Counters for imported files and a list for failed imports by name
        success_count = 0
        fail_count = 0
        failed_files = []

        # Create a file dialog to select STEP, IGS files
        fileDialog = ui.createFileDialog()
        fileDialog.title = 'Select JSON Config'
        fileDialog.filter = 'JSON Files (*.json)'
        fileDialog.filterIndex = 0
        fileDialog.isMultiSelectEnabled = False
        dialogResult = fileDialog.showOpen()
        if dialogResult == adsk.core.DialogResults.DialogOK:
            filenames = fileDialog.filenames
            for filename in filenames:
                try:
                    with open(filename, 'r') as file:
                        # Read the JSON file
                        json_data = json.load(file)
                        ui.messageBox(f'JSON data imported successfully from {str(json_data)}')
                        return json_data
                    success_count += 1

                except Exception as e:
                    # Increment fail count for this file and add its base name to the failed_files list
                    fail_count += 1
                    failed_files.append(os.path.basename(filename))
                    print(f'Error importing {os.path.basename(filename)}: {str(e)}')  # Optional: Log the specific error to the console

            # Modify the message box to include information about failed file names
            if failed_files:
                failed_message = '\n'.join(failed_files)
                ui.messageBox(f'{success_count} files imported successfully\n{fail_count} files failed\n\nFAILED:\n{failed_message}')
            else:
                ui.messageBox(f'{success_count} files imported successfully.\n{fail_count} files failed')

        else:
            ui.messageBox('No file selected')

    except Exception as e:
        if ui:
            ui.messageBox(f'Failed:\n{traceback.format_exc()}')
