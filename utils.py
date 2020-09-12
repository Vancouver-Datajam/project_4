def get_weight_kg_of_plastic(plastic_type):
    if plastic_type == "film":
        return 0.01
    elif plastic_type == "textiles":
        return 0.1
    elif plastic_type == "rigid beverage container":
        return 0.2
    elif plastic_type == "rigid non-beverage container":
        return 0.3
    elif plastic_type == "other":
        # TODO How do we decide the weight of "Other"
        return 0.01