# Access Control


## Unprotected Functionalities
a website might host sensitive functionality at the following URL:
`https://insecure-website.com/admin`

This might be accessible by any user, not only administrative users who have a link to the functionality in their user interface. In some cases, the administrative URL might be disclosed in other locations, such as the `robots.txt` file:
`https://insecure-website.com/robots.txt`

Even if the URL isn't disclosed anywhere, an attacker may be able to use a wordlist to brute-force the location of the sensitive functionality. 

## Lab: Unprotected admin functionality

### Goal:  
This lab has an unprotected admin panel.
Solve the lab by deleting the user carlos. 

`https://0a9500ae038830ea822c602d00d000ba.web-security-academy.net/administrator-panel`

### Unprotected functionalities - continued

if the admin page is 
`https://insecure-website.com/administrator-panel-yb556`

it's not directly guessable, we can still use either wordlist of check out the page source to see if the JavaScript discloses any information

such as:

```javascript
<script>
	var isAdmin = false;
	if (isAdmin) {
		...
		var adminPanelTag = document.createElement('a');
		adminPanelTag.setAttribute('https://insecure-website.com/administrator-panel-yb556');
		adminPanelTag.innerText = 'Admin panel';
		...
	}
</script>
```