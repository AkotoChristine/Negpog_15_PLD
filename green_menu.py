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




