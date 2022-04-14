import os

VERBOSE = False

from src.vulfocus.vulfocusClient import VulfocusClient
import credentials
clinet = VulfocusClient(username=credentials.USERNAME,licence=credentials.LICENCE)
images = clinet.get_images()

imageFileToRead = open('./readyToAttackImages.txt', 'r')
nucleiTemplateFileToRead = open('./readyToAttackNucleiTemplates.txt', 'r')

if(VERBOSE):
    print(images)

count = 0
while True:
    count += 1
 
    # Get next line from both files
    imageLine = imageFileToRead.readline()
    nucleiLine =  nucleiTemplateFileToRead.readline()
 
    # if line is empty
    # end of file is reached
    if not imageLine:
        break
    print("Starting image name: {} nuclei attack: {}".format(imageLine.strip(), nucleiLine.strip()))

    ## START CONTAINER
    startedContainer = clinet.start_container(imageLine)
    if(VERBOSE):
        print(startedContainer)
    startedHost = startedContainer.host
    stertedHostWithoutPort = startedHost.split(':')[0]
    startedPorts = startedContainer.port

    # we dont know which port is working for nuclei attack
    # why not try all :D
    for port in startedPorts.values():
        
        ## NUCLEI ATTACK STARTS HERE
        nucleiCommand = "sudo nuclei -u http://{} -t {} -debug -markdown-export ./nuclei_results".format(stertedHostWithoutPort +":"+ port, nucleiLine.strip())
        cwd = os.path.dirname(os.path.realpath(__file__))

        print("Switching to current working directory")
        commandResult1 = os.system("cd "+cwd)
        
        print("Running nuclei attack with port: {} :D Hope it will find something.".format(port))
        try:
            commandResult2 = os.system(nucleiCommand)
        except:
            print("Failed to execute nuclei command")
        ## NUCLEI ATTACK ENDS HERE

        ## STOP AND DELETE CONTAINER
        #print(clinet.stop_container(imageLine))
        #print(clinet.delete_container(imageLine))



