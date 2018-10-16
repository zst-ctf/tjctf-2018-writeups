# Blank
Web - 5 points

## Challenge 

Written by evanyeyeye

Someone told me there was a flag on this [site](https://blank.tjctf.org/), so why is it that I can only see blank?

## Solution

	$ curl https://blank.tjctf.org/
	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="utf-8">
	    <title>Blank</title>
	    <meta name="viewport" content="width=device-width, initial-scale=1">
	    <style type="text/css">
	        p {
	          position: absolute;
	          top: 35%;
	          left: 50%;
	          transform: translate(-50%, -50%);
	          font-size: 100px;
	        }
	    </style>
	</head>
	<body>
	    <p>『　　』</p>
	    <!-- flag: tjctf{50urc3_c0d3_n3v3r_l0535} -->
	</body>
	</html>

## Flag

	tjctf{50urc3_c0d3_n3v3r_l0535}