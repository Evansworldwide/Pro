   1  import os
   2  import platform
   3  import webbrowser
   4  os.system('termux-setup-storage')
   5  os.system('git pull')
   6  try:os.system('mkdir /sdcard/pro-DATA')
   7  except:pass
   8  try:os.system('mkdir /sdcard/pro-DATA/OK')
   9  except:pass
  10  try:os.system('mkdir /sdcard/pro-DATA/CP')
  11  except:pass
  12  try:os.system('mkdir /sdcard/pro-DATA/TAP-A2F')
  13  except:pass
  14  try:os.system('touch .prox.txt')
  15  except:pass
  16  P = '\x1b[1;97m'
  17  import os,requests
  18  xr = requests.get("http://ip-api.com/json/").json()
  19    try:
  20       	fc = xr["country"]
  21     except KeyError:
  22	print('%s\nBAD INTERNET CONNECTION\n'%(P))
  23	exit()
  24
  25  if __name__ == "__main__":
  26	os.system("git pull")
  27 	if "Nigeria" == fc:
  28		__import__("pro").main_chi()
  29	 else:
  30		__import__("pro").main_chi()
