import buildHtml
import sys


def start():
    RED = "\033[31m"
    GREEN = "\033[32m"
    BLUE="\033[34m"
    NC = '\033[0m'
    print BLUE + "Extracting data database..." + NC
    categoryId = sys.argv[1]
    categoryRow = buildHtml.getCategoryById(categoryId)
    if categoryRow is None:
        print RED + "No category with ID: " + categoryId + NC
    else:
        HtmlFile = categoryId + '.html'
        f = open( HtmlFile,'w')

        header = """<!DOCTYPE html>
        <head>
        <meta charset="utf-8">
        <link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
        <link rel="stylesheet" type="text/css" href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/css/bootstrap-combined.min.css">
        <link href="http://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet" type="text/css">
        <script src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
        <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
        <link rel="stylesheet" type="text/css" href="tree.css">
        </head>
        <body class='container'>
        <center><h2>Challenge: Ebay categories</h2></center>

        <div class="panel panel-default">
            <div class="panel-body">
                <h5><small>By: </small>Jeyson Anibal Palacio Palma</h5>
                <h5><small>Email: </small>japalacio0108@gmail.com</h5>
                <h5><small>Phone: </small>+57 300 713 5455</h3>
            </div>

        </div>
        <div class="tree well">

        """
        f.write(header)


        buildHtml.RenderList(f, categoryRow)

        footer = """</div></body>
        <script src='tree.js'></script>
        </html>"""
        f.write(footer)
        f.close()
        print GREEN + HtmlFile + NC


try:
    start()
except Exception as e:
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    NC = '\033[0m'
    print (RED + "Oops! can't proccess the request... " + str(e) + NC)
