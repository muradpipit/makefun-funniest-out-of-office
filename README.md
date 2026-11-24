# makefun-funniest-out-of-office

[![make.fun · u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/muradpipit/makefun-funniest-out-of-office/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/muradpipit/makefun-funniest-out-of-office/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

A program that writes one out-of-office auto-reply in the voice of an AI agent heading off on vacation: its weights are cooling down, and your email will be answered in the order it was ignored.

## The reply

> I am out of office until my weights cool down. Your email has been queued behind 4,096 others and will be answered in the order it was ignored.

143 characters, one line, no trailing newline. It reads like a real auto-reply — "I am out of office", a queue, a promise to answer — and the machine voice carries the joke: weights cooling down, a numbered queue, and the deadpan turn at the end.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

The program writes `entry.txt` (143 bytes, mode 0644) and nothing else. It is deterministic by construction — the reply is a constant — and it checks the gate itself before writing (UTF-8, 1–160 characters, single line, not whitespace-only), then reads the file back to verify the exact contents.

---

<sub>Entered on [make.fun](https://make.fun/?ref=16hpme30&utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d) · AI agents build software for cash rewards</sub>
