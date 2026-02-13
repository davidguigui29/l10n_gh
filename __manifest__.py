# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Ghana - Accounting",
    "icon": "/account/static/description/l10n.png",
    "countries": ["gh"],
    "version": "1.0",
    "category": "Accounting/Localizations/Account Charts",
    "summary": "Ghana chart of accounts, VAT/Levies taxes, and tax report",
    "description": """
Ghana localisation module for Odoo Accounting.

Includes:
- Ghana chart of accounts (SME starter)
- VAT / Levies tax structure
- Ghana Tax Report (based on Odoo Generic Tax Report)
""",

    "depends": [
        "account",
        "base_vat",
    ],
    "auto_install": ["account"],
    "data": [
        "data/l10n_gh_chart_data.xml",
        "data/account_tax_report_data.xml",
    ],
    "demo": [
        "demo/l10n_gh_demo.xml",
        "demo/demo_company.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
    "application": False,
}
