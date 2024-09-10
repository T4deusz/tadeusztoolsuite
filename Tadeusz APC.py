import customtkinter
import tkinter as tk
from tkinter import simpledialog, filedialog
import csv

def button_callback():
     
   def prompt_for_values():
    root = tk.Tk()
    root.withdraw()  
    values = {}

   
    for column in columns:
        value = simpledialog.askstring("Input", f"Enter value for {column}:")
        if value is None:  
            break
        values[column] = value
    
    return values

columns = [
    'haircolorcode', 'facialhairtypecode', 'curve', 'jerseystylecode', 'agility', 'tattooback', 'accessorycode4',
    'gksavetype', 'positioning', 'tattooleftarm', 'hairtypecode', 'standingtackle', 'preferredposition3',
    'longpassing', 'penalties', 'animfreekickstartposcode', 'isretiring', 'longshots', 'gkdiving', 'icontrait2',
    'interceptions', 'shoecolorcode2', 'crossing', 'potential', 'gkreflexes', 'finishingcode1', 'reactions', 
    'composure', 'vision', 'contractvaliduntil', 'finishing', 'dribbling', 'slidingtackle', 'accessorycode3', 
    'accessorycolourcode1', 'headtypecode', 'firstnameid', 'driref', 'sprintspeed', 'height', 'hasseasonaljersey', 
    'tattoohead', 'preferredposition2', 'strength', 'shoetypecode', 'birthdate', 'preferredposition1', 'tattooleftleg', 
    'ballcontrol', 'phypos', 'shotpower', 'trait1', 'socklengthcode', 'weight', 'hashighqualityhead', 'gkglovetypecode', 
    'tattoorightarm', 'icontrait1', 'balance', 'gender', 'headassetid', 'gkkicking', 'lastnameid', 'defspe', 
    'internationalrep', 'shortpassing', 'freekickaccuracy', 'skillmoves', 'faceposerpreset', 'usercaneditname', 
    'avatarpomid', 'attackingworkrate', 'finishingcode2', 'aggression', 'acceleration', 'paskic', 'headingaccuracy', 
    'iscustomized', 'eyebrowcode', 'runningcode2', 'modifier', 'gkhandling', 'eyecolorcode', 'jerseysleevelengthcode', 
    'accessorycolourcode3', 'accessorycode1', 'playerjointeamdate', 'headclasscode', 'defensiveworkrate', 'tattoofront', 
    'nationality', 'preferredfoot', 'sideburnscode', 'weakfootabilitytypecode', 'jumping', 'skintypecode', 'personality', 
    'gkkickstyle', 'stamina', 'playerid', 'accessorycolourcode4', 'gkpositioning', 'headvariation', 
    'skillmoveslikelihood', 'trait2', 'shohan', 'skintonecode', 'shortstyle', 'overallrating', 'smallsidedshoetypecode', 
    'emotion', 'runstylecode', 'muscularitycode', 'jerseyfit', 'accessorycode2', 'shoedesigncode', 'playerjerseynameid', 
    'shoecolorcode1', 'hairstylecode', 'commonnameid', 'bodytypecode', 'animpenaltiesstartposcode', 'pacdiv', 
    'defensiveawareness', 'runningcode1', 'preferredposition4', 'volleys', 'accessorycolourcode2', 'tattoorightleg', 
    'facialhaircolorcode'
]
app = customtkinter.CTk()
app.title("Advanced Player Creator")
app.geometry("400x150")

button = customtkinter.CTkButton(app, text="Create Player", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
app.grid_columnconfigure(0, weight=1)
app.mainloop()