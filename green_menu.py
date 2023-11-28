#!/usr/bin/python3
class GreenMenu:
    def __init__(self):
        self.crops = self.load_crops_data()
        self.soil_types = self.load_soil_types_data()

    def load_crops_data(self):
        return [
            {"name": "Wheat", "climate": "Temperate", "temperature": 15, "soil_types": ["Loam", "Clay"]},
            {"name": "Rice", "climate": "Tropical", "temperature": 25, "soil_types": ["Clay", "Silt"]},
            # we will add more crops as needed
        ]
    def load_soil_types_data(self):
        return [
            {"name": "Loam", "description": "A balanced mixture of sand, silt, and clay"},
            {"name": "Clay", "description": "Heavy and retains water well"},
            # we will add more soil types as needed
        ]

    def display_menu(self):
        print("Welcome to GreeMenu - Your Agricultural Knowledge Hub")
        print("1. View Crop List")
        print("2. View Soil Types")
        print("3. Search Crop Information")
        print("4. Exit")


    def  run(self):
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
                print("Thank you for using GreeMenu. Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    

    def view_crop_list(self):
        print("\nList of Crops:")
        for crop in self.crops:
            print(f"{crop['name']} - Suitable Climate: {crop['climate']}, Suitable Temperature: {crop['temperature']}°C")
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
                print(f"Suitable Soil Types: {', '.join(crop['soil_types'])}")
                break
           

              if not found:
            print(f"Crop {crop_name} not found in the database.")

if _name_ == "_main_":
    app = GreeMenu()
    app.run()
