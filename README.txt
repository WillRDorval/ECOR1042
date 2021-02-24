ECOR1052 Winter 2021 README for Milestone Project Version 1.0 26/02/2021

The project can be reached at:
Voice: 613 520 2600
Website: https://github.com/WillRDorval/ECOR1042
Email: mohammadsaud@cmail.carleton.ca

Description:
------------

- The project contains two programs, the first is the interactive ui which will prompt the user to load an image. The user can then select a filter or multiple 
filters to apply to the image. You can now save your images with the applied filters. If you try to use the filters without loading an image a “No image loaded”
 error message will appear.
- For the edge dection filter a threshold will need to be entered.
- The batch user interface program, it will prompt the user for the name of a batch file. The program will read the contents in the image file and it will perform 
image manipulations that were present in the file. Afterwards it will save the results.

- The project is made up of 2 files:
    T099_interactive_ui        A Python script
    T099_batch_ui              A Python script 


Installations:
-------------- 

Python 3.9 or later must be installed
Pillow 20.3.3 or later must be intsalled
sys module must be loaded
T099_image_filters must be loaded
Cimpl must be loaded

Usage:
------

After running the program, you will need to load an image. To do so enter,
	"L"

This will prompt you to select an image from your desktop. Once selected, you can choose a filter to apply onto it. To do so enter the first letter of the filter 
mentioned in the interactive UI. Afterwards, your image with the filter will be shown.

Lastly, to save your image, you will need to enter,
	"S"

You may then choose to load the save image again to add another filter on to it. To exit from the program, just enter,
	"Q"

Credits:
--------
William Dorval - Recorded as author of T099_interactive_ui
Mohammad Saud - Recorded as author of T099_batch_ui


Copyright 2021 Chaelan Murray and Raunaq Hoque