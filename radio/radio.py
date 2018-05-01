
def check_interval(tFile, tProgram):
    """Return true if tFile is within 3% if tProgram"""

    tolerance = 0.03  # Tolerance of 3%
    return (abs(tFile - tProgram) / tProgram) <= tolerance
