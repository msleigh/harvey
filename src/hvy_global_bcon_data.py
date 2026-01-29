"""Global data related to boundary conditions."""

inner = {"type": None}
outer = {"type": None}
icon = {"type": None}


def reset():
    """Reset boundary condition data to defaults."""
    inner.clear()
    inner.update({"type": None})
    outer.clear()
    outer.update({"type": None})
    icon.clear()
    icon.update({"type": None})
