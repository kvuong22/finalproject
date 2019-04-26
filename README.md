# Cherry Blossom Sites in Japan
Kim Vuong

[Link to this repository](https://github.com/kvuong22/finalproject)

---

## Project Description

This project will scrape cherry blossom sites and bloom dates from https://www.japan-guide.com/e/e2011_where.html and use that data along with data on the area location and area type of the cherry blossom sites from the CSV file ('site_area_data.csv') to create a database. The database is then used to be queried for the designated flask routes (noted below) to visualize the data through a web browser. The flask app will provide users a list of locations to see cherry blossom trees bloom in Japan. This includes the sites and the area, area type, and the estimated bloom time frame for each site. The user can enter in an area and if the database contains that area, it will display a list of the location sites from input area. If the area is not in the database, it will let the user know the area is not in the database and to try searching for another area. The user will also be able to see the extensive list of all sites with their corresponding area, area type, and bloom dates provided by the database.

## How to Run the Files

1. First, you should install all requirements with 'pip install -r requirements.txt', ideally in a virtual environment.
2. Second, you should run in your terminal 'python SI507project_tools'.
3. Third, you should run in your terminal 'python app.py runserver'. Access the webpage either by using 1) the generated URL in the command prompt: http://127.0.0.1:5000/ or by using the URL link 2) http://localhost:5000/ and paste it into the browser.

## Using Flask Application

1. After accessing the home page from Step 3 of how to run the files, the user can either use the buttons at the bottom of the pages to navigate the flask app or the user can manually type in the URL with the routes listed below. Please note when searching for an area, you will need to manually type in the area in the URL field after 'the search/' and the first letter must be capitalized. Screenshots are all in the repository folder screenshots and are referred to below.
2. Upon loading the home page from step 3 of how to run the files, you should see a pop up box like the one in screenshot_homepage1.png.
3. Once you click OK, you should see the home page looking like screenshot_homepage2.png.
4. The main search page will tell you to manually input the area of interest in the URL and to capitalize the first letter, which looks like screenshot_search_main.png.
5. When you input an area that is in the database, it will return the sites like in screenshot_search_kyoto.png with the example of inputting "Kyoto". If it is an invalid input, one that is not in the database, you will see something like screenshot_invalidsearch.png
6. When viewing all sites in the database, it should look like screenshot_all_site_info.png

## Routes in this application
- `/` -> this is the home page
- `/search/` -> this route is the main search page that reminds the user to manually input the area of interest after 'search/'
- `/search/<area>` -> this route for user input where <area> is and to check with the database for sites
- `/all_site_info` -> this route is where all data from the database is listed

## How to run tests
1. First, access the directory that contains all the files listed as in this repository below.
2. Second, run 'python SI507project_tests.py'.


## In this repository:
- screenshots
  - screenshot_all_site_info
  - screenshot_homepage1
  - screenshot_homepage2
  - screenshot_invalidsearch
  - screenshot_search_kyoto
  - screenshot_search_main
- templates
  - all_sites.html
  - home_page.html
  - invalid_input.html
  - search_area.html
- README.md
- SI507project_tests.py
- SI507project_tools.py
- advanced_expiry_caching.py
- app.py
- database_schema_diagram.png
- db_populate.py
- japanblooms_cache.json
- requirements.txt
- site_area_data.csv


---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [x] This is a completed requirement.
- [ ] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [ ] Project is submitted as a Github repository
- [x] Project includes a working Flask application that runs locally on a computer
- [x] Project includes at least 1 test suite file with reasonable tests in it.
- [x] Includes a `requirements.txt` file containing all required modules to run program
- [x] Includes a clear and readable README.md that follows this template
- [x] Includes a sample .sqlite/.db file
- [x] Includes a diagram of your database schema
- [x] Includes EVERY file needed in order to run the project
- [x] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [x] Includes at least 3 different routes
- [x] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [x] Interactions with a database that has at least 2 tables
- [x] At least 1 relationship between 2 tables in database
- [x] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [ ] Use of a new module
- [ ] Use of a second new module
- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [ ] A many-to-many relationship in your database structure
- [ ] At least one form in your Flask application
- [x] Templating in your Flask application
- [x] Inclusion of JavaScript files in the application **Please note JavaScript is located in the same file as the html templates**
- [x] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [x] Sourcing of data using web scraping
- [ ] Sourcing of data using web REST API requests
- [x] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [x] Caching of data you continually retrieve from the internet in some way

### Submission
- [x] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [x] I included a summary of my project and how I thought it went **in my Canvas submission**!
