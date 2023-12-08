#!/usr/bin/python3
import mysql.connector

class GreenMenu:
    def _init_(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="christine",
            database="greenmenu"
        )
        self.crops = self.load_crops_data()
        self.soil_types = self.load_soil_types_data()

    def execute_query(self, query, data=None, fetch_all=False):
        cursor = self.db.cursor(dictionary=True)
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        if fetch_all:
            result = cursor.fetchall()
        else:
            result = cursor.fetchone()
        cursor.close()
        return result

    def load_crops_data(self):
        query = """
            SELECT c.*, st.name AS soil_type
            FROM crops c
            JOIN soil_types st ON c.soil_type_id = st.id
        """
        return self.execute_query(query, fetch_all=True)

    def load_soil_types_data(self):
        query = "SELECT * FROM soil_types"
        return self.execute_query(query, fetch_all=True)

    def display_menu(self):
        print("Welcome to GreenMenu - Your Agricultural Knowledge Hub")
        print("1. View Crop List")
        print("2. View Soil Types")
        print("3. Search Crop Information")
        print("4. Farm Tool Maintenance")
        print("5. Suggest Fertilizer for Soil Type")
        print("6. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.view_crop_list()
            elif choice == '2':
                self.view_soil_types()
            elif choice == '3':
                self.search_crop_info()
            elif choice == '4':
                self.perform_farm_tool_maintenance()
            elif choice == '5':
                self.suggest_fertilizer()
            elif choice == '6':
                print("Thank you for using GreeMenu. Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


    
    def view_crop_list(self):
        print("\nList of Crops:")
        for crop in self.crops:
            print(f"{crop['name']} - Suitable Climate: {crop['climate']}, Suitable Temperature: {crop['temperature']}°C, Soil Type: {crop['soil_type']}")
        print()

    
    def view_soil_types(self):
        print("\nList of Soil Types:")
        for soil_type in self.soil_types:
            print(f"{soil_type['name']} - Description: {soil_type['description']}")
        print()

    def search_crop_info(self):
        crop_name = input("Enter the name of the crop: ")
        found = False
        
        for crop in self.crops:
            if crop['name'].lower() == crop_name.lower():
                found = True
                print(f"\nCrop Information for {crop['name']}:")
                print(f"Suitable Climate: {crop['climate']}")
                print(f"Suitable Temperature: {crop['temperature']}°C")
                print(f"Suitable Soil Types: {crop['soil_type']}")
                break

        if not found:
            print(f"Crop {crop_name} not found in the database.")

    def perform_farm_tool_maintenance(self):
        print("\nFarm Tool Maintenance")
        tool_name = input("Enter the name of the tool: ")
        maintenance_tips = {
            "shovel": "Clean off dirt and debris after each use. Sharpen the blade regularly to ensure effective digging.",
            "hoe": "Check for any bends or cracks in the blade. Keep the blade sharp for better performance.",
            "rake": "Inspect for any broken or loose tines. Replace any damaged tines to ensure efficient raking.",
            "pruning shears": "Clean and oil the blades after each use. Sharpen the blades to ensure clean cuts on plants.",
            "wheelbarrow": "Check the tires for proper inflation. Grease the wheel bearings regularly for smooth movement.",
            "pitchfork": "Inspect for any bent or damaged tines. Keep the tines sharp for effective pitching.",
            "chainsaw": "Clean the air filter and chain regularly. Keep the chain sharp for efficient cutting.",
        }

        if tool_name.lower() in maintenance_tips:
            print(f"\nMaintenance tips for {tool_name}:")
            print(maintenance_tips[tool_name.lower()])
        else:
            print("Maintenance tips not available for this tool.")
            
    def suggest_fertilizer(self):
        fertilizer_info = {
            "sandy": {
                "nitrogen": "High",
                "phosphorus": "High",
                "potassium": "High",
                "suggested_fertilizers": ["Ammonium nitrate", "Triple superphosphate", "Muriate of potash"],
            },
            "clay": {
                "nitrogen": "Moderate",
                "phosphorus": "Moderate",
                "potassium": "Moderate",
                "suggested_fertilizers": ["Urea", "Monoammonium phosphate", "Potassium sulfate"],
            },
            "loam": {
                "nitrogen": "Balanced",
                "phosphorus": "Balanced",
                "potassium": "Balanced",
                "suggested_fertilizers": ["Complete fertilizer", "Compost", "Manure"],
            },
        }

        soil_type = input("Enter your soil_type choice: ")

        if soil_type not in fertilizer_info:
            print("\033[91mFertilizer information not available for this soil type.\033[0m\n\n")
            return -1
        
        suggested_fertilizer_info = {
            "soil_type": soil_type,
            "nitrogen": fertilizer_info[soil_type]["nitrogen"],
            "phosphorus": fertilizer_info[soil_type]["phosphorus"],
            "potassium": fertilizer_info[soil_type]["potassium"],
            "suggested_fertilizers": fertilizer_info[soil_type]["suggested_fertilizers"],
        }

        if isinstance(suggested_fertilizer_info, str):
            print(suggested_fertilizer_info)
        else:
            print(f"Suggested fertilizers for {soil_type} soil:")
            print(f"\tNitrogen: {suggested_fertilizer_info['nitrogen']}")
            print(f"\tPhosphorus: {suggested_fertilizer_info['phosphorus']}")
            print(f"\tPotassium: {suggested_fertilizer_info['potassium']}")
            print(f"\tSuggested fertilizers: {', '.join(suggested_fertilizer_info['suggested_fertilizers'])}")

    # Example usage

if __name__ == "_main_":
    app = GreenMenu()
    app.run()
