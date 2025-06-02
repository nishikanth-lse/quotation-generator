**QUOTATION GENERATOR**

Author   : Nishikanth  
Version  : 1.0  
License  : © 2025 Nishikanth. All Rights Reserved.

--------------------------------------------------
PROJECT OVERVIEW
--------------------------------------------------
This is a professional CLI-based quotation generator tailored for freelancers and tech consultants. It intelligently evaluates effort, complexity, client behavior, and technical requirements to auto-generate a detailed PDF quotation using customizable pricing coefficients.

--------------------------------------------------
FEATURE HIGHLIGHTS
--------------------------------------------------
- Dynamic quotation based on:
  - Page count & complexity
  - Development time
  - Internet and hosting costs
  - Client behavior factor
  - Additional complexity & effort features
  - Optional premium add-ons (AR, Admin Panel, etc.)

- Uses `.env` file for pricing customization
- Clean PDF quotation output with professional layout
- Organized file output system under `/quotations/`
- Works fully within the terminal — no GUI needed

--------------------------------------------------
REQUIREMENTS
--------------------------------------------------
- Python 3.8+
- Dependencies:
  - `fpdf`
  - `python-dotenv`

Install with:
> pip install fpdf python-dotenv

--------------------------------------------------
USAGE
--------------------------------------------------
1. Set your coefficient values (optional) in a `.env` file:
   Example:

- `ALPHA=1000 BETA=500 GAMMA=1.5 DELTA=1.0 EPSILON=400 MU1=200 MU2=1500 MU3=3000 MU4=2000 MU5=2500`

2. Run the script:
> python project_m_quote.py

3. Enter client name, and input various required project metrics and feature selections when prompted.

4. The tool will:
- Calculate your total quotation
- Generate a clean PDF saved in the `/quotations/` folder

--------------------------------------------------
OUTPUT SAMPLE
--------------------------------------------------
quotation_John_Doe_20-04-2025.pdf

Includes:
- Itemized description (pages, time, hosting, mindset factor)
- Optional add-ons like Admin Panel, AR Viewer, etc.
- Grand total with breakdown
- Branding with company address & contact info

--------------------------------------------------
LICENSE
--------------------------------------------------
© 2025 Nishikanth. All Rights Reserved.

This software is proprietary and confidential. Redistribution or modification without explicit permission is prohibited.

--------------------------------------------------
CONTACT
--------------------------------------------------
Email    : nishikanthpersonal@gmail.com   
LinkedIn : https://www.linkedin.com/in/a-nishikanth/ 

--------------------------------------------------


