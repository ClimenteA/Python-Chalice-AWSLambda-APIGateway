# Python AWS Serverless API (Example)
A CRUD serverless small api built with AWS Chalice, AWS Functions and MongoDB Atlas.

- This api fetches json product data from a given URL;
- Does some cleaning and validation of the data fetched;
- Saves the cleaned data in MongoDB Atlas and saves images to a AWS S3 bucket;
- Fetches saved data and images from MongoDB Atlas and S3 bucket;
- Deletes the product data from MongoDB


# Quickstart

- Clone repo;
- Install dependencies: `pipenv install`;
- Boot-up virtualenv: `pipenv shell`;
- Move in chalice code files: `cd api-intent`;
- Start local dev. server: `chalice local`;
- Add other python packages if needed: ex: `pipenv install pandas`;
- After a new package install, run: `pipenv lock -r > requirements.txt` (this way the packages will be installed in AWS lambda also);
- Deploy to AWS: `chalice deploy`;
- See AWS link: `chalice url`;
- Delete API from AWS: `chalice delete`;


**Prerequisites**

- AWS, MongoDB Atlas accounts;
- AWS Console installed and with credentials configured;
- HTTPIE for manual testing endpoints;


Testing was made manually with [httpie](https://httpie.io) and automated with pytest, [requests](https://requests.readthedocs.io/en/master/) and [assertpy](https://github.com/assertpy/assertpy).


# API

Api can be used at `/products` with URL specified in the body.

URL="https://raw.githubusercontent.com/ClimenteA/Python-Chalice-AWSLambda-APIGateway/main/retailer-data.json"

