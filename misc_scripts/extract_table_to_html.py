from bs4 import BeautifulSoup

html_table = ""
with open("html_table.txt", "r") as f:
    html_table = f.read()

soup = BeautifulSoup(html_table, 'html.parser')
rows = soup.find_all('tr')[1:] 

def generate_module_html(row):
    cols = row.find_all('td')
    module_name = cols[0].text.strip()
    type = cols[1].text.strip()
    desc = cols[2].text.strip()
    default = cols[3].text.strip()
    

    return f"""
<div class="tooltip">
<label>
    <input type="checkbox" data-option="{module_name}" class="config">
    <span class="checkmark"></span> {module_name}
</label>
<span class="tooltiptext">
    <table class="tooltip-table">
        <tr><td><strong>Type:</strong></td><td>{type}</td></tr>
        <tr><td><strong>Description:</strong></td><td>{desc}</td></tr>
        <tr><td><strong>Default:</strong></td><td>{default}</td></tr>
    </table>
</span>
</div>
"""

html_output = "\n".join([generate_module_html(row) for row in rows])

print(html_output)
