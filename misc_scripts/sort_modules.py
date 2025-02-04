import re

# Define the sorting order for "Type"
TYPE_ORDER = {"scan": 1, "output": 2, "internal": 3}  # Others will be sorted later

def extract_type(div_block):
    """Extracts the Type from the div block."""
    match = re.search(r'<td><strong>Type:</strong></td>\s*<td>(.*?)</td>', div_block)
    return match.group(1) if match else "zzz"  # Default "zzz" ensures unknown types appear last

def extract_name(div_block):
    """Extracts the name appearing after '<span class="checkmark"></span>'."""
    match = re.search(r'<span class="checkmark"></span>\s*([\w-]+)', div_block)
    return match.group(1) if match else ""

def sort_divs_in_file(input_file, output_file):
    """Reads an input file, sorts <div> blocks based on Type first, then alphabetically by name."""
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Regex to capture entire <div class="tooltip checkbox-item"> blocks
    div_blocks = re.findall(r'<div class="tooltip checkbox-item">.*?</div>', content, re.DOTALL)

    # Sort div blocks first by Type order, then alphabetically by name
    sorted_divs = sorted(
        div_blocks, 
        key=lambda div: (TYPE_ORDER.get(extract_type(div), 99), extract_name(div))
    )

    # Write sorted content back
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n\n".join(sorted_divs))  # Separate divs with newline for readability

    print(f"Sorted content written to {output_file}")

# Example usage:
input_file = "../divs.txt"  # Change to your actual filename
output_file = "../sorted_output.html"
sort_divs_in_file(input_file, output_file)

