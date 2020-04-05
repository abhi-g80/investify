# investify

Utility tool which scrapes investing.com website for price updates and send whatsapp notification if it breaches a predefined threshold.


## Setup

You can clone the project and simply run the script. You need to have a [twilio](https://www.twilio.com/) account (a free one would do as well). Setup your whatsapp dashboard in twilio first and use that numbers in the script. For the authentication export your Account SSID and Authentication token as follows :-

Account SSID

    $ export export TWILIO_ACCOUNT_SID='ACXXXXXXXXXXXXXXXXXXXXXXXXXXX'

Authentication token

    $ export TWILIO_AUTH_TOKEN='XXXXXXXXXXXXXXXXXXXXXXXXX'


## Usage

```bash
$ python investify.py +1456789012 +31234567789 crypto btc-usd 6600-6700 --sub-market bitcoin --threshold 10
```
This will notify when btc-usd prices breaches the price band of 6600-6700. It currently resets the price band from the last breached price.
