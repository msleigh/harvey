"""Global data related to boundary conditions."""

inner = {"type": None}
outer = {"type": None}
icon = {"type": None}


# Reset state for re-entrant runs.
def reset():
    """Reset global boundary condition data to defaults."""
    inner.clear()
    outer.clear()
    icon.clear()
    inner.update({"type": None})
    outer.update({"type": None})
    icon.update({"type": None})
