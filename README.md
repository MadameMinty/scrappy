# scrap.py

Simple script for website (wget, Chromium) monitoring (Xpath, regex) and communicating changes via an external tool.

## setup and usage

Just put both files somewhere in PATH. Dependencies I needed to make it run:
```
pip install lxml
apt-get install chromium-driver
```

Inspect the examples closely to not feed the script wrong parameters. Be aware this uses `eval()` and I proofed _nothing_. Create your own services (Python functions) using functions `request()` and `filter()`.

**`request()`**: The first argument is `'chrome'` (default if empty) or `'wget'`. The second is target URL.

**`filter()`**: The first argument is the result of a request. Then, a method: `'hash'` (default if empty), `'xpath'`, or `'regex'`. Finally, the pattern to match. Hash method takes an empty pattern for now, maybe I'll add CRC32/SHA1 selection later. 

Execute with e.g. `python3 scrap.py wgxp` to start function `_wgxp()`. I put it in cron.

Make sure to customize `scraphead.py` to have an already existing log path in `filepath` variable (maybe just `mkdir /var/log/scrappy`) and a working `communicate()` function. Mine uses Telegram, but I put Hangouts here for the sake of a demo.

## hangouts.py

To get hangouts.py present in the `communicate()` function by default, you'll need [Hangups](https://github.com/tdryer/hangups/), and then follow these steps:

1. Take [send_message_example.py](https://gist.github.com/tdryer/0cf6903eeb3dc948bae0)

2. In the beginning, blend in
```
import sys
CONVERSATION_ID = sys.argv[1]
MESSAGE = ' '.join(sys.argv[2:])
```

3. Modify `REFRESH_TOKEN_PATH` to work with your username

4. If Python >=3.7, then replace
`async(`
with
`ensure_future(`

You can get the target conversation ID by grepping Hangups logs:
`grep -C 1 'conversation_id' /home/USERNAME/.cache/hangups/log/hangups.log`
