'''
This program allows finding the passwords of a WIFI that the current laptop was connected to. 
In order to see the list of WIFI's, the laptop was connected to, type 'netsh wlan show profiles' in terminal. 
Then in order to find pw of a particular WIFI, type 'netsh wlan show profile "WIFINAMEYOUARELOOKINGFOR" key=clear' in terminal.
Under the title Security setting under the Key content line, you can find the WIFI pw. 
'''
import subprocess

if __name__ == "__main__":
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')  #This line gets all the WIFI networks that this device was connected to converted from utf-8 and split on new line character 
    wifis =[line.split(':')[1][1:-1] for line in data if "All User Profile" in line] #This line returns only things with "All User profile" in the line and splits it with ':'. Then it returns the second item (Rmbr 0 based indexing in python) that is from the first character until the second last character .
    
    for wifi in wifis:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n') #Add the key=clear command for each wifi
        results = [line.split(':')[1][1:-1] for line in results if "Key Content" in line] #Gets only the line which has Key Content or Password in it. 
        try:
            print(f'WIFI: {wifi:<25} Password: {results[0]}') # Print each WIFI name and password
        except IndexError:
            print(f'WIFI: {wifi:<25} Password: Not Able to Retrieve!')
