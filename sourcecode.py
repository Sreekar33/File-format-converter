#file converter form csv to  any of the follwoing formats
# can convert to the follwing types gexf,gml,pickle,graphML,YAML,LEDA,SparseGraph6,Palek,GisShapefile,
#!/usr/bin/python
import csv
import xlsx2csv as X
import networkx as nx 
import sys
import os.path
import pickle



#function1-----start!
def add_attributes_to_nodes(G,rj,nodes_coloumn,att_name,att_values):
#this function adds attribute_name atrribute of each node to that node.The attribute has the value atrribute_value
	a=att_name
	vars()[a]=att_name

	G.add_node(rj[nodes_coloumn],attr_dict={att_name:att_values})	
	#adding the node to the graph with attribute
#funciton1 -----end!




#function2-----start!
def add_attributes_to_edges(G,rj,nodes_coloumn,edges_coloumn,att_name,attr_values):
	#this fucntion adds edge atrribute at a time 
	a=att_name
	vars()[a]=att_name
	splited_edges_coloumn=rj[edges_coloumn].split(",")
	#split the edge column w.r.t "," so that we can add each edge again with the required attibutes 
	splited_edges_atttributes=attr_values.split(",")
	#read the above atrributes 
	for i in range(0,len(splited_edges_coloumn)):
		#this loop the edges are added with there corresonding atrribute in the tuple------
		G.add_edge(rj[nodes_coloumn],splited_edges_coloumn[i],attr_dict={att_name:splited_edges_atttributes[i]})
	#adding the node to the graph with attribute
#function2-----end!





#start1----------file format INPUT--BLOCK------#
print("\n\n                                   WELCOME ")
print("\nThe following  File Formats are accpeted here as input and output  \nINPUT FILE TYPES:csv , xlsx ,  gexf , gml , pickle , graphML,YAML , LEDA , SparseGraph6 , Pajek , GISShapefile\nOUTPUT FILE TYPES: csv , gexf , gml , pickle , graphML , YAML , SparseGraph6 , Pajek , GISShapefile\n\nNOTE:-case sensitive.\nyou can only get [csv] as output if you enter [xlsx] file as input \n")
accepted_input_type_set= ['gexf','gml','pickle','graphML','YAML','LEDA','SparseGraph6','Pajek','GISShapefile','csv','xlsx']
#defining a set the set has all the file formats the programs accepts
program_output_file_type= ['csv','gexf','gml','pickle','graphML','YAML','SparseGraph6','Pajek','GISShapefile']
#defining a set the set has all the formats the program can output
input_file_in_set_bool_value= False
 #the variable is used bccause to check the file foemats the programs accepts in  input formats set  is the file format is present the reteurn value is True .initialised to false because to enter the while loop
output_file_in_set_bool_value=False
#same as the abouve reason 
while(input_file_in_set_bool_value!=True):  #run the loop until we get correct input  -----------------------------------csn use try and catch 
	input_file_type = raw_input("Enter the input file format type: \n")
	#asking the user to enter the input file format and putting in the varaible
	input_file_in_set_bool_value= input_file_type in accepted_input_type_set
	#if the input file format given by the user is in the accpeted format set.The value of the vari able is changetd to true and the while loop stopos
	if(input_file_in_set_bool_value==False):
		print("The file format is not accpetable or you entered a inccorect format please enter a file format again\n")
		#if the file format is nor accpetable the ask the user to enter again
while(output_file_in_set_bool_value!=True): #run the loop until we get the correct input
	output_file_type = raw_input("Enter the output file format:\n")
	#--------------------------------can use try and catch
	#taking the output file extension the user want to change
	output_file_in_set_bool_value=output_file_type in program_output_file_type
	#if the input file format given by the user is in the program output  format set.The value of the varible is changetd to true and the while loop stopos
	if(output_file_in_set_bool_value==False):
		print("The file format is not accpetable or you entered a inccorect format please enter a file format again\n")
		#if the file format is nor accpetable the ask the user to enter again
#end1-----------file format Input block ------#


#start2-----------input output file paths block-----#
while(True):
#while(True): #run the loop until we get correct file path
	file_path=raw_input("Enter the input file path:\n")
	splitter=file_path.split(".")

	#take the inpu t file path in this variable
	if(os.path.isfile(file_path)==True and splitter[1]==input_file_type):#os.path.isfile checks the files existence 
		print("\nFile path exixts\nAnd type is compactible....continue\n")  #checks the file path existtence in the directrey .if the path exists then exit the loop with a message or else print the error message and execuate the while loop again
		break
	else :
		print("\nFile doesnt exits or not compactable with input file type please try again \n")
	
output_file_path=raw_input("Now enter the output file path:\n") 

#end2-------------input output file paths block-----#

 


#start3------------xlsx to csv first -----#
if(input_file_type=='xlsx' and output_file_type != 'csv'):
	#if the nput file is xlsx then we convert that fiel i nto a csv file and then we follow the as usal csv converter for tht
	converted_csv_file_path=raw_input("\n Now .....Enter the folder path to store [csv] file   \nNOTE:-It should be a new folder\n")
		#asking the user to enter the file path so that we can convert thta xlsx file to that one and this variable is used in creatting a grph block
	X.Xlsx2csv(file_path).convert(converted_csv_file_path,sheetid=0)
	converted_csv_file_path=converted_csv_file_path+"/Sheet1.csv" 
	#the file is strored in the folder so the converted file is in that folder withthe name Sheet1 in that folder so the converted csv file path is now changed to the  Sheet1 file path in that folder 
	#converting the file xlsx - > csv
#end3--------------xlsx to csv............#


#start4 ----------creating a graph G-------#
if (input_file_type=='gexf'):
	while True:
		try:
			G = nx.read_gexf(file_path)
	#if the file format is in ---gexf--- read the graph and put that in G variable which is later used to write  graph
			break
		except IOError:
			print("Error while READING the file ")
	
elif(input_file_type=='gml'):
	while True:
		try:
			
			G = nx.read_gml(file_path)
	#if the file format isin ---gml---- read the graph and put that in G variable which is later used to write  graph
			break
		except IOError:
			print("Error while READING the file ")
	
elif(input_file_type=='pickle'):
	while True:
		try:
			G=nx.read_gpickle(file_path)
			break
	#if the file format isin --Pickle--- read the graph and put that in G variable which is later used to write  graph
		except IOError:
			print("Error while READING the file ")
		
elif(input_file_type=='graphML'):
	while True:
		try:
			G = nx.read_graphml(file_path)
			break
	#if the file format isin ---GraphML---- read the graph and put that in G variablich is later used to write  graph
		except IOError:
			print("Error while READING the file ")
	
elif(input_file_type=='LEDA'):
	while True:
		try:
			G = nx.read_leda(file_path)
			break
	#if the file format isin ---LEDA---- read the graph and put that in G variable which is later used to write  graph
		except IOError:
			print("Error while READING the file ")
	
elif(input_file_type=='YAML'):
	while True:
		try:
			G = nx.read_yaml(file_path)
			break
	#if the file format isin ---YAML--- read the graph and put that in G variable which is later used to write  graph
		except IOError:
			print("Error while READING the file ")
	
elif(input_file_type=='Pajek'):
	while True:
		try:
			G = nx.read_pajek(file_path)
			break
	#if the file format isin ---Pajek---- read the graph and put that in G variable which is later used to write  graph
		except IOError:
			print("Error while READING the file ")
		
elif(input_file_type=='SparseGraph6'):
	a=input("enter 1.for Sparse6 \n2.for graph6 format")
	if(a==1):
	  while True:
		try:
			G = nx.read_sparse6(file_path)
			break
		except IOError:
			print("Error while READING the file ")
		
	else :
	  while True:
		try:
			G=nx.read_graph6(file_path)
			break
	#if the file format isin ---SparseGraph6---- read the graph and put that in G variable which is later used to write  graph
		except IOError:
			print("Error while READING the file ")
		
elif(input_file_type=='GISShapefile'):
	while True:
		try:
			G = nx.read_shp(file_path)
			break	
	#if the file format isin ---Gisshapefile--- read the graph and put that in G variable which is later used to write  graph
		except IOError:

			print("Error while READING the file ")
	
elif((input_file_type=='csv' or input_file_type=='xlsx') and  output_file_type!='csv'):
	if(input_file_type=='xlsx'):
		#if the file is xlsx then we have to give the converted xlsxfile (csv file ) file path
		file_path=converted_csv_file_path;
		#changing the filepath to converted file path 

	var_to_know_the_input_graph_format_is_directed_or_undirected_Graph=raw_input("please enter the graph type \n0.Directed \n1.Undirected graph\n")
	#konwing whcih type of graph the user is giving 
	if(var_to_know_the_input_graph_format_is_directed_or_undirected_Graph=="0"):
		
		G=nx.DiGraph()
		#if the user wants a directed graph then create a directed graph G
	else:
		
		G=nx.Graph()
		#if the user wa,''nts a undirected graph then create a undirected graph G
	with open(file_path,'rU') as csvfile:
            #reader = csv.DictReader(open(csvfile, 'rU'), dialect=csv.excel_tab)
            reader = csv.DictReader(csvfile)
			#reading the csv file in dictreader .with this dictreader we can directly access the column in the csv file 
            print("\nHere are the column names with indices")
            for z in range(0,len(reader.fieldnames)):
            	print(str(z)+" "+reader.fieldnames[z])
            while True:
              try:

              	while True:
              		try:
              	 		key_word_error_catcher=0
                 		n_c=raw_input("Enter the nodes column  indices in csv file \n")
                 		nodes_coloumn=reader.fieldnames[int(n_c)]
                 		break
             		except IndexError:
             			print("Error :index error \nsee the index and enter again\n")
                 	
                 
			     #asking the user ti input the node column name in the csv file .If the input column is in the csv file then exit the loop other wise execute  again with a error mssg 
                if nodes_coloumn in reader.fieldnames:
                 	break
                 	
                else:
                 	print("no such column enter again...")    
              except ValueError: 
                  print("oops no such column in csv file ..please enter   a correct column\n")

            while True:
              try:
              	while True:
              		try:
              	 		key_word_error_catcher=0
                 		e_c=raw_input("Enter the edgescolumn in csv file types\n")
                 		edges_coloumn=reader.fieldnames[int(e_c)]
                 		#asking the user ti input the edge column name in the csv file .If the input column is in the csv file then exit the loop other wise execute  again with a error mssg 
                 
                 		break
             		except IndexError:
             			print("Error :index error \nsee the index and enter again\n")
                 

                 
                if edges_coloumn in reader.fieldnames:
                     break
                else:
                 	print("no such column enter again...")
                 
              except ValueError:
                  print("oops no such column in csv file ..please enter   a correct column\n")
            while True:
              try:
              	while True:
              		try:
              	 		key_word_error_catcher=0
                 		a_c=raw_input("Enter the weight/attribute column in csv file \n")
                 		attr_coloumn=reader.fieldnames[int(a_c)]
			     #asking the user ti input the attribute column name in the csv file .If the input column is in the csv file then exit the loop other wise execute  again with a error mssg 
                 
                 		break
             		except IndexError:
             			print("Error :index error \nsee the index and enter again\n")              	
                 
                if attr_coloumn in reader.fieldnames:
                     break
                else:
                 	print("no such column enter again...")
              except ValueError:
                  print("oops no such column in csv file ..please enter   a correct column\n")

            more_atrributes=raw_input("Do your data has more attributes to be added to the nodes or edges  [y/n] \n")
            if(more_atrributes=='y'):
            	nd_atrributes=raw_input("Do you want to add node atrributes [y/n]\n")
            	if(nd_atrributes=='y'):
            		string_contaning_all_the_input_indices_of_node_atrributes=raw_input("Enter all the indices of NODE ATTRIBUTES in a line with commas between them and hit ENTER\n") 
            		splited_string_contaning_all_the_input_indices_of_node_atrributes=string_contaning_all_the_input_indices_of_node_atrributes.split(",")
            	ed_atrributes=raw_input("Do you want to add any edge atrributes [y/n]\n")
            	if(ed_atrributes=='y'):
            		string_contaning_all_the_input_indices_of_edges_atrributes=raw_input("Enter all the indices of EDGES ATTRIBUTES in a line with commmas between them and hit ENTER\n")          	
            		splited_string_contaning_all_the_input_indices_of_edges_atrributes=string_contaning_all_the_input_indices_of_edges_atrributes.split(",")          

            for rj in reader:
		 	#this like is a loop each time it ittiraes the rj vaiable goes to next row in the csv file ,we can access the corresponding column by directly refering like a array .if we gave rj[nodes_column] we can directly get the access to the element in a particular row  
		      if(len(rj[nodes_coloumn])>0):
		      	#checks if thereis a node in that row.if there is a node in thet row then that node is added other wise ist is neglected
		      	if(more_atrributes=='y' and nd_atrributes=='y' and ed_atrributes=='y'):
		      		for it in range(0,len(splited_string_contaning_all_the_input_indices_of_node_atrributes)):
		      			#in this loop we add all the given node atrributes to a node ittiratively going through the row  
		      	
		      			r=int(splited_string_contaning_all_the_input_indices_of_node_atrributes[it])
		      		
		      			#the arribute index are stored as a  string so now converting it into a  int 		      		
		      			add_attributes_to_nodes(G,rj,nodes_coloumn,reader.fieldnames[r],rj[reader.fieldnames[r]])
		      			#calling the function .This function will add node atrributes to the node.
		      		

		        	string_1 = rj[edges_coloumn]
		        	splited_string_1=string_1.split(',')#spliting string w.r.t ","bcoz in some cases there can be more than one edge 

		        	string_2 = rj[attr_coloumn]
		        	splited_string_2=string_2.split(',')#spliting string w.r.t ","
		        	#bcoz in some cases there can be more than one edge 

			        for i in range(0,len(splited_string_1)):
			        	G.add_edge(rj[nodes_coloumn],splited_string_1[i],weight=splited_string_2[i])
			        	#adding edges to the graph with weight atrributes 

		      		for it in range(0,len(splited_string_contaning_all_the_input_indices_of_edges_atrributes)):
		      			#in this loop we add all the given node atrributes to a node ittiratively going through the row  
		      	
		      			r=int(splited_string_contaning_all_the_input_indices_of_edges_atrributes[it])
		      			#the arribute index are stored as a  string so now converting it into a  int 

		      			add_attributes_to_edges(G,rj,nodes_coloumn,edges_coloumn,reader.fieldnames[r],rj[reader.fieldnames[r]])
		      			#calling the function .This function will add node atrributes to the node.
		      			
		      	elif(more_atrributes=='y' and nd_atrributes=='y' and ed_atrributes!='y'):
		      		for it in range(0,len(splited_string_contaning_all_the_input_indices_of_node_atrributes)):
		      			#in this loop we add all the given node atrributes to a node ittiratively going through the row  
		      	
		      			r=int(splited_string_contaning_all_the_input_indices_of_node_atrributes[it])
		      		
		      			#the arribute index are stored as a  string so now converting it into a  int 		      		
		      			add_attributes_to_nodes(G,rj,nodes_coloumn,reader.fieldnames[r],rj[reader.fieldnames[r]])
		      			#calling the function .This function will add node atrributes to the node.
		      		string_1 = rj[edges_coloumn]
		        	splited_string_1=string_1.split(',')#spliting string w.r.t ","bcoz in some cases there can be more than one edge 
		        	string_2=rj[attr_coloumn]
		        	splited_string_2=string_2.split(',')
		      
		        	for i in range(0,len(splited_string_1)):
		        		G.add_edge(rj[nodes_coloumn],splited_string_1[i],weight=splited_string_2[i])
		        		#adding edges to the graph with weight atrributes 
		        elif(more_atrributes=='y' and nd_atrributes!='y' and ed_atrributes=='y'):
		        	G.add_node(rj[nodes_coloumn])

		        	string_1 = rj[edges_coloumn]
		        	splited_string_1=string_1.split(',')#spliting string w.r.t ","bcoz in some cases there can be more than one edge 

		        	string_2 = rj[attr_coloumn]
		        	splited_string_2=string_2.split(',')#spliting string w.r.t ","
		        	#bcoz in some cases there can be more than one edge 

			        for i in range(0,len(splited_string_1)):
			        	G.add_edge(rj[nodes_coloumn],splited_string_1[i],weight=splited_string_2[i])
			        	#adding edges to the graph with weight atrributes 

		      		for it in range(0,len(splited_string_contaning_all_the_input_indices_of_edges_atrributes)):
		      			#in this loop we add all the given node atrributes to a node ittiratively going through the row  
		      	
		      			r=int(splited_string_contaning_all_the_input_indices_of_edges_atrributes[it])
		      			#the arribute index are stored as a  string so now converting it into a  int 

		      			add_attributes_to_edges(G,rj,nodes_coloumn,edges_coloumn,reader.fieldnames[r],rj[reader.fieldnames[r]])
		      			#calling the function .This function will add node atrributes to the node.


		      		
		      	else:
		      		G.add_node(rj[nodes_coloumn])
		      		string_1 = rj[edges_coloumn]
		        	splited_string_1=string_1.split(',')#spliting string w.r.t ","bcoz in some cases there can be more than one edge 
		        	string_2=rj[attr_coloumn]
		        	splited_string_2=string_2.split(',')
		      
		        	for i in range(0,len(splited_string_1)):
		        		G.add_edge(rj[nodes_coloumn],splited_string_1[i],weight=splited_string_2[i])
		        		#adding edges to the graph with weight atrributes 
	#if(input_file_type=='xlsx'):#changed-------------------------------------------------------------------------------------------------------------------------------
	#	os.remove(file_path)
		      		
		 	    	
elif(input_file_type=='xlsx' and  output_file_type =='csv'):
	X.Xlsx2csv(file_path).convert(output_file_path,sheetid=0)

		
#end4 ----------creating a graph G---------#






#start5---------writing graphs in the required formats------------#ile

while True:
	if (output_file_type=='gexf'):
		
			try:
				G = nx.write_gexf(G,output_file_path)
				#if the file format is in ---gexf--- write  graph G
				
				break
			except IOError:
				print("The out put type:"+output_file_type+"please select another output file path\n")

		
	elif(output_file_type=='gml'):
		
			try:
				G = nx.write_gml(G,output_file_path)
		#if the file format isin ---gml----  write  graph G
				break
			except IOError:
				print("The out put type:"+output_file_type+"please select another output file path\n")


		
	elif(output_file_type=='pickle'):
		
			try:
				G=nx.write_gpickle(G,output_file_path)
		#if the file format isin --Pickle---  write  graph G
				break
			except IOError:
				print("The out put type:"+output_file_type+"please select another output file path\n")

	elif(output_file_type=='graphML'):
		
			try:
				G = nx.write_graphml(G,output_file_path)
		#if the file format isin ---GraphML----  write  graph Gkl
				break
			except IOError:
				print("The out put type:"+output_file_type+"please select another output file path\n")
		
		
	elif(output_file_type=='YAML'):
		
			try:
				G= nx.write_yaml(G,output_file_path)
		#if te file format isin ---YAML---  write  graph G
				break
			except IOError:
				print("The out put type:"+output_file_type+"please select another output file path\n")
		
	elif(output_file_type=='Pajek'):
		
			try:
				G = nx.write_pajek(G,output_file_path)
		#if the file format isin ---Pajek----  write  graph G
				break
			except IOError:
				print("The out put type:"+output_file_type+"please select another output file path\n")
		
	elif(output_file_type=='SparseGraph6'):

		a=input("enter 1.for Sparse6 \n2.for graph6 format\n")
		if(a==1):
			
			try:
				G = nx.write_sparse6(G,output_file_path)
		#if the file format isin ---sparse6---  write  graph G
				break
			except IOError:
				print("The out put type:"+output_file_type+"please select another output file path\n")
			
		else :
			
			try:
				G=nx.write_graph6(G,output_file_path)
		#if the file format isin ---graph6----  write  graph G
				break
			except IOError:
				print("The out put type:"+output_file_type+"please select another output file path\n")
			
		#if the file format isin ---SparseGraph6----  write  graph G
	elif(output_file_type=='GISShapefile'):
		
			try:
				G = nx.write_shp(G,output_file_path)	
		#if the file format isin ---Gisshapefile--- write  graph G+
				break
			except IOError:
				print("The out put type:"+output_file_type+"please select another output file path\n")
	output_file_type=raw_input("Now enter file type again other than-> " +output_file_type+" \nE to exit")
	if(output_file_type=='E\n'):
		break
	output_file_path=raw_input("Now enter the output file path again\n")	


 
#end5---------writing graphs in the required formats------------#






print("\nThe Graph is converted successfulliy  from ["+input_file_type+"] to ["+output_file_type+"]\n Check the location "+output_file_path+" for the required output file ")
print("\n                                       THANK YOU\n\n\n")