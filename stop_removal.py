
import re
infile=""

st_list=" കാണാന്‍ ‍| നിന്ന് | കുറഞ്ഞ | മുഴുവന് ‍| കൂടാതെ | ആദ്യം | ഈ | കൂടുതല്‍ | താങ്കള്‍ | എന്നാല് ‍| അതിനു | ശേഷം | ചെയ്യുന്നു | ഇവിടത്തെ | വേണ്ടി | ഏറ്റവും | ഇതില് ‍| വേണ്ടിയും | ആണ് | സ്ഥിതിചെയ്യുന്നു | സ്ഥിതി | സ്ഥിതിചെയ്യുന്ന | ചെയ്യണം | നമ്മുടെ | ഇപ്പോള് ‍| ഒരു | തന്റെ | ചെയ്യുന്ന | എന്ന | ചെയ്യുന്നത് | ഉണ്ട് | മുന്‍പ് | മുമ്പ് | കൂടെ | ചേര്‍ത്തു | ഇപ്രകാരം | എന്നിവയുടെ | കഴിയും | എന്നീ | ഇതാണ് | വളരെ | കാരണം | ഇവിടത്തെ | എപ്പോഴും | കൊണ്ട് | നല്ല | ധാരാളം | എപ്പോഴും | ഇവ | കാരണം | ഇതു | മാത്രമല്ല | മറ്റു | എന്നിവ | കൂടിയാണ് | ഇടയില് ‍| ഇല്ല | എന്നാണ് | എന്നു | കുറച്ച് | അതായത് | എന്തെന്നാല് ‍| എന്നറിയപ്പെടുന്നു | കിടക്കുന്ന | പോയാല് ‍| ഇത് | എല്ലാ | വേണ്ടി | ഇവിടെ | വരുന്നു | പോലുള്ള | വലിയ | പറഞ്ഞ് | ഇതിനെ | കൊടുത്തിട്ടും | എന്ന് | വേണം | ഒരുപോലെ | ഒരു പോലെ | കാര്യമാണ് | കഴിയുന്നു | വളരെ | അധികം | വളരെ അധികം | വളരെയധികം | പോയി | ഉണ്ടാകുന്നുണ്ട് | പക്ഷേ | അതേ | കൊണ്ട് | ഏത് | നിന്നും | എത്താന്‍ | അടുത്ത് | ആയി | എന്നു പറയുന്നു | ഇപ്പോൾ | ഏകദേശം | എന്നുപറയുന്നു | കാണാൻ | ആ | വിവിധ | ഇതിന്റെ | നിന്നു | ഇതിന് | അടുത്ത | അടുത്തുള്ള | പല | പ്രധാന | നിലനിൽക്കുന്ന | നിലനിൽക്കുന്നത് | മുതലായവ | മുതലായവക്ക് | വേണ്ട | പ്രാധാന്യം "
# function to read an input file
def main_program(infile):
#reading an input file
#infile=input("enter the input file")
	file1=open(infile,"r")
	file2=open("output.txt","w")
	f3=open("out.txt","w")
  
#read the contents of the input file and remove the stop words in the stopword list(st_list)
	for content in file1.readlines():
		#print("enter the contents of the input file")
		print(content)
		#identify and stop_words and replace with empty string and write the contents into output file.
		clear = re.sub(st_list,'  ', content)
		file2.write(clear)
		print(clear)
	file2.close()
	#read the output file and display the contents
	file3=open("output.txt","r")
	file_contents = file3.read()
	print("contents of python file")
	print (file_contents)
	tokens=file_contents.split()
	print(tokens)
	for temp in tokens:
		f3.write(temp)
		f3.write("\n")
		
	f3.close()
#print(clear)
	f3=open("out.txt","r")
	f_contents=f3.read()
	#print(f_contents)
	
#file3.close()
	file1.close()
	#fil
	f3.close()
	
	return f_contents
	
