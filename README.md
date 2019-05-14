# Website visualizer
![wikipedialandscape](https://raw.githubusercontent.com/SnowballAntrobus/A3_P2/master/landscape.jpg)
## Background for the second project of ARTV3
    python3 everything.py [url]
It takes a website url and generates an image procedurally.<br>
Very good for wikipedia, but most other popular websites (facebook, twitter , etc) are mostly JS so it wont work as well.<br>
Also, I rushed this, so it's not the most organized code (modular, etc).

### How to Run:
I'm gonna assume you are on Mac. The parts under the instructions you paste into terminal.<br>
1. Get homebrew
    > /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
2. Get Python 3
    > brew install python3
3. Get Pillow
    > pip3 install Pillow
4. Get Beautiful Soup 4
    > pip3 install beautifulsoup4
5. Get Selenium
    > pip3 install selenium
6. Go to Safari and in the help menu look for **Allow Remote Automation** and press enter when it comes up
7. Get git
    > brew install git
8. Go to desktop
    > cd Desktop
9. Get files
    > git clone https://github.com/SnowballAntrobus/A3_P2.git
10. Go to new folder
    > cd A3_P2
11. Run code (I'm using an example URL you can use any URL)
    > python3 everything.py https://en.wikipedia.org/wiki/Earth
12. The image should open in preview and save to landscape.jpg in the A3_P2 folder
