from PyQt5 import QtWidgets
import sys
import json

def main():
    app = QtWidgets.QApplication(sys.argv)
    # Open file dialog asking for rpcs3.exe
    file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
        None,
        "Select rpcs3.exe",
        "",
        "Executable Files (rpcs3.exe)"
    )
    if file_path:
        base_path = "/".join(file_path.split("/")[:-1])
        
        with open(f"{base_path}/config/games.yml") as file:
            games_data = file.read()
            file.close()

        games_data = games_data.split("\n")

        BLES = False
        BLUS = False

        for i in games_data:
            potention_paths = {}

            if "BLES00760" in i.upper():
                BLES = True
                potention_paths["BLES"] = i.split(": ")[1].replace("//","/")
            elif "BLUS30464" in i.upper():
                BLUS = True
                potention_paths["BLUS"] = i.split(": ")[1].replace("//","/")

        if BLUS == True and BLES == True:
            Valid_selection = False
            while Valid_selection == False:

                selection = input("you have both versions of skate 3 installed\n please select what version you would like to use\n TYPE BLES or BLUS: ")

                if selection.upper() == "BLES":
                    BLUS = False
                    Valid_selection = True
                elif selection.upper() == "BLUS":
                    BLES = False
                    Valid_selection = True
            
        if BLES != False or BLUS != False:
            if BLES == True:
                final_path = potention_paths["BLES"]
            elif BLUS == True:
                final_path = potention_paths["BLUS"]           


            if final_path[-1:] == "/":
                final_path = final_path[:-1]
            

            final_data = {"skate_path": final_path, "rpcs3_path": base_path}
            with open("setup.json", "w+") as file:
                file.write(json.dumps(final_data))

            

if __name__ == "__main__":
    main()