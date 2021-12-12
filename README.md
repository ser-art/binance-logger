# Binance SMA logger

## How to build and start 
- Open config/settings.yaml file and configure the app
- `docker-compose up --build` - standart mode
- `docker-compose up --build -d` - detached mode, check logs in the file

## Where to find logs?
logs/sma_logs file gonna have all logging info, it connects to the folder inside docker container 

## Unit testing
- Start `. test.sh`
