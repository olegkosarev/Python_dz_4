from sys import argv

script_name, working_hours, pay_rate, premium = argv

def zp(working_hours, pay_rate, premium):
	return(int(working_hours)*int(pay_rate)+int(premium))



print(zp(working_hours, pay_rate, premium))

