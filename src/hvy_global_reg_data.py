"""Global data for regions."""

# Number of regions inferred from user input
nregs = -1

# List of user-defined regions; each element is a dict of the region's properties
regions = {}


# Function to populate list of regions given user input.
def region(name, mat, xbound=None):
    """Initialise new region."""
    regions[name] = {
        "mat": mat,
        "xbound": xbound,
    }


def reset():
    """Reset region data to defaults."""
    global nregs
    nregs = -1
    regions.clear()
