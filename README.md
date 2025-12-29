TO DO:
- [ ]	Make sure it's bulletproof 
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

### Analysis: 
- [ ]	make analysis bulletproof
- [ ]	connect analysis with GUI
- [ ]	check the imported data right away and see if they are outliers and there is a problem (error window?)

### Graphs & Writings

- [x] Flight time per aircraft (FTAircrafts)
- [x] Flight time per aircraft per date (from/to) (FTAircraft)
- [x] Errors in last month (written analysis)
- [x] Errors per aircraft (maximum coloured) – 1w, 2w, 4w
- [x] Errors per aircraft per day – 1w, 2w, 4w (all aircraft)
- [ ] Aircraft with X error in the last 1w, 2w, 4w
- [ ] Error occurrence per 1w / 2w / 4w / 6m (all aircraft in company)
  - Average (Gaussian)
  - Outliers coloured (1σ, 2σ, 3σ)
  - Uses all available data for averaging
- [ ] Errors per flight time – 1w, 2w, 4w (one aircraft)
- [ ] Engine cycles per aircraft per day – 1w, 2w, 4w
- [ ] Error occurrence per number of engine cycles
  - [ ] One helicopter
  - [ ] All helicopters
  - Includes average line
- [ ] Number of overlimits per flight – 1w, 2w, 4w
  - One helicopter compared to company average

### Exports

- [ ] Export by helicopter register number:
  - 1d, 2d, 5d, 1w, 2w, 4w
- [ ] All helicopters with X error in last 1w, 2w, 4w
- [ ] All graphs for visual presentation
- [ ] Helicopters exceeding averages (1σ, 2σ, 4σ) for error / overlimit



### Basic functions:
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
