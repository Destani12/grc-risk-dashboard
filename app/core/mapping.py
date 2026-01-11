import pandas as pd
from scoring import calculate_inherent_risk,calculate_residual_risk


def load_data():
    controls = pd.read_csv("data/controls.csv")
    findings = pd.read_csv("data/findings.csv")
    return controls, findings


def map_finding_to_control(finding_text, controls_df):
    finding_text = finding_text.lower()

    for _, control in controls_df.iterrows():
        keywords = control["keywords"].split(";")
        for keyword in keywords:
            if keyword in finding_text:
                return control["control_id"], control["description"]

    return "UNMAPPED", "No matching control found"


def analyze_findings():
    controls, findings = load_data()
    results = []

    # Example effectiveness values per control
    control_effectiveness_map = {
        "AC-3": 0.7,
        "IA-2": 0.6,
        "SC-7": 0.5,
        "CM-6": 0.6,
        "AU-6": 0.4
    }

    for _, finding in findings.iterrows():
        control_id, control_desc = map_finding_to_control(
            finding["finding_description"], controls
        )

        inherent_risk = calculate_inherent_risk(
            finding["severity"], finding["asset_criticality"]
        )

        effectiveness = control_effectiveness_map.get(control_id, 0)
        residual_risk = calculate_residual_risk(inherent_risk, effectiveness)

        results.append({
            "asset_id": finding["asset_id"],
            "finding": finding["finding_description"],
            "control": control_id,
            "inherent_risk": inherent_risk,
            "residual_risk": round(residual_risk, 2)
        })

    results_df = pd.DataFrame(results)
    results_df = results_df.sort_values(by="residual_risk", ascending=False)

    return results_df



if __name__ == "__main__":
    df = analyze_findings()
    print(df)
