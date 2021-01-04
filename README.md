# project1-database

<br> The base url is: https://osband-duan-project1-database.herokuapp.com/
<br>
<br> Make sure you have a slash after every url for patch and post requests.
<br> POST users/ creates a new user.
<br> When you POST you must enter a "display_name", a "username", and the "latitude" (float) and
<br> "longitude" (float) of the user's home base is optional and recommended.
<br> GET users/ returns the list of all users with their display_name, username, and user_id.
<br> PATCH users/[user_id]/ allows you to change the user's display_name, username,
<br> and the latitude and longitude of their home base.
<br> DELETE users/[user_id]/ deletes the user linked with user_id.
<br>
<br> POST locations/ creates a new location
<br> When you POST you must enter an "id" (integer), a "place_title", the "address", the "city",
<br> the "state", and the "zip_code" (integer).
<br> Latitude and longitude of the place of interest will be automatically generated.
<br> GET locations/ returns the list of each user and id corresponding to a dictionary of
<br> all locations associated with that user_id. For each location it lists the place_title, latitude, and longitude.
<br> The home base is automatically added as one of the user's pois.
<br> GET [user_id]/poi/ returns the list of poi's associated with that user_id with their
<br> place_title, latitude and longitude.
<br> PATCH locations/[user_id]/[placeTitle]/ allows you to change the locations's place_title, address, city,
<br> state, and zip_code.
<br> DELETE locations/[user_id]/[placeTitle]/ deletes the locations linked with user_id.
