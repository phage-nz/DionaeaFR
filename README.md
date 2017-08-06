DionaeaFR
=========

Front Web to Dionaea low-interaction honeypot.  

DionaeaFR Home: https://github.com/phage-nz/DionaeaFR  
Forked from: https://github.com/rubenespadas/DionaeaFR  
Dionaea Home: https://github.com/DinoTools/dionaea  

## Install ##

  Refer to the automated install instructions at https://github.com/phage-nz/malware-hunting/tree/master/honeypot

## Changelog ##

  - Add transport, type and protocol filters in connections table.
  - Add Attacks graph last 7 days.
  
  - **29/11/2012**
	- Add less support
	- Add HTML minify
	- Add menu icons
	- Other visuals changes
	
  - **18/12/2012**  
	- Add home panel

  - **20/12/2012**  
	- Add country name in tooltips
	- Add Top 10 Ports Graph
	- Add ANTIVIRUS_VIRUSTOTAL variable in settings.py
	- Deactive minify by default
	- Restructure directories
	- Fixed Graphs
  
  - **15/05/2013**
    - Refactoring Code
	- New filters system

  - **16/05/2013**  
    - Fixed mysql_command.
    - Add refresh interval in graphs.

  - **04/06/2017**  
    - Fixed URL encoding.

  - **08/06/2017**  
    - Added sample download functionality.
    
  - **06/08/2017**  
    - Made required changes for Django 1.11.x support.

## To-Do ##

  - Make Debug=False the default mode of deployment.
  - Fix sample downloads after Django 1.11.x migration.
