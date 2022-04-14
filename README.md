# Vulfocus Automate v1

Purpose of this repo is to provide a script that allows the containers hosted by Vulfocus to be automatically tested with the nucleus and store the results.

This work is based on  [vulfocus-py](https://github.com/fofapro/vulfocus-py) with modifications and additions.


> Built-in vulfocus package contains deprecated URL. This is
> the updated version. Instead of `pip install vulfocus`, clone this repo.
> It uses modified version of the vulfocus, located under src folder.

##  How to use?
- Clone this repo.
- Make sure you have nucleus installed properly. (This repo uses nucleus command from the current working directory)
- Create vulfocus account from vulfocus.io
- Open `credentials.py` and enter your credentials.
	- To find your licence:
		- login your vulfocus account and switch to account tab(second from the top in the left menu)
		- In the opened page, click the second tab, which will show your email password and **licence***
-  Open `readyToAttackImages.txt`
	- Write an image name of your choice from the vulfocus application on each line.
		> vulfocus/flink-cve_2020_17519:latest

- Open  `readyToAttackNucleiTemplates.txt`
	-	On each line, write the path of an appropriate nucleus template for the vulnerable image you selected.
		> cves/2020/CVE-2020-17519.yaml

 **Notice: For txt files, the entries must have the same order.** 
	(First line of the readyToAttackImages.txt will be used together with the first line of the readyToAttackNucleiTemplates.txt`  )
 
 - Open terminal and change directory to vulfocusAutomate folder.
```bash
  cd vulfocusAutomate
```
- Run automate scrpt.
```bash
  python automate.py 
```
- At the end it will save the logs of the tests under `nuclei_results` folder.
