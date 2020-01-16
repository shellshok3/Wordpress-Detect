import sys
import requests
import threading
import thread
from termcolor import colored
import json
from threading import Thread


###############################################################

def wp_login_page(url):
   try:

         readme = requests.get(url +"/readme.html")
         readme_source = readme.text

         if 'wp-admin' in readme_source:

              wp_login = requests.get(url +"/wp-login.php")
              wp_login_source = wp_login.text
              
              if '<input type="password"' in wp_login_source:

                   print("\n    [OK] " + " [ " + url + " ] " + " Is Wordpress WebSite\n\n ")

                   ok = open ('Wp-Website.txt','a+')
                   ok.write("\n" + url + "\n")
                   ok.close()
            

         else:
            print("Web Site Is Not Wp")

   except Exception:
      print("Web Site Is Down . . .")

###############################################################

if (len(sys.argv) != 3):

     print "\n\n" + 60 * "*"
     print "\n\nPlease Use : wp-user.py -url http://target.com \n"
     print "OR \n"
     print "Please Use : wp-user.py -file target.txt \n"
     print "\n\n" + 60 * "*"

     sys.exit(1)
else:
     method_options = sys.argv[1]
     url = sys.argv[2]

if (method_options == "-url"):
        try:
              print " \n************ Thread Started For [ " + url +" ] ************"
              t1 = threading.Thread(target=wp_login_page, args=[url,])
              t1.start()
        except Exception:
              print "Error: unable to start thread"
elif (method_options == "-file"):
        try:
             lines = [line.rstrip() for line in open(sys.argv[2])]
             for url in lines:

                  print " \n************ Thread Started For [ " + url +" ] ************"
                  wp_login_page(url)


        except Exception:

             print "Error: unable to start thread"

