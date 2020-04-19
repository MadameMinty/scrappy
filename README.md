# scrap.py

Simple script for website (wget, Chromium) monitoring (Xpath, regex) and communicating changes via an external tool.

## setup and usage

Just put both files somewhere in PATH. Dependencies I needed to make it run:
```
pip install lxml
apt-get install chromium-driver
```

Execute with e.g. `python3 scrap.py wgxp` to start function `_wgxp()`. I put it in cron. Inspect the examples closely to not feed the script wrong parameters.

Make sure to customize `scraphead.py` to have an already existing log path in `filepath` variable (maybe just `mkdir /var/log/scrappy`) and a working `communicate()` function. 

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
