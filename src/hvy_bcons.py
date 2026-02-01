"""Functions related to boundary conditions."""

import hvy_global_bcon_data as bcon


def setup():
    """Set up boundary conditions."""
    if bcon.inner["type"] == "dirichlet":
        bcon.inner["itype"] = 0
    else:
        if bcon.inner["type"] == "neumann":
            bcon.inner["itype"] = 1
        else:
            message = (
                f"Incorrect inner boundary type: {bcon.inner['type']}. "
                'Specify "dirichlet" or "neumann".'
            )
            raise ValueError(message)

    if bcon.outer["type"] == "dirichlet":
        bcon.outer["itype"] = 0
    else:
        if bcon.outer["type"] == "neumann":
            bcon.outer["itype"] = 1
        else:
            message = (
                f"Incorrect outer boundary type: {bcon.outer['type']}. "
                'Specify "dirichlet" or "neumann".'
            )
            raise ValueError(message)

    icontype = 0
    iconval = 0.0
    if bcon.icon["type"] is None:
        pass
    elif bcon.icon["type"] == "gaussian":
        icontype = 1
        iconval = bcon.icon["time"]
    elif bcon.icon["type"] == "sin":
        icontype = 2
        iconval = bcon.icon["value"]
    elif bcon.icon["type"] == "cos":
        icontype = 5
        iconval = bcon.icon["value"]
    elif bcon.icon["type"] == "chevron":
        icontype = 3
        iconval = bcon.icon["value"]
    elif bcon.icon["type"] == "constant":
        icontype = 4
        iconval = bcon.icon["value"]
    else:
        message = f"Boundary condition type not coded: {bcon.icon['type']}."
        raise ValueError(message)
    bcon.icon["itype"] = icontype
    bcon.icon["ival"] = iconval
