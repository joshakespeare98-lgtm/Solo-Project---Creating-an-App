**What is needed in the app?**

* new user (username and password)
* two separate lists. One being active users and the other being disabled users. Both these list should be shown.
* be able to move a user from active to disabled or the other way around
* test a login - either print "access granted" or "access denied"
* save users to a csv file

**Structuring the data**

* each user is a dictionary with two keys.

Eg. username: Jake, Password: password

* users stored in two python lists:

Eg. active\_users = \[]      disabled\_users = \[]

**List of functions I need to create:**

* add\_user() #ask for username and password, add dictionary to active\_users
* view\_users() #print both lists to the screen
* disable\_user() #find user in active\_users, move them to disabled\_users
* enable\_user() #find user in disabled\_users, move them to active\_users
* test\_login() #ask for username and password, check against active\_users, print result
* save\_users() #write both lists to users.csv
* load\_users() #read users.csv on startup and fill both lists

**Menu options:**

1. add user
2. view active and disabled users
3. disable a user
4. enable a user
5. test login
6. exit

**File list (keeping functions on separate file):**

* main.py - use this to run the menu loop and import functions from user\_manager.py
* user\_manager.py - all the functions and active and disabled user lists
* users.csv - this should be created automatically when you add a user

**Basic flow**

Start - load users() - show menu - user picks option - run  function - save if needed - repeat - exit

**Possible things to do**

* add users before submitting. Eg. add a user for each account type.
