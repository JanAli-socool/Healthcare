# patient.py
class Patient:
    def __init__(self, name, age, weight_kg, height_m):
        self.name = name
        self.age = age
        self.weight_kg = weight_kg
        self.height_m = height_m

    def calculate_bmi(self):
        return self.weight_kg / (self.height_m ** 2)

    def display_info(self):
        bmi = self.calculate_bmi()
        print(f"Patient: {self.name}")
        print(f"Age: {self.age} years")
        print(f"Weight: {self.weight_kg} kg")
        print(f"Height: {self.height_m} m")
        print(f"BMI: {bmi:.2f}")
