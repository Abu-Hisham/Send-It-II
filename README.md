[![Build Status](https://travis-ci.org/Abu-Hisham/Send-It-II.svg?branch=master)](https://travis-ci.org/Abu-Hisham/Send-It-II)

[![Coverage Status](https://coveralls.io/repos/github/Abu-Hisham/Send-It-II/badge.svg?branch=develop)](https://coveralls.io/github/Abu-Hisham/Send-It-II?branch=develop)

# **SEND-IT APPLICATION**

## Description

An application that enables users to deliver parcels to their recipients in different regions. This is users by senders making parcel delivery orders through the system which will in turn trigger a notification on the other end of the intended recipient. The logistics of how the parcel is to be delivered to their respective destinations remain the sole mandate of the staff of the holding company guided through the information provided by the system.

## Technologies Used

The system is authored using python's flask framework for the backend services and the frontend is powered by a JavaScript framework React/AngularJS.

The Database is built using PostgreSQL 

## Links to Any Related Projects or References

<https://abu-hisham.github.io/send-it/>

<https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way>

https://dzone.com/articles/restful-web-services-with-python-flask

## Installation Instructions

1. Clone the repository locally git clone 

   ```
   git https://github.com/Abu-Hisham/Send-It-II.git
   ```

2. create a virtual environment ( You need to have virtualenv installed)

   ```
   virtualenv venv
   ```

3. install project dependencies/ requirements

   ```
   pip install -r requirements.txt
   ```

4. Activate the virtual environment

   ```
   venv\scripts\activate
   ```

5. Set flask environment variables

   ```
   setx FLASK_APP run.py
   
   setx APP_SETTINGS development
   ```

6. Run the project by firing the below command

   ```
   flask run
   ```
