# FullstackScript
![GitHub Repo stars](https://img.shields.io/github/stars/zachariahsharma/FullstackScript)


Fusion 360 Script to automate the CAM process for 2D plates.

## Features

- Batch import of STEP/IGS files into the current Fusion design  [oai_citation_attribution:0‡GitHub](https://github.com/zachariahsharma/FullstackScript/blob/main/lib/importStep.py)  
- Load part dimensions and settings from a JSON configuration file  [oai_citation_attribution:1‡GitHub](https://github.com/zachariahsharma/FullstackScript/blob/main/lib/importJSON.py)  
- Nest parts using Fusion’s 2D true-shape Arrange solver  [oai_citation_attribution:2‡GitHub](https://github.com/zachariahsharma/FullstackScript/blob/main/lib/AutoArrange.py)  
- Generate CAM setups with stock offsets and WCS from customizable templates  [oai_citation_attribution:3‡GitHub](https://github.com/zachariahsharma/FullstackScript/blob/main/lib/SetupGenerator.py)  
- Delete empty or invalid toolpaths to streamline operations  [oai_citation_attribution:4‡GitHub](https://github.com/zachariahsharma/FullstackScript/blob/main/lib/DeleteToolpaths.py)  
- Post-process drills and profiles into NC programs via user‑selected folder  [oai_citation_attribution:5‡GitHub](https://github.com/zachariahsharma/FullstackScript/blob/main/lib/NewNCProgram.py)  

## Prerequisites

- Autodesk Fusion 360 with API support  
- The `.cps` post‑processor file for Laguna (path configured in `NewNCProgram.py`)  
- JSON config files matching the expected schema (see `test.json`)  

## Installation

1. Clone or download this repository to your local machine.  
2. In Fusion 360, open **Scripts and Add-Ins** → **Scripts** tab, click **➕** (Add), and select the `FullstackScript` folder.  [oai_citation_attribution:6‡Autodesk Help](https://help.autodesk.com/view/fusion360/ENU/?guid=SLD-MANAGE-SCRIPTS-ADD-INS&utm_source=chatgpt.com)  
3. (Optional) Check **Run on Startup** and click **Run** to execute immediately.  

## Configuration

- **JSON config** (`.json`): Must include keys such as  
  - `width`, `length`, `height`, `trueheight`  
  - `machine` (e.g., `"IQ"`, `"Swift"`), `material` (e.g., `"Aluminum"`, `"Polycarb"`)  [oai_citation_attribution:7‡GitHub](https://github.com/zachariahsharma/FullstackScript/blob/main/lib/importJSON.py)  
- **HSM templates**: Update file paths in  
  - `lib/SetupGenerator.py` for `.f3dhsm-template` files  
  - `lib/NewNCProgram.py` for the `.cps` post‑processor  

## Usage

Run the script from the **Scripts and Add-Ins** dialog. It will:

1. **importStep**: Prompt to select and import STEP/IGS files  [oai_citation_attribution:8‡GitHub](https://github.com/zachariahsharma/FullstackScript/blob/main/lib/importStep.py)  
2. **importJSON**: Prompt to select a JSON config and load data  [oai_citation_attribution:9‡GitHub](https://github.com/zachariahsharma/FullstackScript/blob/main/lib/importJSON.py)  
3. **AutoArrange**: Arrange imported parts on a 2D plane  [oai_citation_attribution:10‡GitHub](https://github.com/zachariahsharma/FullstackScript/blob/main/lib/AutoArrange.py)  
4. **SetupGenerator**: Create CAM setups and apply HSM templates  [oai_citation_attribution:11‡GitHub](https://github.com/zachariahsharma/FullstackScript/blob/main/lib/SetupGenerator.py)  
5. **DeleteToolpaths**: Remove empty or invalid toolpaths  [oai_citation_attribution:12‡GitHub](https://github.com/zachariahsharma/FullstackScript/blob/main/lib/DeleteToolpaths.py)  
6. **NewNCProgram**: Post-process and save NC programs to a chosen folder  [oai_citation_attribution:13‡GitHub](https://github.com/zachariahsharma/FullstackScript/blob/main/lib/NewNCProgram.py)  

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

- Autodesk Fusion 360 API and sample code  [oai_citation_attribution:14‡Autodesk Help](https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-9701BBA7-EC0E-4016-A9C8-964AA4838954&utm_source=chatgpt.com)  
- Portland CNC’s JSON import and STEP utilities  [oai_citation_attribution:15‡GitHub](https://github.com/zachariahsharma/FullstackScript/blob/main/lib/importJSON.py)  

## License

Distributed under the GPL‑3.0 License. See [LICENSE](LICENSE) for details.
