import re
import pandas as pd

INPUT_MD = "template.md"
OUTPUT_EXCEL = "requirements.xlsx"

def extract_requirements():
    """Extracts all [REQ-#] labels from the Markdown file and saves them to an Excel file."""
    with open(INPUT_MD, "r", encoding="utf-8") as file:
        content = file.readlines()

    req_pattern = r"\[REQ-(\d+)\]"  # Matches [REQ-#]
    requirements = []
    seen_reqs = set()

    for line in content:
        matches = re.findall(req_pattern, line)
        for req_num in matches:
            req_label = f"REQ-{req_num}"
            if req_label in seen_reqs:
                print(f"⚠️ Duplicate requirement found: {req_label}")
            else:
                seen_reqs.add(req_label)
                requirements.append({"Requirement ID": req_label, "Description": line.strip()})

    if requirements:
        df = pd.DataFrame(requirements)
        df.to_excel(OUTPUT_EXCEL, index=False)
        print(f"Extracted {len(requirements)} requirements and saved to {OUTPUT_EXCEL}.")
    else:
        print("No requirements found in the Markdown file.")

if __name__ == "__main__":
    extract_requirements()