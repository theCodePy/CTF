# Walking An Application
## Premium room

flag1: What is the flag from the HTML comment?

	found a url from the comment /new-home-beta
	navigate to this page and the found the flag
	flag: THM{HTML_COMMENTS_ARE_DANGEROUS}

flag2: What is the flag from the secret link?

	there was a link in the <p> tag with href=/secret-page
	found the link in the home page source code. 
	navigate to the link and found the flag.
	flag: THM{NOT_A_SECRET_ANYMORE}

flag3: What is the directory listing flag?

	show all the resources have a common directory. /assets
	visited the page /assets and show all the resources are there.
	found a text file /assets/flag.txt
	flag: THM{INVALID_DIRECTORY_PERMISSIONS}

flag4: What is the framework flag?

	In the bottom the page a comment give me the framework website and version:
	visited the framework website it was written there we should be having a zip file in our website.
	so downloaded the file /tmp.zip from our target website. 
	flag: THM{KEEP_YOUR_SOFTWARE_UPDATED}

flag5: What is the flag behind the paywall?

	the intended approach was to view the news article that is primium only.
	from the inspector turn off the check box position: absolute. to view it.
	but I already found it in the css file the image file was encoded in base64.
	flag: THM{NOT_SO_HIDDEN}

flag6: What is the flag in the red box?

	it's rather unusual to me. in the developer mode --> sources.
	go to javascript file flash.mini.js  in this file the was something printed with javascript but instently flashed.
	by flash['remove']();
	so set a breakpoint in that by clicking on the left button on that line
	reload the page to get the red box where the flag is written.
	flag: THM{CATCH_ME_IF_YOU_CAN}

flag7: What is the flag shown on the contact-msg network request?

	in the /contact page, 
	go to network tab in the inspector.
	then click on send message to get the ajex reply message.
	also visiting /contact-msg can also get you the flag. 
	in the javascript file they used POST method in /contact-msg. but using GET method we can also get the flag.
	flag: THM{GOT_AJAX_FLAG}