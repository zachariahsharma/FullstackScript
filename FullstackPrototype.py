"""This file acts as the main module for this script."""

import traceback
import adsk.core
import adsk.fusion
import adsk.cam
import os
app = adsk.core.Application.get()
ui  = app.userInterface
try:
    from .lib.AutoArrange import AutoArrange
    from .lib.SetupGenerator import SetupGenerator
    from .lib.DeleteToolpaths import DeleteToolpaths
    from .lib.importStep import importStep
    from .lib.importJSON import importJSON
    from .lib.NewNCProgram import NewNCProgram
except:
    ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))



def run(_context: str):
    """This function is called by Fusion when the script is run."""

    try:
        importStep()
        data = importJSON()
        AutoArrange(data)
        SetupGenerator(data)
        DeleteToolpaths()
        NewNCProgram()
    except:  
        ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
        app.log(f'Failed:\n{traceback.format_exc()}')
