# Sounding-Table-Project
By: Christopher Andersen

I was selected to cadet ship with Crowley on the oil tanker MV California transporting Alaskan crude oil up and down the West Coast. One of the duties on the ship every morning was to record the sounding numbers (measurement of the liquid level in a tank (cm)). This included sounding 4 waste oil tanks, each with different shapes and volumes. I noticed our sounded volume values were fluctuating too much for what is a reasonable margin of error. Multiple values spanning weeks were 1-2 cubic meters off of the expected value of the tank. These sounded values served as a spot check for the computers on the ship to make sure the computer values were accurate as an overflow of these tanks could lead to millions of dollars in fines. Some of these tanks were only designed to carry 12 cubic meters of oil so a measurement being off could lead to disaster. 

These values were calculated using different variables: the sounded value of the tank (gathered using a sounding tape with a weighted bob at the end), the ship’s trim (normally angled 2-5 meters astern which leads to a vastly different sounded volume if unaccounted for), and the sounding tables (benchmark with 5 cm increments listing every volume per 5 cm from +5 meters to -1 meter of trim (1 meter increment)). I realized the issue causing the volume values to be inaccurate was the shape of the tank. At the top and bottom, the walls were curved which led to an exponential change in volume; so it was impossible to get accurate values if the equation used to calculate the volume was linear. After realizing this, I wrote a fourier series for each tank with the values given in the sounding table as discrete inputs to create an equation for the volume. I mirrored the equation around the endpoint to make a continuous periodic function, only looking at the position between x=0 and x=½ of the period to gather data. After writing one of these fourier series, I realized solving the problem this way would be unsustainable as the equation took more than two pages. 

I decided to take a different approach, instead writing an equation applicable to all tanks listed below and use the sounding table data as an input. I took advantage of the tank’s continuity and its sloped edges by taking the aggregate slope per centimeter between the 5 cm increments given by the sounding table, with an input for the ship’s trim as a volume scalar. I checked my equation’s values against the sounding table and the actual values given by the ship's volume measurement system. It was within a hundredth of a cubic meter of both values. I wrote this equation and the data from the sounding tables into Python. After installing the program on the ship’s computer, any engineer in the future can select the tank they want the volume of, input the value from the sounding tape, input the ship’s trim, and a volume will be calculated. No arithmetic required. 

My solution saves the engineers of that ship 30 minutes every morning not spent doing arithmetic, or correcting mathematical errors. Over the projected lifespan of the ship, it will save engineers 5840 hours they can spend doing something more important than algebra.

Sounding table equation:

![Sounding table equation](/images/IMG_0107.jpg "Sounding table equation")


Variables:
HI_HT: Volume of the sounded innage rounded to the next highest innage value on the sounding table at the actual trim rounded to the next highest degree

HI_0: Volume of the sounded innage rounded to the next highest innage value on the sounding table at 0 degrees of trim

HI: Sounded innage rounded to the next highest innage value on the sounding table

HT: Actual trim rounded to the next highest degree

ST: Actual trim of the ship

LI_HT: Volume of the sounded innage rounded to the next lowest innage value on the sounding table at the actual trim rounded to the next highest degree

LI_0: Volume of the sounded innage rounded to the next lowest innage value on the sounding table, 0 degrees of trim

LI: Sounded innage rounded to the next lowest innage value on the sounding table

SV: Measurement taken from the sounding tape

Example of sounding table:

![Sounding table](/images/Sounding-table.png "Sounding table")
