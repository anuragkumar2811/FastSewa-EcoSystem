import jinja2
import pdfkit
import os

# 1. Setup - Tell Python where your HTML template is
template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

# 2. Load the template
template = template_env.get_template('invoice_template.html')

# 3. Create "Fake" Data (This simulates what Team B will send you later)
# We are filling the {{ placeholders }} in your HTML
context = {
    'customer_name': 'Rahul Sharma',
    'customer_phone': '+91 98765 43210',
    'customer_address': 'Sector 4, Patna, Bihar',
    'quote_id': 'FS-2025-001',
    'date': '13 Dec 2025',
    'service_category': 'Construction - FastSewa BuildNet',
    'service_description': 'Residential Construction (Ground Floor)',
    'rate': '1500',
    'quantity': '1200 sq ft',
    'amount': '18,00,000',
    'tax_amount': '3,24,000',
    'total_amount': '21,24,000'
}

# 4. Render the HTML with this data
output_text = template.render(context)

# 5. Configuration for PDFKit (Point to where you installed wkhtmltopdf)
# IF THIS FAILS, try removing the 'configuration' argument in the next step
try:
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe' # CHECK THIS PATH
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    
    # 6. Generate the PDF
    pdfkit.from_string(output_text, 'FastSewa_Quote_Test.pdf', configuration=config)
    print("✅ Success! 'FastSewa_Quote_Test.pdf' has been created.")
    
except OSError:
    print("❌ Error: Could not find wkhtmltopdf. Please check the path in the code.")