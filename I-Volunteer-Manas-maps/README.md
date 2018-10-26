# I-Volunteer
# Microsoft Codefundo++
Connectivity (cellular/internet) becomes increasingly difficult or disrupted when disasters hit any area. This project aims effectively store and utilize the audio data received from ham operators at ground zero to enhance the rescue operations through the web application. Received audio is stored and processed using wave and scipy package and converted to text using Azure speech to text convertor. Natural language processing(NLP) is performed on text to extract information like location where people are stranded, road destroyed, new routes for walking etc. Using this information, we will update the issue on a route blockage dashboard on website. Along with updation , we will add a marker on Google maps according to the blocking address and type of blockage. This information will be used to plan on where to send rescue teams, how many to send and the best routes to evacuate people. Google map will also show how many people are stranded at the affected locations.
Dashboard also has contact number of relief camps, real time status of how many people are there at camps, number of people who require urgent medical treatment, amount of food and medical supplies required etc. (from information obtained from ham operators and volunteers).