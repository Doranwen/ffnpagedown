# Description
This is a simple Python script that automates the process of using PageDown to autoload all pages of a fandom on [Fanfiction.net](https://www.fanfiction.net/).  The results can then be processed with a link grabbing extension to get a list of all story links on those pages.

# Backstory / Personal Note
Full confession: I do not generally consider myself a programmer since I have no time to learn and forget what I do learn due to lack of use.  However, a few years ago I used [pyautogui](https://pyautogui.readthedocs.io/en/latest/) to create a simple macro script for personal use.  It occurred to me that I could tweak that to make it automate hitting the PageDown button when loading all pages of a fandom on Fanfiction.net, so I fiddled with it and in short order had it working.

# Before using
Instructions below work on Linux; you may need to adjust for your own OS.

## Get script

### Using git
Run:
```
git clone https://github.com/Doranwen/ffnpagedown.git
```

### Downloading manually
Go to to the top of this page and click the Code button, then choose Download Zip.

## Set up script environment
Run each command one by one:
```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
To exit the script environment, run `deactivate`.

# Running the script
1) Install an extension that allows you to auto-load each page of story results on Fanfiction.net. (As far as I know, only [Fanfiction Tools on Firefox](https://addons.mozilla.org/en-US/firefox/addon/fanfiction-tools/) does this.  If there's a Chrome extension with that feature, please create an Issue to ask me to add the link to it!)
2) (Optional) Install [Link Gopher for Firefox](https://addons.mozilla.org/en-US/firefox/addon/link-gopher/).  This will enable you to grab all links when you are done.
3) Activate Fanfiction Tools on the page of filters you want on Fanfiction.net.  Take note of how many total pages it has.
4) Open a terminal window to the ffnpagedown folder.
5) Make sure the terminal window is in front of the browser, and that your mouse is on either the minimize button OR the window for the terminal in the taskbar.
6) Run the following commands, one by one:
```
source venv/bin/activate
python3 ffnpagedown.py
```

The script will ask you to input the number of pages for that fandom.  Once you do that and hit enter, it will minimize the terminal window and begin hitting Page Down for you.

When it has finished, check that all pages have loaded by pressing PageDown manually until you see the bottom of the page.

# (Optional) Extract links
1) Click on the Link Gopher button on the Firefox toolbar.
2) Choose "Extract Links by Filter".
3) Type `/1/` in the box and click OK.
4) Select the entire page (Ctrl + A).
5) Copy/paste it into a text file.
6) Remove the top and bottom links (which appear on every page of links).

What's left should be the full list of story links.

# Tips
Before running the script, disable any popups that may steal window focus.

