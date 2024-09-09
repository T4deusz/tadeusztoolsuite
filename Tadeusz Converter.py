import csv
import time
import customtkinter
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Set up the custom theme
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (default), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Colors: "blue" (default), "dark-blue", "green"

# Function to open a file dialog for selecting input file
def select_input_file():
    file_path = filedialog.askopenfilename(title="Select Input File (rm24output-players.txt)")
    if file_path:
        process_file(file_path)
    else:
        messagebox.showwarning("No File Selected", "Please select a file to convert.")

# Function to open a file dialog for selecting output file
def select_output_file():
    file_path = filedialog.asksaveasfilename(title="Select Output File Location and Name", defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    return file_path

# Function to simulate progress and delay
def update_progress(progress_bar, duration):
    steps = 100
    delay = duration / steps
    for i in range(steps + 1):
        time.sleep(delay)  # Simulate work by sleeping for each step
        progress_bar.set(i / 100)  # Update progress
        app.update_idletasks()  # Ensure progress bar updates in real-time

# Function to process the file
def process_file(input_file):
    # Define the new column order
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

    # Add a delay with progress bar
    update_progress(progress_bar, duration=10)  # 10 seconds to simulate task

    # Read the input file and reorder columns, adding 'firstnameid' with default value if missing
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
            reader = csv.DictReader(infile, delimiter='\t')
            
            # Add 'firstnameid' column if not in the file
            if 'firstnameid' not in reader.fieldnames:
                print("'firstnameid' column not found. Adding with default value.")
            
            writer = csv.DictWriter(outfile, fieldnames=new_column_order, delimiter='\t')
            writer.writeheader()
            
            # Write the rows with reordered columns, adding 'firstnameid' if it is missing
            for row in reader:
                if 'firstnameid' not in row:
                    row['firstnameid'] = 0
                writer.writerow({col: row.get(col, '') for col in new_column_order})

        messagebox.showinfo("Success", f"File successfully saved as: {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Main function to create the UI
def main():
    global app
    # Create a root window using customtkinter
    app = customtkinter.CTk()  
    app.geometry("400x300")
    app.title("Tadeusz Converter")

    # Set custom icon from image URL
    image_url = "https://i.ibb.co/Fm7KmMZ/sergio-ramos-espagne-1.jpg"
    response = requests.get(image_url)
    img_data = BytesIO(response.content)
    icon_image = Image.open(img_data)
    icon_image = icon_image.resize((64, 64), Image.LANCZOS)  # Use Image.LANCZOS for high-quality resampling
    icon_photo = ImageTk.PhotoImage(icon_image)
    
    # Set the window and taskbar icon
    app.iconphoto(False, icon_photo)

    # Create a label for the title at the top center
    title_label = customtkinter.CTkLabel(app, text="Tadeusz Converter", font=("Arial", 20))
    title_label.grid(row=0, column=0, pady=10, padx=20, sticky="n")

    # Create a button using customtkinter, center it below the title
    select_file_btn = customtkinter.CTkButton(app, text="Choose File to Convert", command=select_input_file)
    select_file_btn.grid(row=1, column=0, padx=20, pady=20, sticky="n")

    # Create a progress bar
    global progress_bar
    progress_bar = customtkinter.CTkProgressBar(app, width=300)
    progress_bar.grid(row=2, column=0, pady=20, padx=20)
    progress_bar.set(0)

    # Run the GUI loop
    app.mainloop()

# Run the main function
if __name__ == "__main__":
    main()
