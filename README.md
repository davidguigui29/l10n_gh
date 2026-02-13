# Ghana Accounting Localization (`l10n_gh`)

`l10n_gh` is an Odoo localization module for Ghana accounting.
It provides a starter chart of accounts, Ghana VAT/levies taxes, and a Ghana tax report template.

## Features

- Ghana chart of accounts for SME setups
- Ghana VAT and levy tax structure (including 20% effective setup)
- Ghana tax report based on Odoo's generic tax report
- Demo data for quick testing

## Module Info

- Name: `Ghana - Accounting`
- Version: `1.0`
- Country: `Ghana (GH)`
- License: `LGPL-3`
- Dependencies:
  - `account`
  - `base_vat`

## Installation

1. Copy or keep this module in your custom addons path.
2. Update your apps list.
3. Install **Ghana - Accounting** (`l10n_gh`) from Apps.
4. Create a Ghana company or set company fiscal country to Ghana.
5. Load the Ghana chart of accounts if not auto-loaded.

## What Gets Loaded

- Chart template data from `data/l10n_gh_chart_data.xml`
- Ghana tax report data from `data/account_tax_report_data.xml`
- Demo records from:
  - `demo/l10n_gh_demo.xml`
  - `demo/demo_company.xml`

## Development Notes

- Chart template logic lives in `models/template_gh.py`.
- Migration helper currently attempts chart loading for companies using chart template `gh`.

## Contributing

Contributions are welcome.

If you want to contribute:

1. Fork the repository
2. Create a feature or fix branch
3. Commit clear, focused changes
4. Open a pull request with:
   - What changed
   - Why it changed
   - How it was tested

Issues, bug reports, tax rule corrections, and accounting improvements for Ghana are all appreciated.

## Support

For issues or feature requests, please open an issue in the repository where this module is maintained.
