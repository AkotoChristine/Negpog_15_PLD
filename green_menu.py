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
