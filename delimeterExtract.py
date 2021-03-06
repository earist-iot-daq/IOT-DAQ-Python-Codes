"""
String Manipulation
v1.0 - Original file, delimiter ',', no code for compromising control characters.
"""

dataArray = []

def extractData(extract):
    count = 0
    previousCount = 0
 #   print('aasasaasa')
    for x in extract:
        count = count + 1
        if (x == ','):
            dataArray.append(extract[previousCount:count - 1])
            previousCount = count
        
        if(count == len(extract)):
            dataArray.append(extract[previousCount:len(extract)])
            
        

dataLimit = 0
while dataLimit < 1:
    dataLimit = dataLimit + 1
    data = input('Input Data: ')
    extractData(data)

print('Done!')
