# email-data
Command Line Python app to pull/enter/and see email data.

Please note - this is programmed to take email data exported from WordFly (which is pre-formatted with specific columns and rows.)

Usage: Python3 main.py '<filepath>' [optional <campaign_initial>] flag(s)

command line flags:
 - '-t (n)' / '--top (n)' = will show you the best performing email of the week.
 - '-w / --worst' = shows the worst performing email of the week.
 - '-c (NAME)' / '--campaign (NAME)' = filters csv by 'Campaign' and shows all email campaigns  that contain that NAME.
