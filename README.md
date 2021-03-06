# Impulse #
Impulse website been created for people who would like to continue or start the active lifestyle in the new gym. Website have all necessary information
about new gym and everything it can offer to new members. 

# UX #

## Strategy plane ##
Website should attract new customers who are 18 years old above. As gym is new all information customer will be getting from this webtsite. Design must be intuitive, which will allow users to navigate and engage with the website without any prior experience .It should be easy in use, especially find necessary information. Pictures should be attractive and clear.  

## Scope plane ##
Website will have navbar which will be devided in two rows, one will have Name of Gym, Member Login Button and Shopping bag. Second row will have collapsible cards: Club overview, Timetable, Club Facilities and Packages. Main page will contain welcome message and Join Us Button.

## Structure plane ##
Users will be able to purchase packages and sign up. Login to their profile and see purchase history. 
There will be 12 packages available to purchase 1 year (full gym, swimming pool only or classes only), 1 month (full gym, swimming pool only or classes only) or 1 day(full gym, swimming pool only or classes only).

## Skeleton plane ##
All website will be created in same design. The header will be fixed on the top with all required buttons. 

The wireframe for mobile phone and desktop will look the same, however mobile version will hide in collapsable button second row of nav bar.
[![GYM.png](https://i.postimg.cc/0yfCjJNS/GYM.png)](https://postimg.cc/tss6mJWR)

## Surfuce plane ##
Colors will be dark on main page, as is the most popular gym has dark theme, however packages will be bright with colorful pictures.

# User Stories: #
1. As a user I would like to register to my peronal account.
2. As a user I would like to login and logout.
3. As a user I would like to receive confirmation email after creating account.
4. As a user I would like to see all packages available.
5. As a user I would like to see details of packages (like price, what included)
6. As a user I would like to see classes and what time they are available.
7. As a user I would like to view the total packages I chose.


The live version of project you can see [here.](https://vkirijanova-impulse.herokuapp.com/)

# Features #

### Existing features ###
Website have buttons which help customers to log in and log out. Next to log in button there is shopping bag, for customer to remind if they choose any packages. Collapsable 4 buttons will describe club, show timetable, facilieties and packages available in the gym. Each package have discription with name, price and buttons to raise or decrease numbers of packages. 


### Future features ###
- There will be certain amount of spaces to classes, so users will be able to save space through their profile.
- Team introduction (coaches)

# Technology used #
- HTML 
- CSS (the language to style HTML and make bootstrap more individual)
- JavaScript
- jQuery

- Gitpod
- GitHub
- Heroku
- Materialize

- Chrome DevTools
- Jshint
- W3C school
- W3C mark up validation service (to test HTML and CSS)

# Testing #
- HTML tested with W3C mark up validation service. I had some syntax issue only due to jinja template been used to build all pages.
- CSS have been tested with W3C mark up validation service 
- Javascript code passed in Jshint with no major issues, one undefined variable found - $.
- Project's responsiveness checked on iPhone, Google Chrome, Microsoft Edge and worked perfectly.

# Manual Testing #
1. Annautorised User: Home page contains of nav bar and main page. In main page under welcoming note there is button 'Join Us', after clicking on it, website will redirect you to page with all packages offered. By clicking button 'Impulse' we are returning to the main page.
Nav bar has main name of page 'Impulse' which redirect you to main page as soon as you press the button. On the right side there are 2 buttons: member login and shopping bag (set to zero). By pressing 'Member Login' dropdown button showing 'Login' button. This button redirect us to page where you can enter your user name and password and log in. 

2. Register: by pressing 'Member Login' dropdown button show 'Login'. This button redirect us to page where there is Sign Up button. It show form with email address, new user name and password. By filling all necessary field, varification email being received. After confirming email I was successfully signed up and redirect to main page.

3. Registerd User: Nav bar has main name of page 'Impulse' which redirect you to main page as soon as I press the button. On the right side there are 3 buttons: member login and shopping bag. By pressing 'Member Login' show dropdown two buttons: My account and Logout. Press button 'My account' it redirect to user's account where he can find his personal details and purchase history. Press button 'Member Login' and choose 'Logout' from dropdown option. Website checking if we want log out, press sign out and website redirecting to main page.

4. Button of nav bar has 4 collapsable card. Pressed Club Overview and it showed short club overview. Pressed Timetable and Timetable showed with classes name and time in particular week day. Pressed Club Facilieties showed three cards with pictures of facilities (main gym, swimming pool and studio). Pressed last button Packages opened new page with all packages we have. 

5. Choosed one of the packages, it opened new page with package picture, name, description and price. +/- button updated number of packages without leaving page. Pressed button add to bag, in bag appeared chosen item an total price been updated. Pressed shopping bag icon on the top right corner. Shopping bag have information about package and total price. Pressed button Secure checkout, redirect to checkout form. Filled out all necessary fields, entered fake card details as per stripe documentation. Pressed complete order. Email been send to terminal and on website showed purchase order.
  

## Testing user stories ##
1. As a user I would like to register to my peronal account.
    User can sign up straight away on the page by pressing button Members Login, then from dropdown button Login and then Sign Up. Second option they could choose package first and there will will be option to sign up before purchasing it. Sign up nitton will direct to the form where new users will have to fill Name, Email Address and Password. 

2. As a user I would like to login and logout.
    User can see Member Login straight after entering website. After pressing button login user will have to enter his user name and password to enter login. Same button Member Login will have dropdown button Sign Out. When user will sign out website will reconfirm if user truly wish to log out.

3. As a user I would like to receive confirmation email after creating account.
    With the help of Google mail, user will receive confirmation after purchasing package or sign in with our website. Confirmation email might take up to 10 minutes to show in email box.

4. As a user I would like to see all packages available.
    By pressing packages on nav bar user will see all packages available along with name and price.

5. As a user I would like to see details of packages (like price, what included)
    As soon a user will click on favorite package, they will have new page opened with all details including price, name and description of package.

6. As a user I would like to see classes and what time they are available.
    User can press button Timetable in nav bar where they will see all available classes, their time and week of the day.

7. As a user I would like to view the total packages which I chose.
    By pressing shopping bag user can see all order, review number and securely purchase package and join gym.

### Issues ###
1. Issue with wevhook handler, especially handle_payment_intent_succeeded. 
2. Pictures are not uploading only on club facilities. Error showing that file cannot be find, but pictures are correctly upload to AWS and are in gitpod media folder. Images dissapear after uploading to AWS, packages some pictures I put back as admin website, but facilities could't find solution.

# Deployment #

### Managing Git ###
1. I then added to my local repo using `git add -A`;
2. And then commit them to my local repo using `git commit -m "message"`;
3. Once that was done I push my local repo to the remote (Github) using `git push`.

### Cloning a repositary ###
If you would like to clone a repositary follow theese steps:
1. Log in on GitHub;
2. Navigate to needed repositary;
3. Above the list of the files, click green button Code;
4. On the dropdown selection, you will find a link to clone the code with HHTPS;
5. Open Git Bash;
6. Open new location where you want to clone repositary;
7. Type git clone, and then paste the URL you copied earlier.
8. Press Enter.

### Heroku deployment ###
1. Setup files which Heroku needs in your terminal:
    - requirements.txt: tells Heroku which applications and dependencies are required to run our app.
    - Procfile: what Heroku looks for to know which file runs the app (use capital P for Procfile, and delete blank line at bottom of Procfile as may cause problems when running on Heroku).
2. Go to [Heroku](https://www.heroku.com/), once logged into your dashboard, click ???Create new app???.
3. Create app name (must be unique, and generally use a 'dash' or 'minus' instead of spaces, and all lowercase letters).
4. Choose region closest to you.
5. Then click ???Create app???.
6. Setup automatic deployment from your GitHub repository.
7. Double check if your GitHub profile is displayed.
8. Add your repository name and click 'Search'.
9. Once it finds your repo, click 'Connect' to connect to this app.
10. Click on ???Settings???.
11. Then click ???Reveal Config Vars???.
12. Then enter the variables (from the env.py) file to securely tell Heroku which variables are required: IP, PORT, MONGO_DBNAME, MONGO_URI, SECRET_KEY.
13. Push requirements.txt and Profile to repository, in terminal, add/commit/push.
14. In [Heroku](https://www.heroku.com/), press ???Enable Automatic Deployment??? and ???Deploy Branch???.
15. Once it's done, you'll see ???Your app was successfully deployed.??? Click ???View??? to launch your new app.


### Credits ###
Main idea and help been taken from Boutique Ado project created by Code Institute

### Content ###
1. Main background picture and package's pictures been taken from [Unsplash website](https://unsplash.com/)
2. To create collapsible nav, I used help from [w3school](https://www.w3schools.com/howto/howto_js_collapsible.asp)
3. To create clases table I used inspiration from [Bootsnipp]{https://bootsnipp.com/snippets/mME3y)
4. To create cards for nav bar I used [w3school]{https://www.w3schools.com/bootstrap4/bootstrap_cards.asp)


### Acknowledgements ###
My mentor Spencer Barriball for his support.
