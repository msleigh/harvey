"""Global data for regions."""

# Number of regions inferred from user input
nregs = -1

# List of user-defined regions; each element is a dict of the region's properties
regions = {}


# Function to populate list of regions given user input.
def region(name, mat, xbound=None):
    """Initialise new material."""
    regions[name] = {"mat": mat, "xbound": xbound,}
