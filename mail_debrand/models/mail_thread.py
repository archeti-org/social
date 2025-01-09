# Copyright 2019 ForgeFlow S.L.
#   Lois Rilo <lois.rilo@forgeflow.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import re

from odoo import models


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    def _replace_local_links(self, html, base_url=None):
        html = super()._replace_local_links(html, base_url=base_url)
        html = re.sub(
            r"""(Powered by\s(.*)Odoo</a>)""", "<div>&nbsp;</div>", html
        )
        return html
