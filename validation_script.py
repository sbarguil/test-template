import os
import subprocess

def validate_markdown(markdown_file):
    """Performs validation checks on the Markdown file."""
    # Example 1: Check for required sections
    with open(markdown_file, "r") as f:
        content = f.read()
        if "# Summary" not in content:
            raise ValueError("Missing 'Summary' section")

    # Example 2: Check for broken links (using a tool like `markdown-link-check`)
    try:
        subprocess.run(["markdown-link-check", markdown_file], check=True)
    except subprocess.CalledProcessError:
        raise ValueError("Broken links found")

    # Add more validation checks as needed...

if __name__ == "__main__":
    markdown_file = "template.md" 
    try:
        validate_markdown(markdown_file)
        print("Markdown validation passed!")
    except ValueError as e:
        print(f"Markdown validation failed: {e}")
        exit(1)  # Fail the Travis CI build