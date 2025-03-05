Install Serverless Framework
npm install -g serverless

Initialize a new Serverless project
serverless create --template aws-python

Install the plugin to run functions locally
npm install serverless-offline --save-dev

Installa Json
npm init -y

deploy the function
serverless offline

we try in the terminal or in the browse
curl "http://localhost:3000/dev/hello?name=Nicolas"
