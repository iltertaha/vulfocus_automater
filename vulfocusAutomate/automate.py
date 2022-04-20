import parse_args
import sys, os
from src.vulfocus.vulfocusClient import VulfocusClient
import credentials
from datetime import datetime

arguments = parse_args.parse()

imageFileToRead = open(arguments['image-file'], 'r')
nucleiTemplateFileToRead = open(arguments['template-file'], 'r')
sys_path = arguments['working-dir']
output_dir = arguments['output-dir']
VERBOSE = arguments['verbose']


sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
print( "Current directory: "+ os.path.dirname(os.path.realpath(__file__)))


clinet = VulfocusClient(username=credentials.USERNAME,licence=credentials.LICENCE)
images = clinet.get_images()


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
    startedHostWithoutPort = startedHost.split(':')[0]
    startedPorts = startedContainer.port

    # we dont know which port is working for nuclei attack
    # why not try all :D
    for port in startedPorts.values():

        current_time = datetime.now()
        
        ## NUCLEI ATTACK STARTS HERE
        # nucleiCommand = "nuclei -u http://{} -t {} -debug -markdown-export ./nuclei_results".format(startedHostWithoutPort +":"+ port, nucleiLine.strip())
        nucleiCommand = f'nuclei -u http://{startedHostWithoutPort}:{port} -t {nucleiLine.strip()} -debug -markdown-export {output_dir}_{current_time.year}-{current_time.month}-{current_time.day}_{current_time.hour}:{current_time.minute}'
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



