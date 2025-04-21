# FullstackScript
![GitHub Repo stars](https://img.shields.io/github/stars/zachariahsharma/FullstackScript)


Fusion 360 Script to automate the CAM process for 2D plates.

## Features

- Batch import of STEP/IGS files into the current Fusion design
- Load part dimensions and settings from a JSON configuration file
- Nest parts using Fusion’s 2D true-shape Arrange solver 
- Generate CAM setups with stock offsets and WCS from customizable templates 
- Delete empty or invalid toolpaths to streamline operations 
- Post-process drills and profiles into NC programs via user‑selected folder 

## Prerequisites

- Autodesk Fusion 360 with API support  
- The `.cps` post‑processor file for Laguna (path configured in `NewNCProgram.py`)  
- JSON config files matching the expected schema (see `test.json`)  

## Installation

1. Clone or download this repository to your local machine.  
2. In Fusion 360, open **Scripts and Add-Ins** → **Scripts** tab, click **➕** (Add), and select the `FullstackScript` folder. 
3. (Optional) Check **Run on Startup** and click **Run** to execute immediately.  

## Configuration

- **JSON config** (`.json`): Must include keys such as  
  - `width`, `length`, `height`, `trueheight`  
  - `machine` (e.g., `"IQ"`, `"Swift"`), `material` (e.g., `"Aluminum"`, `"Polycarb"`) 
- **HSM templates**: Update file paths in  
  - `lib/SetupGenerator.py` for `.f3dhsm-template` files  
  - `lib/NewNCProgram.py` for the `.cps` post‑processor  

## Usage

Run the script from the **Scripts and Add-Ins** dialog. It will:

1. **importStep**: Prompt to select and import STEP/IGS files
2. **importJSON**: Prompt to select a JSON config and load data
3. **AutoArrange**: Arrange imported parts on a 2D plane 
4. **SetupGenerator**: Create CAM setups and apply HSM templates 
5. **DeleteToolpaths**: Remove empty or invalid toolpaths 
6. **NewNCProgram**: Post-process and save NC programs to a chosen folder 
## Project Structure
```
FullstackScript/
├── FullstackPrototype.py      # Entry point: orchestrates the pipeline
├── lib/
│   ├── AutoArrange.py         # 2D true-shape nesting
│   ├── importStep.py          # STEP/IGS import
│   ├── importJSON.py          # JSON configuration loader
│   ├── SetupGenerator.py      # CAM setup & template application
│   ├── DeleteToolpaths.py     # Cleanup invalid toolpaths
│   ├── NewNCProgram.py        # NC program post-processing
│   └── templates/
│       ├── AluminumIQ.f3dhsm-template
│       ├── AluminumSwift.f3dhsm-template
│       ├── PolycarbIQ.f3dhsm-template
│       └── PolycarbSwift.f3dhsm-template
├── test.json                  # Example JSON config
└── LICENSE                    # GPL‑3.0 License
```

## Acknowledgements

- Autodesk Fusion 360 API and sample code
- Portland CNC’s JSON import and STEP utilities 

## License

Distributed under the GPL‑3.0 License. See [LICENSE](LICENSE) for details.
