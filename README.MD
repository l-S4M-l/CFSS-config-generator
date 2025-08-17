# Folder Generator for CFSS

This tool helps generate a settings file (`setup.json`) for use with another tool called **CFSS**.  
It guides you to select your `rpcs3.exe` file and automatically locates your Skate 3 game installation, supporting both BLES and BLUS versions.

## How It Works

1. Launch the tool.
2. Select your `rpcs3.exe` using the file dialog.
3. The tool reads your RPCS3 configuration to find your Skate 3 game path.
4. If both BLES and BLUS versions are found, you can choose which one to use.
5. The tool creates a `setup.json` file with the correct paths for CFSS.

## Requirements

- Python 3
- PyQt5

## Usage

```sh
pip install -r requirement.txt
python main.py
```

## Output

- `setup.json` containing the paths needed for CFSS.

## Notes

- Make sure RPCS3 and Skate 3 are installed and properly configured.
- This tool does not modify any game