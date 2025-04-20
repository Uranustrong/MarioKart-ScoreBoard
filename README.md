# What is this ?
This is a documentation about how to set up the score-borad webserver for MarioKart
# How to use ?
## For ones with ntucsiebigfight gmail account
- Set up environment
```bash=
git clone <url>
cd MarioKart-ScoreBoard
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip && pip install -r requirement.txt
chmod +x ./run-server.sh
```
- Get the API key

Go to the Google Cloud Console

Login as `ntucsiebigfight`

Click the Navigation menu at left upper corner

Go to IAM & Admin > Service Accounts > Choose the first email listed in it > Keys > Add key

Jason key file will be automatically downloaded to your local machine

Add the content to file `mariokart_credential`
- Run server
```
./run-server.sh
```
- Open web browserx
Type `http://localhost:4000/#<A/B>-<M/L><x>` to access 
A: 競賽組
B: 休閒組
M: 一般賽
L: 敗部賽
x: 比賽編號
eg: 競賽組一般賽第一場 > `http://localhost:4000/#A-M1`
### Note: 
- In Google Sheet, you need to have respective sheet for server to get match infomation.
- You can type `ctrl-c` to stop the server.
- If you want to change the web for different match, just modify the sub-directory of url. Say, change #A-M1 to #A-M2 to access the second match's infomation
- If you found the web is not refreshing, you can try to manually refresh it to apply changes.
# Acknowlegment
Thanks to b10 王勻學長 provides this code
# Reference:
- https://file.wang.works/share/ol1Uq67J