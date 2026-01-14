"""Global data for materials."""

# Number of materials inferred from user input
nmats = -1

# List of user-defined materials; each element is a dict of the material's properties
materials = {}


# Reset state for re-entrant runs.
def reset():
    """Reset global material state."""
    global nmats
    materials.clear()
    nmats = -1


# Function to populate list of materials given user input.
def material(name, d):
    """Initialise new material."""
    materials[name] = {"d": d,}
    materials[name]["id"] = len(materials)  # Start material numbering at 1


def reset():
    """Reset material data to defaults."""
    global nmats
    nmats = -1
    materials.clear()
