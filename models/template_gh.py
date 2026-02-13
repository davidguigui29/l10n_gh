# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models
from odoo.addons.account.models.chart_template import template


class AccountChartTemplate(models.AbstractModel):
    _inherit = "account.chart.template"

    @template("gh")
    def _get_gh_template_data(self):
        return {
            # These must exist in data/template/account.account-gh.csv (as template IDs)
            "property_account_receivable_id": "gh_110000",
            "property_account_payable_id": "gh_210000",
            "property_account_expense_categ_id": "gh_510000",
            "property_account_income_categ_id": "gh_410000",
            "code_digits": "6",
        }

    @template("gh", "res.company")
    def _get_gh_res_company(self):
        return {
            self.env.company.id: {
                "account_fiscal_country_id": "base.gh",

                # Optional but nice UX: account code prefixes used when creating bank/cash journals
                "bank_account_code_prefix": "120000",
                "cash_account_code_prefix": "121000",
                "transfer_account_code_prefix": "122000",

                # Default taxes (must exist in data/template/account.tax-gh.csv)
                "account_sale_tax_id": "GH_ST20",
                "account_purchase_tax_id": "GH_PT20",
            },
        }
