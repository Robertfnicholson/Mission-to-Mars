# Import splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
import selenium
from webdriver_manager.chrome import ChromeDriverManager


# Add a function that will
# 1Initialize the browser.
# 2 Create a data dictionary.
# 3 End the WebDriver and return the scraped data.
#  define this function as "scrape_all" and then initiate the browser.
def scrape_all():
    # # Set up Splinter
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # Next, we're going to set our news title and paragraph variables (remember, this function will return two values)
    # This line of code tells Python that we'll be using our mars_news function to pull this data.
    news_title, news_paragraph = mars_news(browser)

    # Now that we have our browser ready for work, we need to create the data dictionary. Add the following code
    # to our scrape_all() function:
    # Run all scraping functions and store results in dictionary
    # This dictionary does two things: It runs all of the functions we've created—featured_image(browser),
    # for example—and it also stores all of the results. When we create the HTML template, we'll create paths
    # to the dictionary's values, which lets us present our data on our template. We're also adding the date
    # the code was run last by adding "last_modified": dt.datetime.now(). For this line to work correctly,
    # we'll also need to add import datetime as dt to our imported dependencies at the beginning of our code.
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now()
    }
    # Stop webdriver and return data
    browser.quit()
    return data

# Refactor the scrape news code
# create a function called mars_news
# Begin the function by defining it, then indent the code as needed to adhere to function syntax.
# Instead of having our title and paragraph printed within the function, we want to return them from the function
# so they can be used outside of it. We'll adjust our code to do so by deleting news_title and news_p and include
# them in the return statement instead
# We also need to add an argument to the function: def mars_news(browser):
# We're going to add a try and except clause addressing AttributeErrors. By adding this error handling, we are
# able to continue with our other scraping portions even if this one doesn't work.
# we're going to add the try portion right before the scraping:
# After adding the try portion of our error handling, we need to add the except part. After these lines,
# we'll immediately add the following:
#     except AttributeError:
#         return None, None
# By adding try: just before scraping, we're telling Python to look for these elements. If there's an error,
# Python will continue to run the remainder of the code. If it runs into an AttributeError, however, instead of
# returning the title and paragraph, Python will return nothing instead.
def mars_news(browser):

    # Scrape Mars News
    # Visit the mars nasa news site
    url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    return news_title, news_p

# ## JPL Space Images Featured Images
# Refactor the above function code to scrap the featured images
# The code to scrape the featured image will be updated in almost the exact same way we just updated the mars_news
# section. We will:
# 1. Declare and define our function.
# def featured_image(browser):
# 2. Remove print statement(s) and return them instead.
# In our Jupyter Notebook version of the code, we printed the results of our scraping by simply stating the variable
# (e.g., after assigning data to the img_url variable, we simply put img_url on the next line to view the data).
# We still want to view the data output in our Python script, but we want to see it at the end of our function
# instead of within it.
# return img_url
# 3. Add error handling for AttributeError.
# try:
#    # find the relative image url
#    img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
#
# except AttributeError:
#    return None
def featured_image(browser):
    # Visit URL
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'

    return img_url

# ## Mars Facts
# Update Mars facts table in a similar manner to the above function updates. This time, though, we'll be adding
# BaseException to our except block for error handling. A BaseException is a little bit of a catchall when it
# comes to error handling. It is raised when any of the built-in exceptions are encountered and it won't handle
# any user-defined exceptions. We're using it here because we're using Pandas' read_html() function to pull data,
# instead of scraping with BeautifulSoup and Splinter. The data is returned a little differently and can result
# in errors other than AttributeErrors, which is what we've been addressing so far.
# Let's first define our function:
# def mars_facts():
# Next, we'll update our code by adding the try and except block.
#   try:
#       # use 'read_html" to scrape the facts table into a dataframe
#       df = pd.read_html('https://galaxyfacts-mars.com')[0]
#    except BaseException:
#       return None
# The code to assign columns and set the index of the DataFrame will remain the same, so the last update we need
# to complete for this function is to add the return statement.
#    return df.to_html()

# We want the table from the website https://galaxyfacts-mars.com/
def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)

    # Convert dataframe back to HTML, add bootstrap
    return df.to_html(classes="table table-striped")

if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())






