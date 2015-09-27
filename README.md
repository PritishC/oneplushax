# oneplushax
Abusing the One Plus Invite system to take up several slots

To run this, assuming you have OSX -:

```
pip install selenium
brew install chromedriver
(optional) brew install phantomjs

python oneplus_invites.py --email_base some_email --invite_url "https://someurl"
```

This script exploits a loophole in the OnePlus Invites system by way of inserting the period character in a Gmail ID. Periods can be inserted anywhere, but it will still refer to the same email (known property of Gmail IDs). However, OnePlus thinks they're different emails.

Note that there is a 10-second gap during which you have to manually verify the captcha. The rest is automated.

So the procedure goes somewhat like this -:

1. Sign up with your primary email - the one which you want to bump up in rank.
2. Generate the invite/referral link - we will use this in the script.
3. Now use a secondary email ID, which should be Gmail, and should be long enough.
4. Running the script with these two params should get you several confirmation links on
   the secondary email/Gmail ID.
5. I'm not sure if you need to follow them up, but do so. And voila, your primary email
   should be bumped up according to their system.
6. ???
7. Profit!
