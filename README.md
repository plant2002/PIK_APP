TO DO:
- [ ]	Make sure it's bulletproof (after presentation, such as that date_from is earlier than date_to, fn_from smaller than fn_to etc)
- [ ]	get the code cleaned up
- [ ]	connect GUI to functions
- [ ]	show graphs in GUI Analysis
- [ ]	change GUI Analysis
- [x]	create a Jupyter notebook with analysis + export in it
- [x]	PowerPoint presentation
- [x]	added client, company, helicopter tables to database
- [x]	client login/register
- [x]	company login/register
- [ ]	add new helicopter GUI + queries
- [ ]	how to make sure it's only one guy adding helicopters for the x company?
- [x]	how do I link new VEMD .csv to a helicopter that doesn't exist yet (maybe open a new window if I find a FN that isn't yet in the database???)
- [ ]	how do you transfer/delete helicopters from x company to y company?

Analysis: 
- [ ]	make analysis bulletproof
Analysis:

-graphs + writings
	- [ ]	flight time per aircraft (FTAircrafts)
	- [ ]	flight time per aircraft per date (from/to) (FTAircraft)
	- [ ]	errors in last month (write down)
	- [ ]	errors per aircraft (maximum coloured) 1w, 2w, 4w
	- [ ]	errors per aircraft per day (1w, 2w, 4w,...), all aircraft
	- [ ]	aircrafts with x error in the last 1w, 2w, 4w,...
	- [ ]	error occurrence per 1w/2w/4w/6m (all aircraft in company)
		-	average --> OUTLIERS COLOURED (1w,2w,4w + choose 1s,2s, 3s)
		(use all available data for averaging + gauss)
	- [ ]	errors per flight time 1w, 2w, 4w for one aircraft
	- [ ]	engine cycles per aircraft per day 1w, 2w, 4w
	- [ ]	error occurrence per no. of engine cycles
		- [ ]	one helicopter
		- [ ]	all your helicopters
		(add a line of averages)
	- [ ]	number of overlimits per flight for 1w, 2w, 4w
		-one helicopter compared to average?
-exports
	- [ ]	heli register number -> export data for:
		1d, 2d, 5d, 1w, 2w, 4w,...
	- [ ]	all heli with x error in last 1w, 2w, 4w
	- [ ]	all graphs??? for visual presentation
	- [ ]	all heli exceeding averages-> 1s, 2s, 4s--> for error/overlimit
	
-	Basic functions:
- [x] cleaning up CSV 
- [x] database 
- [x] connecting DB to python 
- [x] main page of GUI 
- [x] GUI is okay now 
- [x] GUI connect to other frames works okay, all in one file though (GUI2.py) since the links weren't working as they should in multiple files.
- [x] Clean up GUI_2
- [x] uploading csv files to a folder 'uploads' 
- [x] importing into DB (all works and gets inserted. Failures only when a new code is detected)
- [x] moving csv after it was processed
- [x] reimporting works and rewrites the rows in the database

https://www.figma.com/file/sVt59DgmlymZQrweML1bTM/Pik-app?type=design&node-id=36-27&mode=design&t=1rqOvimrYzFkVntX-0 tkdesigner notes:
