import os
os.chdir('/Users/abhishek/Desktop/shivam/python-got-to-go/')

import webbrowser
import requests
import json

from user import user
from master import master

user = user()
master = master()

print('')
print('')
print('Welcome to Shouchalya Mission')
print('-----------------------------')
print('')
print('')
print("Welcome to login module")
choice = int(input("Do you want to sign-in or sign-up, please select 1 or 2 "))
if choice == 1:
    user.login()
    print(user.first_name + " logged in last at " + str(user.last_login))
else:
    user.new_user()

master.read_data()

choice = 0
while choice < 4:

    print('')
    print('')
    print('0: View all records')
    print('1: Add new record')
    print('2: Edit existing record')
    print('3: Enter your current loction to find the closest toilets')
    print('4: Exit')
    choice = int(input('Enter your choice [0..4] - '))

    if choice == 0:
        master.view_data()

    elif choice == 1:
        if user.user == "shivam":
            master.capture_data()
        else:
            print("unauthorised access")

    elif choice == 2:
        if user.user == "shivam":
            id = int(input("Enter the ID to edit - "))
            master.edit_data(id)
        else:
            print("unauthorised access")
    elif choice == 3:

        send_url = 'http://freegeoip.net/json'
        r = requests.get(send_url)
        j = json.loads(r.text)
        lat = j['latitude']
        lon = j['longitude']
        #lat = 0
        #lon=0

        p1 = 'Enter Current location (Latitude  = ' + str(lat) + ') = '
        curr_lat = input(p1)
        if curr_lat == '':
            curr_lat = lat
        else:
            curr_lat = float(curr_lat)

        p1 = 'Enter Current location (Longitude = ' + str(lon) + ') = '
        curr_lon = input(p1)
        if curr_lon == '':
            curr_lon = lon
        else:
            curr_lon = float(curr_lon)

        counter  = int(input('Count of toilets to be displayed = '))

        master.calculate_distance(curr_lat, curr_lon, counter)

        url = 'file:///Users/abhishek/Desktop/shivam/python-got-to-go/map.html'
        webbrowser.open_new(url)

    else:
        user.logout()
