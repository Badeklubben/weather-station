# Inf142M1

First mandatory assignment in inf142

Team members:

	- Gard Kalland
	- Østen Edvardsen
	- Stian Munkejord
	- Oskar Michalski
	- Lars Bysheim

Some Information:

We have built a program collecting data from three fictional weather stations. The weather stations "reads" the weather and transfers it to one of two storages. Using our web-page, a client can access data from both of the storages.
The "README.png" is from an older version, but it still shows how it is all connected.

Some of the files are nearly duplicates and best commented in "Storage_Bergen_Karmøy" and "Weather_Station_Bergen" 

					----Running----

On Windows:

	1. Run "start.py"
	2. Run "website-start.py"
	3. Go to "localhost:5000"

On others:

	1. Run "tcp_server.py" and "udp_server.py" in both of the storage folders
	2. Run "tcp_client.py" in all three of the weather_station folders (try to start them as close to eachother as possible for higher realism)
	3. Run "web-server.py" in FMI/webserver/
	4. Go to "localhost:5000"


If you want to try it in a terminal just follow the above steps, but instead of "web-server.py" you should run "udp_client.py" in the FMI folder.
The commands:

	1. help
	2. {location name}		- returns the average for each day at this location
	3. {location name} {(1-31)} 	- returns data for each hour of the chosen day and location

Locations = bergen,karmøy and oslo

					----Extensions----

1. sqlite:

We created a sqlite database called "weather-data.db" and placed it in both of the storages. The db holds a single table called "WEATHER" with 6 coloumns: 

	1. id (autoincrementing, mostly there for debugging)
	2. location
	3. day (day of the month)
	4. month
	5. temperature
	6. rain
	
When the storage tcp_server recives this data it executes a line of SQL, inserting it into the db.
The udp_server fetches a piece of that db based on the client command.
Using a sqlite database made it easy to fetch the wanted data without having to loop through all the data on each client request.

Since we are collecting data from a simulation and not real weather data, we can not restart the program without clearing the database. The "station.py" script starts over from May 1. 00:00 every time we restart, and we dont want duplicated data. That is why, when we start running the tcp_servers, we clear out the database.

NB:
We have had no problem with this, but
if should experience a problem with duplicated data (ex: two May 2. or 48 hour in a day), try this:

	1. Shut down everything
	2. Download and run "DB BROWSER FOR SQLITE"
	3. Open the weather-data.db in db browser. 
	4. Execute the file "clear.sql" in the "Execute SQL" tab
	5. Do this with both the database files and try running it again.

This was a problem, but it has never happened to any of us after we fixed it. However, if it does happen to you, this is the way we fixed it then.
	
2. flask:

