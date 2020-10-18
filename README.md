## Step 1:
### Use the built in argparse python library and use it generate a command line app for submitting  film reviews:


The app should support submitting  multiple  reviews (by repeatedly running python app.py)

*Note: If you’re having trouble getting argparse to work, feel free to use python’s inbuilt “input” function instead to read values from the command line.*



## Step 2:
### Install the Flask python library and setup a route that serves the following  static HTML page:
```
<doctype html>
    <html>
        <head>
            <title> All Films</title>
        </head>
        <body>
            <ul>
                <li>Flubber</li>
                <li>Jumanji</li>
                <li>Aladdin</li>
            </ul>
        </body>
    </html>
```


You should serve this under the route *"/films/list"* on your flask web server.
*Hint:* You’ll want to place the html in a named folder and use the send_from_directory method from the flask module.


## Step 3:
### Serve a templated table of films along with their star ratings on the route "films/table“:
        FILM        STARS
        Flubber       3
        Jumanji       5
        Aladdin       4

The films should be read from the file generated in Step 1.

*Hint:* You’ll want to place your template in the /templates folder and use the built-in Flask render_template() method.

## Step 4:
### Add support for filtering this list by star rating
 e.g. "films/table?stars=3" should return just:
        FILM        STARS
        Flubber       3
 
## Step 5:
### Finally build a HTTP form served on the route "/films/submit" that fulfils the function of step 1.
If you’ve got this working feel free to experiment with the include/excludes templating structures introduced today or play around with the features listed on the Jinja Template Designer Documentation.
