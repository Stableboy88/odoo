import requests
from odoo import models, fields, api
import logging
import os

_logger = logging.getLogger(__name__)

class CurrencySync(models.Model):
    _name = 'currency.sync'
    _description = 'Currency Sync'

    @api.model
    def sync_currency_rates(self):
        url = 'https://www.bangkokbank.com/api/exchangerateservice/GetLatestfxrates'
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,th;q=0.8',
            'cache-control': 'no-cache',
            'ocp-apim-subscription-key': os.getenv('BANGKOK_BANK_API_KEY'),
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.bangkokbank.com/en/personal/other-services/view-rates/foreign-exchange-rates',
            'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            'sec-ch-ua-arch': 'arm',
            'sec-ch-ua-bitness': '64',
            'sec-ch-ua-full-version-list': '"Google Chrome";v="129.0.6668.100", "Not=A?Brand";v="8.0.0.0", "Chromium";v="129.0.6668.100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '',
            'sec-ch-ua-platform': 'macOS',
            'sec-ch-ua-platform-version': '15.0.1',
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            # Process the data as needed
            _logger.info("Currency rates synced successfully: %s", data)
        except requests.exceptions.RequestException as e:
            _logger.error("Error syncing currency rates: %s", e)