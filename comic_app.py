import customtkinter as ctk
from tkinter import filedialog, messagebox
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Set the appearance and theme
ctk.set_appearance_mode("dark")  # Options: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Options: "blue" (standard), "green", "dark-blue"

class ComicInfoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ComicInfo.xml Creator")
        self.geometry("700x800")

        # List of fields
        self.fields = [
            "Title", "LocalizedSeries", "Series", "Number", "Count", 
            "Volume", "Publisher", "Year", "Month", "Day", 
            "Writer", "Penciller", "Inker", "Colorist", "Letterer", 
            "CoverArtist", "Editor", "Translator", "Genre", "Tags", 
            "Web", "PageCount", "LanguageISO", "Format", "SeriesGroup", 
            "StoryArc", "StoryArcNumber", "AlternativeSeries", 
            "AlternativeCount", "AgeRating", "GTIN", "Summary"
        ]

        self.age_rating_options = [
            "Unknown", "Rating Pending", "Early Childhood", "Everyone", 
            "G", "Everyone 10+", "PG", "Kids to Adults", "Teen", 
            "MA15+", "Mature 17+", "M", "R18+", "Adults Only 18+", "X18+"
        ]

        self.entries = {}

        # --- UI Layout ---
        # Create a main container frame
        self.main_container = ctk.CTkFrame(self, corner_radius=15)
        self.main_container.pack(pady=20, padx=20, fill="both", expand=True)

        # Header
        self.header = ctk.CTkLabel(
            self.main_container, 
            text="ComicInfo.xml Creator", 
            font=ctk.CTkFont(family="Segoe UI", size=24, weight="bold")
        )
        self.header.pack(pady=(20, 10), padx=20)

        # Scrollable Frame for all input fields
        self.scroll_frame = ctk.CTkScrollableFrame(
            self.main_container, 
            label_text="Comic Details",
            corner_radius=10
        )
        self.scroll_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.create_widgets()

        # Save Button - Placed at the bottom of the main container
        self.save_btn = ctk.CTkButton(
            self.main_container, 
            text="Export to ComicInfo.xml", 
            command=self.save_xml,
            font=ctk.CTkFont(size=16, weight="bold"),
            height=45,
            corner_radius=10
        )
        self.save_btn.pack(pady=20, padx=20)

    def create_widgets(self):
        # Using a grid layout inside the scrollable frame for alignment
        for i, field in enumerate(self.fields):
            # Label
            lbl = ctk.CTkLabel(self.scroll_frame, text=field + ":", font=ctk.CTkFont(size=13))
            lbl.grid(row=i, column=0, padx=20, pady=10, sticky="e")

            # Input logic
            if field == "AgeRating":
                ent = ctk.CTkComboBox(self.scroll_frame, values=self.age_rating_options, width=300)
                ent.set("Unknown")
            elif field == "Summary":
                ent = ctk.CTkTextbox(self.scroll_frame, width=300, height=100)
            else:
                ent = ctk.CTkEntry(self.scroll_frame, width=300)
            
            ent.grid(row=i, column=1, padx=20, pady=10, sticky="w")
            self.entries[field] = ent

    def save_xml(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".xml",
            initialfile="ComicInfo.xml",
            filetypes=[("XML files", "*.xml")]
        )

        if not file_path:
            return

        root_el = ET.Element("ComicInfo")

        for field in self.fields:
            widget = self.entries[field]
            
            if isinstance(widget, ctk.CTkTextbox):
                value = widget.get("1.0", "end-1c").strip()
            else:
                value = widget.get().strip()

            if value: 
                child = ET.SubElement(root_el, field)
                child.text = value

        xml_string = ET.tostring(root_el, encoding='utf-8')
        reparsed = minidom.parseString(xml_string)
        pretty_xml = reparsed.toprettyxml(indent="  ")

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(pretty_xml)
            messagebox.showinfo("Success", f"File saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    app = ComicInfoApp()
    app.mainloop()
