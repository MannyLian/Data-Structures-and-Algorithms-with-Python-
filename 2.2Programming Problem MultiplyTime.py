"""
Conduct an experiment to prove that the product of two numbers does not depend
on the size of the two numbers being multiplied. Write a program that plots the
results of multiplying numbers of various sizes together. HINT: To get a good
reading you may want to do more than one of these multiplications and time
them as a group since a multiplication happens pretty quickly in a computer.
Verify that it truly is a O(1) operation. Do you see any anomalies? It might be
explained by Python’s support of large integers. What is the cutoff point for
handling multiplications in constant time? Why? Write a program that produces
an XML file with your results in the format given in this chapter. Then visualize
your results with the PlotData.py program provided in this chapter.
"""

import datetime
import random
import time

def main():

    file = open("MultiplyTimeTest.xml","w")

    file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')

    file.write('<Plot title="Average Multiply Time">\n')


    xList = []
    yList = []
    mList = []
    for e10 in range(1,20):
        xmin = 10**e10
        xmax = 10**(e10+1)

        xList.append(e10+1)
        factor1list = []
        factor2list = []
        for x in range(100000):
            factor1 = random.randint(xmin, xmax)
            factor1list.append(factor1)

            factor2 = random.randint(xmin, xmax)
            factor2list.append(factor2)
        starttime = datetime.datetime.now()

        for index in range(100000):
            mList.append(factor1list[index] * factor2list[index])

        endtime = datetime.datetime.now()

        deltaT = endtime - starttime

        averageTime = deltaT.total_seconds() /100000 * 1000000

        yList.append(averageTime)

    file.write('    <Axes>\n')
    file.write('        <XAxis min="'+str(10)+'" max="'+str(xmax)+'">Factor Size</XAxis>\n')
    file.write('        <YAxis min="'+str(min(yList))+'" max="'+str(100)+'">Microseconds</YAxis>\n')
    file.write('    </Axes>\n')

    file.write('    <Sequence title="Average Access Time vs Factor Size" color="red">\n')

    for i in range(len(xList)):
        file.write('    <DataPoint x="'+str(xList[i])+'" y="'+str(yList[i])+'"/>\n')
    file.write('    </Sequence>\n')
    file.write('</Plot>\n')
    file.close()


if __name__ == "__main__":
    main()