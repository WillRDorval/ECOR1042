"""
Submission by T099

William Dorval 101187466
Raunaq Hoqie 101180524
Chaelan Murray 101180990
Mohammad Saud 101195172

Submitted on: 
"""

from T099_interactive_ui import command
from Cimpl import choose_file, load_image, copy, create_color, set_color, show, Image, save_as, get_color, create_image

filename = "batch_sample.txt"
batch_file = open(filename)

for line in batch_file:
    items = line.split(" ")
    for i in range(len(items)):
        items[i] = items[i].rstrip()
        
    filter_list = []
    for i in range(2, len(items)):
        filter_list.append(items[i])
    
    current_image = load_image(items[0])
    for filter_entry in filter_list:
        new_image = command(filter_entry, current_image)
        current_image = copy(new_image)
        
    final_image_name = items[1]
    save_as(current_image, final_image_name)
    show(current_image)
        
    
    