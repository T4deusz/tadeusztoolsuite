import tkinter as tk
from tkinter import simpledialog, filedialog
import csv

# Define the player attribute columns
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

# Function to prompt for a value for each column
def prompt_for_values():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    values = {}

    # Ask for a value for each column
    for column in columns:
        value = simpledialog.askstring("Input", f"Enter value for {column}:")
        if value is None:  # If the user cancels, break
            break
        values[column] = value
    
    return values

# Function to save the compiled values into a txt file
def save_to_file(values):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.asksaveasfilename(title="Save File", defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    
    if file_path:
        with open(file_path, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=columns, delimiter='\t')
            writer.writeheader()
            writer.writerow(values)
        print(f"File saved as: {file_path}")
    else:
        print("Save operation was cancelled.")

# Main function to run the script
def main():
    # Prompt user for values
    player_values = prompt_for_values()
    
    # If values were provided, save them to a file
    if player_values:
        save_to_file(player_values)

# Run the script
if __name__ == "__main__":
    main()
