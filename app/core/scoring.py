def calculate_inherent_risk(severity, asset_criticality):
    """
    Inherent Risk = Severity × Asset Criticality
    """
    return severity * asset_criticality


def calculate_residual_risk(inherent_risk, control_effectiveness):
    """
    Residual Risk = Inherent Risk × (1 - Control Effectiveness)

    control_effectiveness is a number between 0 and 1
    """
    return inherent_risk * (1 - control_effectiveness)
