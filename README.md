# naftbike
Slovnaft bike web scraper, for data analysis

<h1>Milestones</h1>
<h2>1. Milestone</h2>

Loading the web site to the local variables

<h2>2. Milestone</h2>
Data are persistently updating in our database - this step includes a cron job.

<h2>3. Milestone</h2>
Architecture is capable of providing reasonable fast response to a request. For instance, if aggregation query takes a 15min on 6 months old data => something is wrong. This have to be tested properly on generated data!

<h2>4. Milestone</h2>
Application provides dummy REST-API implementation (GET requests for whole tables)

<h2>5. Milestone</h2>
Application provides smart REST-API for "aggregated" queries (only GET requests; parameters would be maybe name/id/latitude|longitude of station, hours, days of week, months, etc.) 

<h2>6. Milestone</h2>
Dummy frontend in (probably) Vue.js, consuming REST-API and showing simple dashboard

<h2>7. Milestone</h2>
Frontend is capable of visualizing all RESP-API endpoints.
