import customtkinter
import csv
import tkinter as tk
from tkinter import filedialog, messagebox
button = customtkinter.CTkButton(root_tk, fg_color="red") 
def button_callback():
    file_path = filedialog.askopenfilename(title="Select Input File (rm24output-players.txt)")
    if file_path:
        process_file(file_path)
    else:
        messagebox.showwarning("No File Selected", "Please select a file to convert.")
        
def select_output_file():
    file_path = filedialog.asksaveasfilename(title="Select Output File Location and Name", defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    return file_path
def process_file(input_file):
    new_column_order = [
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
    output_file = select_output_file()
    if not output_file:
        messagebox.showwarning("No Output File", "Output file not selected!")
        return

    try:
        with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
            reader = csv.DictReader(infile, delimiter='\t')
            
           
            if 'firstnameid' not in reader.fieldnames:
                print("'firstnameid' column not found. Adding with default value.")
            
            writer = csv.DictWriter(outfile, fieldnames=new_column_order, delimiter='\t')
            writer.writeheader()
            
            
            for row in reader:
                if 'firstnameid' not in row:
                    row['firstnameid'] = 0
                writer.writerow({col: row.get(col, '') for col in new_column_order})

        messagebox.showinfo("Success", f"File successfully saved as: {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


app = customtkinter.CTk()
app.title("Tadeusz Converter")
app.geometry("400x150")

button = customtkinter.CTkButton(app, text="Select File to convert", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20)
app.grid_columnconfigure(0, weight=1)
app.mainloop()