# SberTroika 2021 hackathon backend

Backend for SberTroika 2021 hackathon.  

## Setup and running
First install all necessary python packages using requirements.txt


```bash
pip install -r requirements.txt
```

Run server:
```bash
python run.py
```
This script will run Flask script on port 8080.

Navigate to url http://127.0.0.1:8080/ in browser.

* /get_overload (POST) - Returns JSOТ with value of overload on river pier.

### Test using curl
To enter url of website to parse
```bash
curl -v -XPOST -H Content-Type:application/json --data '{"location": "Автозаводский мост", "time": "2021-12-21 14:35:36"}' http://127.0.0.1:8080/get_overload 
```
Returns JSON with field overload_value - value of overload on river pier.

Heroku demo: https://sbertroika21-leaderstat-flask.herokuapp.com/.
