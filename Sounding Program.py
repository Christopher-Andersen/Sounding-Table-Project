# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 09:24:35 2023

@author: Chris Andersen
"""
options = ['SEP. BILGE OIL T.', 'BILGE HOLDING T.',
           'PURIF. SLUDGE T.', 'F.O. DRAIN T.']
tankSounded = ''
inputMessage = "Pick a tank:\n"

for index, item in enumerate(options):
    inputMessage += f'{index+1}) {item}\n'

inputMessage += 'Your choice (type 1, 2, 3, or 4): '

while tankSounded not in map(str, range(1, len(options) + 1)):
    tankSounded = input(inputMessage)
soundedValue = float(input('Input the sounded measurement of the tank: '))
shipsTrim = float(input('Input the ships trim from ICMS: '))
highInnage = ''
lowInnage = ''
highTrim = ''
highInnage_highTrim = ''
highInnage_0Trim = ''
lowInnage_highTrim = ''
lowInnage_0Trim = ''

# Tank sounding logic for SEP. BILGE OIL TANK
if int(tankSounded) == 1:
    if 0 <= float(soundedValue) <= 5:
        highInnage = 5
        lowInnage = 0
        highInnage_0Trim = 0.1
        lowInnage_0Trim = 0

        if 0 <= float(shipsTrim) <= 1:
            highTrim = 1
            highInnage_highTrim = 0.2
            lowInnage_highTrim = 0
            
        elif 1 < float(shipsTrim) <= 2:
            highTrim = 2
            highInnage_highTrim = 0.2
            lowInnage_highTrim = 0.1

        elif 2 < float(shipsTrim) <= 3:
            highTrim = 3
            highInnage_highTrim = 0.2
            lowInnage_highTrim = 0.1

        elif 3 < float(shipsTrim) <= 4:
            highTrim = 4
            highInnage_highTrim = 0.2
            lowInnage_highTrim = 0.1

        elif 4 < float(shipsTrim) <= 5:
            highTrim = 5
            highInnage_highTrim = 0.2
            lowInnage_highTrim = 0.1

    elif 5 < float(soundedValue) <= 10:
        highInnage = 10
        lowInnage = 5
        highInnage_0Trim = 0.3
        lowInnage_0Trim = 0.1

        if 0 <= float(shipsTrim) <= 1:
            highTrim = 1
            highInnage_highTrim = 0.3
            lowInnage_highTrim = 0.2

        elif 1 < float(shipsTrim) <= 2:
            highTrim = 2
            highInnage_highTrim = 0.3
            lowInnage_highTrim = 0.2

        elif 2 < float(shipsTrim) <= 3:
            highTrim = 3
            highInnage_highTrim = 0.3
            lowInnage_highTrim = 0.2

        elif 3 < float(shipsTrim) <= 4:
            highTrim = 4
            highInnage_highTrim = 0.4
            lowInnage_highTrim = 0.2

        elif 4 < float(shipsTrim) <= 5:
            highTrim = 5
            highInnage_highTrim = 0.4
            lowInnage_highTrim = 0.2
    elif 10 < float(soundedValue) <= 15:
        highInnage = 15
        lowInnage = 10
        highInnage_0Trim = 0.5
        lowInnage_0Trim = 0.3

        if 0 <= float(shipsTrim) <= 1:
            highTrim = 1
            highInnage_highTrim = 0.5
            lowInnage_highTrim = 0.3

        elif 1 < float(shipsTrim) <= 2:
            highTrim = 2
            highInnage_highTrim = 0.5
            lowInnage_highTrim = 0.3

        elif 2 < float(shipsTrim) <= 3:
            highTrim = 3
            highInnage_highTrim = 0.5
            lowInnage_highTrim = 0.3

        elif 3 < float(shipsTrim) <= 4:
            highTrim = 4
            highInnage_highTrim = 0.6
            lowInnage_highTrim = 0.4

        elif 4 < float(shipsTrim) <= 5:
            highTrim = 5
            highInnage_highTrim = 0.6
            lowInnage_highTrim = 0.4

    elif 15 < float(soundedValue) <= 20:
        highInnage = 20
        lowInnage = 15
        highInnage_0Trim = 0.7
        lowInnage_0Trim = 0.5

        if 0 <= float(shipsTrim) <= 1:
            highTrim = 1
            highInnage_highTrim = 0.7
            lowInnage_highTrim = 0.5

        elif 1 < float(shipsTrim) <= 2:
            highTrim = 2
            highInnage_highTrim = 0.8
            lowInnage_highTrim = 0.5

        elif 2 < float(shipsTrim) <= 3:
            highTrim = 3
            highInnage_highTrim = 0.8
            lowInnage_highTrim = 0.5

        elif 3 < float(shipsTrim) <= 4:
            highTrim = 4
            highInnage_highTrim = 0.8
            lowInnage_highTrim = 0.6

        elif 4 < float(shipsTrim) <= 5:
            highTrim = 5
            highInnage_highTrim = 0.8
            lowInnage_highTrim = 0.6

    elif 20 < float(soundedValue) <= 25:
        highInnage = 25
        lowInnage = 20
        highInnage_0Trim = 1.0
        lowInnage_0Trim = 0.7

        if 0 <= float(shipsTrim) <= 1:
            highTrim = 1
            highInnage_highTrim = 1.0
            lowInnage_highTrim = 0.7

        elif 1 < float(shipsTrim) <= 2:
            highTrim = 2
            highInnage_highTrim = 1.0
            lowInnage_highTrim = 0.7

        elif 2 < float(shipsTrim) <= 3:
            highTrim = 3
            highInnage_highTrim = 1.0
            lowInnage_highTrim = 0.8

        elif 3 < float(shipsTrim) <= 4:
            highTrim = 4
            highInnage_highTrim = 1.1
            lowInnage_highTrim = 0.8

        elif 4 < float(shipsTrim) <= 5:
            highTrim = 5
            highInnage_highTrim = 1.1
            lowInnage_highTrim = 0.8

    elif 25 < float(soundedValue) <= 30:
        highInnage = 30
        lowInnage = 25
        highInnage_0Trim = 1.2
        lowInnage_0Trim = 1.0

        if 0 <= float(shipsTrim) <= 1:
            highTrim = 1
            highInnage_highTrim = 1.3
            lowInnage_highTrim = 1.0

        elif 1 < float(shipsTrim) <= 2:
            highTrim = 2
            highInnage_highTrim = 1.3
            lowInnage_highTrim = 1.0

        elif 2 < float(shipsTrim) <= 3:
            highTrim = 3
            highInnage_highTrim = 1.3
            lowInnage_highTrim = 1.0

        elif 3 < float(shipsTrim) <= 4:
            highTrim = 4
            highInnage_highTrim = 1.3
            lowInnage_highTrim = 1.1

        elif 4 < float(shipsTrim) <= 5:
            highTrim = 5
            highInnage_highTrim = 1.4
            lowInnage_highTrim = 1.1

    elif 30 < float(soundedValue) <= 35:
        highInnage = 35
        lowInnage = 30
        highInnage_0Trim = 1.5
        lowInnage_0Trim = 1.2

        if 0 <= float(shipsTrim) <= 1:
            highTrim = 1
            highInnage_highTrim = 1.5
            lowInnage_highTrim = 1.3

        elif 1 < float(shipsTrim) <= 2:
            highTrim = 2
            highInnage_highTrim = 1.6
            lowInnage_highTrim = 1.3

        elif 2 < float(shipsTrim) <= 3:
            highTrim = 3
            highInnage_highTrim = 1.6
            lowInnage_highTrim = 1.3

        elif 3 < float(shipsTrim) <= 4:
            highTrim = 4
            highInnage_highTrim = 1.6
            lowInnage_highTrim = 1.3

        elif 4 < float(shipsTrim) <= 5:
            highTrim = 5
            highInnage_highTrim = 1.7
            lowInnage_highTrim = 1.4

    elif 35 < float(soundedValue) <= 40:
        highInnage = 40
        lowInnage = 35
        highInnage_0Trim = 1.8
        lowInnage_0Trim = 1.5

        if 0 <= float(shipsTrim) <= 1:
            highTrim = 1
            highInnage_highTrim = 1.9
            lowInnage_highTrim = 1.5

        elif 1 < float(shipsTrim) <= 2:
            highTrim = 2
            highInnage_highTrim = 1.9
            lowInnage_highTrim = 1.6

        elif 2 < float(shipsTrim) <= 3:
            highTrim = 3
            highInnage_highTrim = 1.9
            lowInnage_highTrim = 1.6

        elif 3 < float(shipsTrim) <= 4:
            highTrim = 4
            highInnage_highTrim = 2.0
            lowInnage_highTrim = 1.6

        elif 4 < float(shipsTrim) <= 5:
            highTrim = 5
            highInnage_highTrim = 2.0
            lowInnage_highTrim = 1.7

    elif 40 < float(soundedValue) <= 45:
        highInnage = 45
        lowInnage = 40
        highInnage_0Trim = 2.2
        lowInnage_0Trim = 1.8

        if 0 <= float(shipsTrim) <= 1:
            highTrim = 1
            highInnage_highTrim = 2.2
            lowInnage_highTrim = 1.9

        elif 1 < float(shipsTrim) <= 2:
            highTrim = 2
            highInnage_highTrim = 2.2
            lowInnage_highTrim = 1.9

        elif 2 < float(shipsTrim) <= 3:
            highTrim = 3
            highInnage_highTrim = 2.3
            lowInnage_highTrim = 1.9

        elif 3 < float(shipsTrim) <= 4:
            highTrim = 4
            highInnage_highTrim = 2.3
            lowInnage_highTrim = 2.0

        elif 4 < float(shipsTrim) <= 5:
            highTrim = 5
            highInnage_highTrim = 2.3
            lowInnage_highTrim = 2.0

    elif 45 < float(soundedValue) <= 50:
        highInnage = 50
        lowInnage = 45
        highInnage_0Trim = 2.5
        lowInnage_0Trim = 2.2

        if 0 <= float(shipsTrim) <= 1:
            highTrim = 1
            highInnage_highTrim = 2.5
            lowInnage_highTrim = 2.2

        elif 1 < float(shipsTrim) <= 2:
            highTrim = 2
            highInnage_highTrim = 2.6
            lowInnage_highTrim = 2.2

        elif 2 < float(shipsTrim) <= 3:
            highTrim = 3
            highInnage_highTrim = 2.6
            lowInnage_highTrim = 2.3

        elif 3 < float(shipsTrim) <= 4:
            highTrim = 4
            highInnage_highTrim = 2.6
            lowInnage_highTrim = 2.3

        elif 4 < float(shipsTrim) <= 5:
            highTrim = 5
            highInnage_highTrim = 2.7
            lowInnage_highTrim = 2.3

    elif 50 < float(soundedValue) <= 55:
        highInnage = 55
        lowInnage = 50
        highInnage_0Trim = 2.9
        lowInnage_0Trim = 2.5

        if 0 <= float(shipsTrim) <= 1:
            highTrim = 1
            highInnage_highTrim = 2.9
            lowInnage_highTrim = 2.5

        elif 1 < float(shipsTrim) <= 2:
            highTrim = 2
            highInnage_highTrim = 2.9
            lowInnage_highTrim = 2.6

        elif 2 < float(shipsTrim) <= 3:
            highTrim = 3
            highInnage_highTrim = 3.0
            lowInnage_highTrim = 2.6

        elif 3 < float(shipsTrim) <= 4:
            highTrim = 4
            highInnage_highTrim = 3.0
            lowInnage_highTrim = 2.6

        elif 4 < float(shipsTrim) <= 5:
            highTrim = 5
            highInnage_highTrim = 3.1
            lowInnage_highTrim = 2.7

    elif 55 < float(soundedValue) <= 60:
        highInnage = 60
        lowInnage = 55
        highInnage_0Trim = 3.3
        lowInnage_0Trim = 2.9

        if 0 <= float(shipsTrim) <= 1:
            highTrim = 1
            highInnage_highTrim = 3.3
            lowInnage_highTrim = 2.9

        elif 1 < float(shipsTrim) <= 2:
            highTrim = 2
            highInnage_highTrim = 3.3
            lowInnage_highTrim = 2.9

        elif 2 < float(shipsTrim) <= 3:
            highTrim = 3
            highInnage_highTrim = 3.4
            lowInnage_highTrim = 3.0

        elif 3 < float(shipsTrim) <= 4:
            highTrim = 4
            highInnage_highTrim = 3.4
            lowInnage_highTrim = 3.0

        elif 4 < float(shipsTrim) <= 5:
            highTrim = 5
            highInnage_highTrim = 3.4
            lowInnage_highTrim = 3.1

    elif 60 < float(soundedValue) <= 65:
        highInnage = 65
        lowInnage = 60
        highInnage_0Trim = 3.6
        lowInnage_0Trim = 3.3

        if 0 <= float(shipsTrim) <= 1:
            highTrim = 1
            highInnage_highTrim = 3.7
            lowInnage_highTrim = 3.3

        elif 1 < float(shipsTrim) <= 2:
            highTrim = 2
            highInnage_highTrim = 3.7
            lowInnage_highTrim = 3.3

        elif 2 < float(shipsTrim) <= 3:
            highTrim = 3
            highInnage_highTrim = 3.7
            lowInnage_highTrim = 3.4

        elif 3 < float(shipsTrim) <= 4:
            highTrim = 4
            highInnage_highTrim = 3.8
            lowInnage_highTrim = 3.4

        elif 4 < float(shipsTrim) <= 5:
            highTrim = 5
            highInnage_highTrim = 3.8
            lowInnage_highTrim = 3.4
# Sounding equation            
correctedVolume = ((((((highInnage_highTrim - highInnage_0Trim) / highTrim) *
                  shipsTrim) + highInnage_0Trim) / highInnage - ((((lowInnage_highTrim -
                  lowInnage_0Trim) / highTrim) * shipsTrim) + lowInnage_0Trim) / lowInnage) /
                  (highInnage - lowInnage) * (soundedValue - lowInnage) + (((((lowInnage_highTrim -
                  lowInnage_0Trim) / highTrim) * shipsTrim) + lowInnage_0Trim) / lowInnage)) * soundedValue
print('The corrected volume of the tank is ' + str(correctedVolume))
