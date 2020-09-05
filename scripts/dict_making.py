#!/usr/bin/env python3

import os
import re
import random
import jsonpickle
import json

my_dict = {}       # aprox mem consumpton   150 Mb of trimmed subs requires 5 Gb RAM for hashing

#trimmed subs. Each name is youtube ID ! w/o extections !
source_dir = '/home/d/pikkerConstilation/test'		 #don't put / at the end

id_list = os.listdir(source_dir)

print(f'source_dir\'s got {len(id_list)} files in it')

#for instance from 00:00:45 to N secs
def time_converter(time):
	time = time.split(':')
	time_in_seconds = int(time[0])*3600 + int(time[1])*60 + int(time[2])  
	if time_in_seconds > 10:
		time_in_seconds = time_in_seconds - 7 

	return str(time_in_seconds)


for n in range(len(id_list)):

	text = open(f'{source_dir}/{id_list[n]}')

	for line in text:
		
		time_sample = line[:8]
		
		if line[:2].isdigit() == False:  #all string should beging with time sample
			continue		
		
		#build a link for youtube video
		link_for_youtube = f'{id_list[n]}?t{time_converter(time_sample)}'.split(' ')
		
		#build a link to the line of text so we won't store the same line multiple times
		#link_for_dict = 

		#the line that will be one of the values to the keys which is ecencially words it contains
		splited_line = line[9:].split()

		#check if a substring begins with a letter
		try:
			if_letter = bool(re.match('[a-z]', splited_line[0].lower()))
		except IndexError:
			if_letter = False

		if if_letter:  
			for word in splited_line:
				word = word.lower()
				key_value = link_for_youtube + splited_line

				my_dict.setdefault(word, [])
				my_dict[word].append(key_value)

#print(id_list[1])
	print(len(my_dict))



#trim values to leave only N number values to each key
def value_numbers_trimmer(N):	#haven't used it inside the iteration to have as much random results as possibe. In other case most of the worlds would be linked to the first videos
	for key in my_dict:
		values = my_dict[key]
		if len(values) > N:
			my_dict[key] = random.sample(my_dict[key], N)

value_numbers_trimmer(50)

print(my_dict['for'])

#my_dict.clear()

print(my_dict)


def write_dictionary():
	#Create a file for my_dict
	my_dict_context = os.path.join('/home/d/pikkerConstilation/test', 'my_dict.json')
	if not os.path.exists('/home/d/pikkerConstilation'):
		os.makedirs('/home/d/pikkerConstilation')

	with open(my_dict_context, 'w') as json_file:
		encoded = jsonpickle.encode(my_dict)
		json.dump(encoded, json_file) 

#jsonpickle.decode(the_encoded_object, keys=True)


write_dictionary()


#return json.loads(jsonpickle.encode(result, unpicklable=False)) 

        # filename = os.path.join(user_config_dir(), 'Child_QTable.json')
        # with open(filename, 'w') as json_file:
        #     encoded_dictionary = jsonpickle.encode(dictionary)
        #     json.dump(encoded_dictionary, json_file) 

# def write_dictionary(self):
#         """
#         Writes the QTABLE configuration to the QTable.json file.
#         """
#         config_dir = user_config_dir()
#         filename = os.path.join(config_dir, 'QTable.json')
#         to_save_var = {
#             "environment": self.environment,
#             "qtable": self.qtable,
#             "providers_offers": self.providers_offers,
#             "self_state": self.self_state,
#             "tree": self.tree
#         }
#         with open(filename, 'w') as json_file:
#             encoded_to_save_var = jsonpickle.encode(to_save_var)
#             json.dump(encoded_to_save_var, json_file) 




















# #print from a dict to a file

# fout = "/your/outfile/here.txt"
# fo = open(fout, "w")

# for k, v in yourDictionary.items():
#     fo.write(str(k) + ' >>> '+ str(v) + '\n\n')

# fo.close()

















