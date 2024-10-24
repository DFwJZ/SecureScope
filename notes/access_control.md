# Access Control


## Unprotected Functionalities
a website might host sensitive functionality at the following URL:
`https://insecure-website.com/admin`

This might be accessible by any user, not only administrative users who have a link to the functionality in their user interface. In some cases, the administrative URL might be disclosed in other locations, such as the `robots.txt` file:
`https://insecure-website.com/robots.txt`

Even if the URL isn't disclosed anywhere, an attacker may be able to use a wordlist to brute-force the location of the sensitive functionality. 

### Lab: Unprotected admin functionality

#### Goal:  
This lab has an unprotected admin panel.
Solve the lab by deleting the user carlos. 

`https://0a9500ae038830ea822c602d00d000ba.web-security-academy.net/administrator-panel`

## Unprotected functionalities - continued

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

### Lab: Unprotected admin functionality with unpredictable URL

#### Goal
 This lab has an unprotected admin panel. It's located at an unpredictable location, but the location is disclosed somewhere in the application.

Solve the lab by accessing the admin panel, and using it to delete the user `carlos`. 

#### Analysis 
found the admin endpoint is : `/admin-qlm0u4'`

```javascript
if (isAdmin) {
   var topLinksTag = document.getElementsByClassName("top-links")[0];
   var adminPanelTag = document.createElement('a');
   adminPanelTag.setAttribute('href', '/admin-qlm0u4');
```
## Parameter-based access control methods
 Some applications determine the user's access rights or role at login, and then store this information in a user-controllable location. This could be:

- A hidden field.
- A cookie.
- A preset query string parameter.

The application makes access control decisions based on the submitted value. For example:

`https://insecure-website.com/login/home.jsp?admin=true`

`https://insecure-website.com/login/home.jsp?role=1`

### Lab: User role controlled by request parameter

#### Goal 
 This lab has an admin panel at `/admin`, which identifies administrators using a forgeable cookie.

Solve the lab by accessing the admin panel and using it to delete the user `carlos`.

You can log in to your own account using the following credentials: `wiener:peter` 

#### Analysis
Inspect the page -> Storage -> Cookies -> set Admin value from false to true

## Horizonal Privilege Escalation
 Horizontal privilege escalation attacks may use similar types of exploit methods to vertical privilege escalation. For example, a user might access their own account page using the following URL:

`https://insecure-website.com/myaccount?id=123`

if an attacker modifies the `id` parameter value to that of another user, they might gain access to another user's account page, and the associated data and functions.

> Note: 
This is an example of an insecure direct object reference (IDOR) vulnerability. This type of vulnerability arises where user-controller parameter values are used to access resources or functions directly.

An application might use globally unique identifiers (GUIDs) to identify users. This may prevent an attacker from guessing or predicting another user's identifier.

### Lab: User ID controlled by request parameter, with unpredictable user IDs 

#### Goal
 This lab has a horizontal privilege escalation vulnerability on the user account page, but identifies users with GUIDs.

To solve the lab, find the GUID for `carlos`, then submit his API key as the solution.

You can log in to your own account using the following credentials: `wiener:peter` 

#### Analysis 
Log into account using given creds, go through the articles, found `Trying To Save The World` written by `carlos`
view Page Source found carlos' GUID:

```javascript
<h1>Trying To Save The World</h1>
<p><span id=blog-author><a href='/blogs?userId=c4afbab3-a0c2-4522-b5a1-363025708836'>carlos</a></span> | 29 September 2024</p>
```
Change the id from

`/my-account?id=63821ce2-f35c-4092-a686-f06471c56690`

to

`/my-account?id=c4afbab3-a0c2-4522-b5a1-363025708836`

found the API key.

## Horizontal to vertical privilege escalation
 An attacker might be able to gain access to another user's account page using the parameter tampering technique already described for horizontal privilege escalation:

`https://insecure-website.com/myaccount?id=456`

If the target user is an application administrator, then the attacker will gain access to an administrative account page.

#### Analysis 
Log into account using given creds -> change the id value in the url from wiener to administrator -> turn burp proxy on -> click update password -> retrieve password from the intercepted traffic -> using administrator creds to log into the account -> access to the admin panel and delete carlos