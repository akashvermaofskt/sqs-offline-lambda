# sqs-offline-lambda
# run: npm install
## Execute this steps in home directory (package.json)
Step 1:
docker-compose -f ./docker/docker-compose.yml up -d

Step 2:
sls offline start 

Step 3 (In another terminal):
sls invoke local -f start-lambda
