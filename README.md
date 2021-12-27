# order-book-tracker
Order Book Tracker Service

Service fetches data every 5 seconds and writes to transactions table as well as creating a day based record on Statistics table. It updates the daily record continuously. 


Tech Stack:
Django, Postgres, Celery, Docker, Docker-Compose


API views shows daily, weekly and monthly resolutions.
Weekly and monthly resolutions also shows min, max and avg of the weeks and months.

API endpoints described as below:
GET http://127.0.0.1:8000/api/bookstatistics/btctry/daily/

Returns the record belongs to current day. It contains last 24 hours data.


GET http://127.0.0.1:8000/api/bookstatistics/btctry/weekly/

Returns the record belongs to last 7 days.


GET http://127.0.0.1:8000/api/bookstatistics/btctry/monthly/

Returns the record belongs to last 30 days.

How to run:
1- Run docker-compose up --build