import os
import math
from fpdf import FPDF
from dotenv import load_dotenv
from datetime import datetime

# Load .env variables
load_dotenv()

# Constants - Pricing Coefficients (Defaults)
ALPHA = float(os.getenv("ALPHA", 1000))
BETA = float(os.getenv("BETA", 500))
GAMMA = float(os.getenv("GAMMA", 1.5))
DELTA = float(os.getenv("DELTA", 1.0))
EPSILON = float(os.getenv("EPSILON", 400))
MU1 = float(os.getenv("MU1", 200))
MU2 = float(os.getenv("MU2", 1500))
MU3 = float(os.getenv("MU3", 3000))
MU4 = float(os.getenv("MU4", 2000))
MU5 = float(os.getenv("MU5", 2500))

# Company Details
COMPANY_NAME = "Project-Money"
COMPANY_ADDRESS = "440, North street, Viralimalai, Pudukkottai - 621316"
COMPANY_EMAIL = "nishikanthpersonal@gmail.com"
COMPANY_PHONE = "0000000000"

# Feature Sets
complexity_features = {
    "Static Content": 1,
    "Responsive Design": 2,
    "Product Filters": 2,
    "Forms/Validation": 2,
    "API Integration": 3,
    "Live Data": 3,
    "Animations/Modals": 3,
    "Login/Auth": 4,
    "AR Viewer": 5,
    "Cart Logic": 4,
}

effort_features = {
    "Client Revisions": 2,
    "Late Content": 2,
    "New Tech Research": 3,
    "Debugging Time": 3,
    "Branding Rework": 2,
    "UX/UI Deep Work": 3,
}

special_addons = {
    "AR Try-On": MU2,
    "Real-time DB": MU3,
    "User Account System": MU4,
    "Admin Panel": MU5
}


class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 10, COMPANY_NAME, ln=True, align="C")
        self.set_font("Helvetica", "", 12)
        self.cell(0, 6, COMPANY_ADDRESS, ln=True, align="C")
        self.cell(0, 6, f"Email: {COMPANY_EMAIL} | Phone: {COMPANY_PHONE}", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, f"Generated on {datetime.now().strftime('%d-%m-%Y %H:%M')}", 0, 0, "C")


def ask_checklist(title, options: dict):
    print(f"\n{title}")
    for idx, feat in enumerate(options, 1):
        print(f"{idx}. {feat}")
    chosen = input("Select options (comma-separated numbers): ")
    selected = []
    for i in chosen.split(","):
        i = i.strip()
        if i.isdigit() and 0 < int(i) <= len(options):
            selected.append(list(options.items())[int(i)-1])
    return selected


def ask_yes_no(prompt):
    return input(f"{prompt} (1 for Yes, 0 for No): ").strip() == "1"

client_name = input("Client Name: ")

def generate_pdf(client_name, items):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "", 12)

    pdf.cell(0, 10, f"Quotation For: {client_name}", ln=True)
    pdf.ln(5)

    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(90, 8, "Description", 1)
    pdf.cell(30, 8, "Unit Price", 1)
    pdf.cell(30, 8, "Qty", 1)
    pdf.cell(40, 8, "Total", 1, ln=True)

    pdf.set_font("Helvetica", "", 12)
    grand_total = 0
    for item in items:
        desc = item["description"]
        price = item["unit_price"]
        qty = item["quantity"]
        total = price * qty
        grand_total += total

        desc_safe = desc.encode("latin-1", "replace").decode("latin-1")
        pdf.cell(90, 8, desc_safe, 1)
        pdf.cell(30, 8, f"Rs. {price:.2f}", 1)
        pdf.cell(30, 8, str(qty), 1)
        pdf.cell(40, 8, f"Rs. {total:.2f}", 1, ln=True)

    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(150, 10, "Grand Total", 1)
    pdf.cell(40, 10, f"Rs. {grand_total:.2f}", 1, ln=True)

    safe_client_name = client_name.replace(" ", "_")

    pdf.ln(10)
    pdf.set_font("Helvetica", "I", 10)
    pdf.multi_cell(0, 8, "Thank you for your business.\nLet us know if you have any questions or need modifications.")
    
    foldername = "quotations"
    os.makedirs(foldername, exist_ok = True)
    
    filename = f"quotation_{safe_client_name}_{datetime.now().strftime('%d-%m-%Y')}.pdf"
    filepath = os.path.join(foldername, filename)
    pdf.output(filepath)
    print(f"\n[+] Quotation generated successfully: {filename}")


def main():
    print("=== Project-M Quotation CLI ===")
    

    p = int(input("Number of Pages (p): "))
    t = int(input("Development Time in Hours (t): "))
    i = float(input("Internet/Data Cost (₹) (i): "))
    d = float(input("Domain & Hosting Cost (₹) (d): "))
    m = int(input("Client Mindset (1–10) (m): "))

    selected_complexity = ask_checklist("Page Complexity Features:", complexity_features)
    selected_efforts = ask_checklist("Extra Effort Factors:", effort_features)

    addons = []
    for addon in special_addons:
        if ask_yes_no(f"Include {addon}?"):
            addons.append((addon, special_addons[addon]))

    # Base Quotation Calculation
    s = max(1, min(sum(v for _, v in selected_complexity), 10))
    e = sum(v for _, v in selected_efforts)

    Q = (ALPHA * p * s) + (BETA * t) + (GAMMA * i) + (DELTA * d) + (EPSILON * e)
    Q += (MU1 * (p * s) * math.log(m + 1))
    Q += sum(price for _, price in addons)

    # Description Builder
    items = [
        {"description": f"{p} Pages with avg. complexity", "unit_price": ALPHA * s, "quantity": p},
        {"description": "Development Time", "unit_price": BETA, "quantity": t},
        {"description": "Internet/Data", "unit_price": i, "quantity": 1},
        {"description": "Domain & Hosting", "unit_price": d, "quantity": 1},
        {"description": "Effort Adjustments", "unit_price": EPSILON, "quantity": e},
        {"description": "Mindset/Scaling Impact", "unit_price": MU1 * (p * s) * math.log(m + 1), "quantity": 1},
    ]
    for name, price in addons:
        items.append({"description": name, "unit_price": price, "quantity": 1})

    print(f"\nEstimated Quotation: Rs. {Q:,.2f}")
    generate_pdf(client_name, items)


if __name__ == "__main__":
    main()