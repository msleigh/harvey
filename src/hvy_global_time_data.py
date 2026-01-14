"""Global data related to calculation time."""

dt = -1.0
end = -1.0


# Reset state for re-entrant runs.
def reset():
    """Reset global time data to defaults."""
    global dt, end
    dt = -1.0
    end = -1.0
