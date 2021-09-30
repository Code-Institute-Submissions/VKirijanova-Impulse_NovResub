# Impulse #

Story about why this website

# UX #

## Strategy plane ##
The aim of the project is to create an interactive book's library that would be fully responsive on all devices and screens. The 
target will be all aged love readers, so website should be simple to understand and easy to navigate.

## Scope plane ##
The library will be styled in a minimalistic design. It will allow users to log in and log out of app, add books which they already read with full description of the book. Also they can browse through other customers books and find new books. 

## Structure plane ##
The main page will have list of books on the website, entered by all users. User will be able to log in, by pressing login button and view his profile. He will be able to add new books manually with Name of the book, Author, pages, year of publicity and small book description. 

## Skeleton plane ##
All website will be created in same design. The header will be fixed on the top with all required buttons. Extra information about books will be hiden in colapsable card.

The wireframe for mobile phone and desktop will look the same, however mobile version will have hamburger button to hide buttons.
[![mockup.png](https://i.postimg.cc/KvZN5Rb1/mockup.png)](https://postimg.cc/7bW0HPf4)

## Surfuce plane ##
Website designed in yellow colors, to match the theme of the app Books. Background picture is not that bright, however gives the feeling of real live library.

# User Stories: #
1. 

Mockup
[![responsiveness.png](https://i.postimg.cc/MpqYdX8c/responsiveness.png)](https://postimg.cc/PPVZqXJh)

The live version of project you can see [here.](https://virtual-books-library.herokuapp.com/)

# Features #

### Existing features ###
Website has a collapsible books list with extra information about them inside. Have buttons which can Log users in, log them out, add new books, edit books and delete them. New users can register to app and enjoy full library.


### Future features ###
- Users will be able to create their wish list, which will be visible only for them. This way they can safe all book they intereted for future and not loose them in long books list.
- All books will have purchase links, for users to easy find their favorite books online.
- Admin will be only user who will be able to delete books from app, however other users will be able to add books to their profile or wish list.
- As some of input fields have min and max characters, users will see how many charactares must be entered.

# Technology used #
- HTML 
- CSS (the language to style HTML and make bootstrap more individual)
- JavaScript
- jQuery

- Gitpod
- GitHub
- Heroku
- Werkzeug??
- Materialize

- Chrome DevTools
- Jshint
- W3C school
- W3C mark up validation service (to test HTML and CSS)

# Testing #
- HTML tested with W3C mark up validation service. I had some syntax issue only due to jinja template been used to build all pages.
- CSS have been tested with W3C mark up validation service, error been showed:[![Error.png](https://i.postimg.cc/W1nXCm90/Error.png)](https://postimg.cc/Mnn7jBJG). 

After removing shadow from element, no errors was found.

- Javascript code passed in Jshint with no major issues, one undefined variable found - $.
- Project's responsiveness checked on iPhone, Google Chrome, Microsoft Edge and worked perfectly.

# Manual Testing #
Home page have a list of books, already added by users. By clicking on the book name, container collapse down and show extra information about the book. On right side you have Home, Log In and Register button, on mobile version buttons hiding in hamburger button.
Press Log In button it will redirect you to log in page with form which require Username and Password. Both input areas are mandatory and will turn red if left empty. If user will log in wrong username or password, flash message will pop in with message "Incorrect Uername and/or Password". Username and Password have minimum of 5 caracters, which indicates with message "Match the requested format" if you type less than 5. After entering right username and password, press Log In button, it is redirecting user to their profile page.
Press Register button it will redirect to register page with form. Username and Password have minimum of 5 caracters, which indicates with message "Match the requested format" if you type less than 5. After choosing new username and pasword and press Sign Up botton it showed error, studying code in app.py find mistake (right parenthesis was in the wrong place). After fixing mistake and pressing Sign Up button again app was redirected to created user's profile page with flash message "Welcome to our library!". 
When user is logged in their profile following new buttons shows on right side of screen: My Page, Add New Book, Wish List and Log Out. My Page and Wish List is empty page with only Name on it.
Press Add New Book button and it will redirect to form. Form consist of text fields to fill up Book Name, Author, Book Description, Pages, Year of Publishing and Purchase Link, as well as style of books section, where you can choose style of the book. By fill up all field and choosing one book style, press add book. App redirect to Home Page and pop up flsh message on the top "Book Successfully Added to Library.
On home page there is list of all books been added previously. Each book have two buttons "Delete" and "Edit". Press button Delete and it deleting selected book with flash message "Book Succesfully Deleted". Press Edit button and it will redirect you to form with full description of book to edit. Update required field and press button "Edit Book", changes been saved and flash message appearing on the top "Book Successfully Updated".
On right side press button Log Out. It will log user out, redirect to Log In page with flash message "You have been logged out". Buttons "My Page", "Add New Book", "Wish List" and "Log Out" dissapeared, as well "Edit" and "Delete" buttons next to books on Home Screen.

## Testing user stories ##
1. 

### Issues ###


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
2. Go to [Heroku](https://www.heroku.com/), once logged into your dashboard, click ‘Create new app’.
3. Create app name (must be unique, and generally use a 'dash' or 'minus' instead of spaces, and all lowercase letters).
4. Choose region closest to you.
5. Then click ‘Create app’.
6. Setup automatic deployment from your GitHub repository.
7. Double check if your GitHub profile is displayed.
8. Add your repository name and click 'Search'.
9. Once it finds your repo, click 'Connect' to connect to this app.
10. Click on ‘Settings’.
11. Then click ‘Reveal Config Vars’.
12. Then enter the variables (from the env.py) file to securely tell Heroku which variables are required: IP, PORT, MONGO_DBNAME, MONGO_URI, SECRET_KEY.
13. Push requirements.txt and Profile to repository, in terminal, add/commit/push.
14. In [Heroku](https://www.heroku.com/), press ‘Enable Automatic Deployment’ and ‘Deploy Branch’.
15. Once it's done, you'll see ‘Your app was successfully deployed.’ Click ‘View’ to launch your new app.


### Credits ###

### Content ###
1. Background picture been taken from [Unsplash website](https://unsplash.com/)
2. Used to create collapsible nav: https://www.w3schools.com/howto/howto_js_collapsible.asp
3. Classes timetable https://bootsnipp.com/snippets/mME3y


### Acknowledgements ###
My mentor Spencer Barriball for his support.
