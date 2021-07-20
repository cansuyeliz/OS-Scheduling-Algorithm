import sys

scheduleFile = open("schedule.txt", "r")
scheduleList=[]
for line in scheduleFile:
    line_str=line.split(", ")
    line_str = [element for element in line_str]  
    scheduleList.append(line_str)

for i in range(len(scheduleList)):
    scheduleList[i][1] = int(scheduleList[i][1])
    scheduleList[i][2] = int(scheduleList[i][2])
    scheduleList[i][3] = int(scheduleList[i][3])

def firstComeFirstServed(scheduleList):
    outputFile = open("output.txt", "w")
    scheduleList.sort(key = lambda x: x[1])
    taskNames = []
    arrivalTimes= []
    priorities = []
    cpuBursts = []
    for k in scheduleList:
        taskNames.append(k[0])
        arrivalTimes.append(k[1])
        priorities.append(k[2])
        cpuBursts.append(k[3]) 
    outputFile.write("First Come First Serve Scheduling\n")
    outputFile.write("\n")
    for i in range(len(taskNames)):
        outputFile.write("Will run Name: " + str(taskNames[i]) + "\n")
        outputFile.write("Priority: "+ str(priorities[i]) + "\n")
        outputFile.write("Burst: "+ str(cpuBursts[i]) + "\n")
        outputFile.write("Task "+ str(taskNames[i]) + " is finished\n")
        outputFile.write("\n")
    outputFile.close()   
scheduleFile.close()
# firstComeFirstServed(scheduleList)
scheduleFile = open("schedule.txt", "r")
def priorityScheduling(scheduleList):
    outputFile = open("output.txt", "w")
    scheduleList.sort(key = lambda x: x[1])
    taskNames = []
    arrivalTimes= []
    priorities = []
    cpuBursts = []
    for k in scheduleList:
        taskNames.append(k[0])
        arrivalTimes.append(k[1])
        priorities.append(k[2])
        cpuBursts.append(k[3])
    outputFile.write("Shortest Job First Scheduling\n")
    outputFile.write("\n")
    outputFile.write("Will run Name: " + str(taskNames[0])+"\n")
    outputFile.write("Priority: "+ str(priorities[0])+"\n")
    outputFile.write("Burst: "+ str(cpuBursts[0])+"\n")
    outputFile.write("Task "+ str(taskNames[0]) +" is finished\n")
    outputFile.write("\n")
    outputFile.close()
    outputFile = open("output.txt", "a")
    taskNames.pop(0)
    arrivalTimes.pop(0)
    priorities.pop(0)
    cpuBursts.pop(0)
    scheduleList.pop(0)
    scheduleList.sort(key = lambda x: -x[2])
    for j in scheduleList:
        outputFile.write("Will run Name: "+ str(j[0])+"\n")
        outputFile.write("Priority: "+ str(j[2])+"\n")
        outputFile.write("Burst: "+ str(j[3])+"\n")
        outputFile.write("Task "+ str(j[0])+ " is finished\n")
        outputFile.write("\n")
    outputFile.close()    
scheduleFile.close()
#priorityScheduling(scheduleList)
scheduleFile = open("schedule.txt", "r")
def shortestJobFirst(scheduleList):
    outputFile = open("output.txt", "w")
    scheduleList.sort(key = lambda x: x[1])
    taskNames = []
    arrivalTimes= []
    priorities = []
    cpuBursts = []
    for k in scheduleList:
        taskNames.append(k[0])
        arrivalTimes.append(k[1])
        priorities.append(k[2])
        cpuBursts.append(k[3])
    outputFile.write("Shortest Job First Scheduling\n")
    outputFile.write("\n")
    outputFile.write("Will run Name: " + str(taskNames[0])+"\n")
    outputFile.write("Priority: "+ str(priorities[0])+"\n")
    outputFile.write("Burst: "+ str(cpuBursts[0])+"\n")
    outputFile.write("Task "+ str(taskNames[0]) +" is finished\n")
    outputFile.write("\n")
    outputFile.close()
    outputFile = open("output.txt", "a")
    taskNames.pop(0)
    arrivalTimes.pop(0)
    priorities.pop(0)
    cpuBursts.pop(0)
    scheduleList.pop(0)
    scheduleList.sort(key = lambda x: x[3])
    for j in scheduleList:
        outputFile.write("Will run Name: "+ str(j[0])+"\n")
        outputFile.write("Priority: "+ str(j[2])+"\n")
        outputFile.write("Burst: "+ str(j[3])+"\n")
        outputFile.write("Task "+ str(j[0])+ " is finished\n")
        outputFile.write("\n")
    outputFile.close()    
scheduleFile.close()
#shortestJobFirst(scheduleList)
scheduleFile = open("schedule.txt", "r")
def roundRobin(scheduleList):
    outputFile = open("output.txt", "w")
    scheduleList.sort(key = lambda x: x[1])
    taskNames = []
    arrivalTimes= []
    priorities = []
    cpuBursts = []
    for k in scheduleList:
        taskNames.append(k[0])
        arrivalTimes.append(k[1])
        priorities.append(k[2])
        cpuBursts.append(k[3]) 
    quantum = 10
    time = 0
    outputFile.write("Round Robin Scheduling\n")
    outputFile.write("\n")
    while (1):
        done = True
        for i in range(len(cpuBursts)):
            if cpuBursts[i] > 0:
                done = False
                if cpuBursts[i] > quantum:
                    time = time + quantum
                    cpuBursts[i] = cpuBursts[i] - quantum
                    outputFile.write("Will run Name: " + str(taskNames[i]) + "\n")
                    outputFile.write("Priority: "+ str(priorities[i]) + "\n")
                    outputFile.write("Burst: "+ str(cpuBursts[i]) + "\n")
                    outputFile.write("\n")
                else:
                    time = time + cpuBursts[i]
                    cpuBursts[i] = 0
                    outputFile.write("Will run Name: " + str(taskNames[i]) + "\n")
                    outputFile.write("Priority: "+ str(priorities[i]) + "\n")
                    outputFile.write("Burst: "+ str(cpuBursts[i]) + "\n")
                    outputFile.write("Task "+ str(taskNames[i]) + " is finished\n")
                    outputFile.write("\n")

        if done == True:
            break
    outputFile.close()    
scheduleFile.close()
#roundRobin(scheduleList)
scheduleFile = open("schedule.txt", "r")
def priorityWithRoundRobin(scheduleList):
    outputFile = open("output.txt", "w")
    scheduleList.sort(key = lambda x: -x[2])
    taskNames = []
    arrivalTimes= []
    priorities = []
    cpuBursts = []
    for k in scheduleList:
        taskNames.append(k[0])
        arrivalTimes.append(k[1])
        priorities.append(k[2])
        cpuBursts.append(k[3])
    outputFile.write("Priority with Round Robin Scheduling\n")
    outputFile.write("\n")
    for j in priorities:
        if priorities.count(j) > 1:
            quantum = 10
            time = 0
            while (1):
                done = True
                if cpuBursts[priorities.index(j)] > 0:
                    done = False
                    if cpuBursts[priorities.index(j)] > quantum:
                        time = time + quantum
                        cpuBursts[priorities.index(j)] = cpuBursts[priorities.index(j)] - quantum
                        outputFile.write("Will run Name: "+ str(taskNames[priorities.index(j)]) + "\n")
                        outputFile.write("Priority: " + str(priorities[priorities.index(j)]) + "\n")
                        outputFile.write("Burst: "+ str(cpuBursts[priorities.index(j)])+ "\n")
                        outputFile.write("\n")
                    else:
                        time = time + cpuBursts[priorities.index(j)]
                        cpuBursts[priorities.index(j)] = 0
                        outputFile.write("Will run Name: "+ str(taskNames[priorities.index(j)]) + "\n")
                        outputFile.write("Priority: "+  str(priorities[priorities.index(j)]) + "\n")
                        outputFile.write("Burst: "+ str(cpuBursts[priorities.index(j)]) + "\n")
                        outputFile.write("Task "+ str(taskNames[priorities.index(j)])+ " is finished\n")
                        outputFile.write("\n")

                if done == True:
                    break 
        else:
            outputFile.write("Will run Name: "+ str(taskNames[priorities.index(j)]) + "\n")
            outputFile.write("Priority: "+ str(priorities[priorities.index(j)]) + "\n")
            outputFile.write("Burst: "+ str(cpuBursts[priorities.index(j)]) + "\n")
            outputFile.write("Task "+ str(taskNames[priorities.index(j)])+ " is finished\n")
            outputFile.write("\n")
    outputFile.close()                       
scheduleFile.close()
#priorityWithRoundRobin(scheduleList)
if sys.argv[2] == "schedule.txt":
    if sys.argv[1] == "fcfs":
        firstComeFirstServed(scheduleList)
    elif sys.argv[1] == "sjf":
        shortestJobFirst(scheduleList)
    elif sys.argv[1] == "pri":
        priorityScheduling(scheduleList)
    elif sys.argv[1] == "rr":
        roundRobin(scheduleList)
    elif sys.argv[1] == "pri-rr":
        priorityWithRoundRobin(scheduleList)
    else:
        print("The algorithm doesn't exist.")
else:
    print("The file doesn't exist.")  










    
 
    
