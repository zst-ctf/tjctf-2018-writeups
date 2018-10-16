# Central Savings Account
Web - 10 points

## Challenge 

Written by evanyeyeye

I seem to have forgotten the password for my [savings account](https://central_savings_account.tjctf.org/). What am I gonna do?

The flag is not in standard flag format.


## Solution

View source code of page

We find out that the password is validated client-side in this file: https://central_savings_account.tjctf.org/static/main.js

	$(document).ready(function() {
	    $("#login-form").submit(function() {
	        if (md5($("#password").val()).toLowerCase() === "698967f805dea9ea073d188d73ab7390") {
	            $("html").html("<h1>Login Succeeded!</h1>");
	        }
	        else {
	            $("html").html("<h1>Login Failed!</h1>");
	        }
	    })
	});

Google search for the hash and we find the reversed hash results: https://hashtoolkit.com/reverse-md5-hash/698967f805dea9ea073d188d73ab7390

	Algorithm	Hash	Decrypted
	md5	698967f805dea9ea073d188d73ab7390	avalon


## Flag

	avalon