# DevClubWebScraping

## Installation
*(Tested on python 3.8.5)*  
*Create a virtual environment (Optional)*  
pip install -r requirements.txt (Windows)  
pip3 install -r requirements.txt (Linux/Mac)  
Download and extract chromedriver from https://chromedriver.chromium.org/downloads  
*Must have chrome*
## Moodle Auto-Login
Edit the PATH variable inside moodleLogin.py and set it to chromedriver.exe  
run using  
python ./Moodle/moodleLogin.py (Windows)  
python3 ./Moodle/moodleLogin.py (Linux/Mac)  
Enter username and password. Password should be hidden.

## Codeforces
cd Codeforces  
python fetch_round.py [round number] (Windows)  
python3 fetch_round.py [round number] (Linux/Mac)
