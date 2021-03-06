# investify

Utility tool which scrapes investing.com website for price updates and send whatsapp notification if it breaches a predefined threshold.


## Installation

    $ pip install investify


## Setup

You can clone the project and simply run the script. You need to have a [twilio](https://www.twilio.com/) account (a free one would do as well). Setup your whatsapp dashboard in twilio first and use that numbers in the script. For the authentication export your Account SSID and Authentication token as follows :-

Account SSID

    $ export TWILIO_ACCOUNT_SID='ACXXXXXXXXXXXXXXXXXXXXXXXXXXX'

Authentication token

    $ export TWILIO_AUTH_TOKEN='XXXXXXXXXXXXXXXXXXXXXXXXX'


## Usage

    $ investify +1456789012 +31234567789 crypto btc-usd 6600-6700 --sub-market bitcoin --threshold 10

This will notify when btc-usd prices breaches the price band of 6600-6700. It currently resets the price band from the last breached price.

The tool will logging INFO (or DEBUG) level messages in standard out. This can certainly be redirected to a specified log file.

Debug level messages as follows :-

    $ investify --debug +11234567890 +7112356789 crypto btc-usd 6600-6700 --sub-market bitcoin --threshold 10 --interval 0.1
    2020-04-05 20:13:38 [DEBUG] main() - Logging set to debug
    2020-04-05 20:13:38 [DEBUG] main() - crypto/bitcoin/btc-usd end point will be queried.
    2020-04-05 20:13:39 [DEBUG]  run() - Fetched page successfully.
    2020-04-05 20:13:39 [DEBUG]  run() - Price of btc-usd is $6804.9.
    2020-04-05 20:13:39 [ INFO]  run() - Price 6804.9 breached price band [6600.0, 6700.0].
    2020-04-05 20:13:39 [DEBUG]  run() - Resetting price band with threshold value 10.0.
    2020-04-05 20:13:39 [ INFO]  run() - Resetting price band to [6798.0951, 6811.704899999999].
    2020-04-05 20:13:39 [DEBUG]  run() - Sending text.
    2020-04-05 20:13:46 [DEBUG]  run() - Fetched page successfully.
    2020-04-05 20:13:46 [DEBUG]  run() - Price of btc-usd is $6803.6.
    ^C
    2020-04-05 20:13:49 [ INFO] main() - Caught interrupt, exiting...

Help menu for the tool.

    $ investify -h
    Usage: investify.py [options...] [to number] [from number] [market] [contract]
                        [priceband]

      Utiltiy script to notify if instrument price fluctuates out of price band.

    Options:
      -s, --symbol TEXT      Contract symbol. [default: contract]
      -t, --threshold FLOAT  Threshold in bps.  [default: 100.0]
      -i, --interval FLOAT   Interval to perform check (mins).  [default: 1.0]
      -m, --sub-market TEXT  E.g. crypto is market and bitcoin is sub market.
      -d, --debug            Print debug messages.
      -h, --help             Show this message and exit.

`to number` should be your whatsapp number whereas `from number` should the number given by Twilio to be used for your whatsapp sandbox. You can consult official Twilio for whatsapp [page](https://www.twilio.com/docs/whatsapp/api).


## Test

Remember to export twilio environment variables before running the tests.

    $ cd <project dir>/investify
    $ py.tests tests
