# VentilatorManeuverExtractionState
ZAM Breath Extraction - State Based

##Usage:
1. Create a folder (ex. named ventextract)
2. Place python file ventextract.py in that folder
3. Place ASC file from ventilator in that folder
4. Create a subfolder in the folder (ex. named "extracts")
5. Run python script with cmd arguments as follows "path of ASC file" "output files' root name" "path of output folder"
ex. with above examples:
cd into ventextract
python ventextract.py Rb14-DuBDPS BDPS extracts 
will output files into the extract folder with names BDPS-ZAM1, BDPS-ZAM2, ...
