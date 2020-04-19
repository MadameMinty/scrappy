# scrappy
Simple script for website (wget, Chromium) monitoring (Xpath, regex) and communicating changes via an external tool (below instructions for Hangouts). Execute with e.g. `python3 scrap.py wgxp` to start function `_wgxp()`. I put it in Cron. Inspect the examples closely to not feed the script wrong parameters.

Make sure to customize `scraphead.py` to have a working `communicate()` function and an already existing log path in `filepath` variable.

To get hangouts.py, which requires Hangups https://github.com/tdryer/hangups/,

1. Take https://gist.github.com/tdryer/0cf6903eeb3dc948bae0

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

Tip, you can get the target conversation ID by grepping Hangups logs:
`grep -C 1 'conversation_id' /home/USERNAME/.cache/hangups/log/hangups.log`
