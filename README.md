# HackerRank Scrapper

This repo is a scrapper to get my own solutions of HackerRank problems and to save them to my github repo.

This scrapper uses Python Selenium.

## Usage

Change the variables in the py file as shown

<pre>
challenge_list_url = 'www.hackerrank.com/url_to_challenge_list'
tutorial_name      = 'name-of-tutorial'
extension          = 'the extension of your programming language'
path_to_driver     = 'path_to_your_webdriver'
</pre>

Create a credentials.py file with the variables username and password.

## Example

<pre>
challenge_list_url = 'https://www.hackerrank.com/domains/tutorials/30-days-of-code?filters%5Bstatus%5D%5B%5D=solved&filters%5Bsubdomains%5D%5B%5D=30-days-of-code&badge_type=30-days-of-code'
tutorial_name      = '30-days-of-code-cpp'
extension          = 'cpp'
path_to_driver     = 'chromedriver_linux64/chromedriver'
</pre>

credentials.py
<pre>
username='my-user'
password='my-password'
</pre>

then just go into terminal and
<pre>
$python3 scrapper.py
</pre>
