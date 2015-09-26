# oneplushax
Abusing the One Plus Invite system to take up several slots

To run this, assuming you have OSX -:

```
pip install selenium
brew install chromedriver
(optional) brew install phantomjs

python oneplus_invites.py
```

This script exploits a loophole in the OnePlus Invites system by way of inserting the period character in a Gmail ID. Periods can be inserted anywhere, but it will still refer to the same email (known property of Gmail IDs). However, OnePlus thinks they're different emails.

Note that there is a 15-second gap during which you have to manually verify the captcha. The rest is automated. Enjoy while it lasts.
