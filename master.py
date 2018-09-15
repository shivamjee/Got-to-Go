import csv
from math import sin, cos, sqrt, atan2, radians


class master:
    'Common base class for toilets'

    def __init__(self):
        self.csv_rows = []

    def read_data(self):
        csv_file_obj = open('/Users/abhishek/Desktop/shivam/python-got-to-go/toilet.csv')
        csv_reader = csv.reader(csv_file_obj)
        self.csv_rows = list(csv_reader)

    def capture_data(self):
        print('Enter the following values')
        id        = int(self.csv_rows[-1][0]) + 1
        address   = input('Address   = ')
        locality  = input('Locality  = ')
        state     = input('State     = ')
        pin       = input('Pincode   = ')
        latitude  = input('Latitude  = ')
        longitude = input('Longitude = ')
        owner     = input('Owner     = ')
        paid      = input('Free/Paid = ')
        rating    = input('Rating    = ')
        row = [str(id), address, locality, state, pin, latitude, longitude, owner, paid, rating]
        self.csv_rows.append(row)
        self.write_data()

    def edit_data(self, id):
        print('Press Enter if you want old value else key in new value to be updated in the CSV')

        p1 = 'Address     [' + self.csv_rows[id][1] + '] = '
        address = input(p1)
        address = address or self.csv_rows[id][1]

        p1 = 'Locality    [' + self.csv_rows[id][2] + '] = '
        locality = input(p1)
        locality = locality or self.csv_rows[id][2]

        p1 = 'State       [' + self.csv_rows[id][3] + '] = '
        state = input(p1)
        state = state or self.csv_rows[id][3]

        p1 = 'Pincode     [' + self.csv_rows[id][4] + '] = '
        pin = input(p1)
        pin = pin or self.csv_rows[id][4]

        p1 = 'Latitude    [' + self.csv_rows[id][5] + '] = '
        latitude = input(p1)
        latitude = latitude or self.csv_rows[id][5]

        p1 = 'Longitude   [' + self.csv_rows[id][6] + '] = '
        longitude = input(p1)
        longitude = longitude or self.csv_rows[id][6]

        p1 = 'Owner       [' + self.csv_rows[id][7] + '] = '
        owner = input(p1)
        owner = owner or self.csv_rows[id][7]

        p1 = 'Free/Paid   [' + self.csv_rows[id][8] + '] = '
        paid = input(p1)
        paid = paid or self.csv_rows[id][8]

        p1 = 'Rating      [' + self.csv_rows[id][9] + '] = '
        rating = input(p1)
        rating = rating or self.csv_rows[id][9]

        row = [str(id), address, locality, state, pin, latitude, longitude, owner, paid, rating]

        self.csv_rows[id] = row
        self.write_data()

    def view_data(self):
        self.read_data()
        for row in self.csv_rows:
            print(row)

    def write_data(self):
        csv_file_obj = open('/Users/abhishek/Desktop/shivam/python-got-to-go/toilet.csv', 'w', newline='')
        csv_writer = csv.writer(csv_file_obj)
        for row in self.csv_rows:
            csv_writer.writerow(row)
        csv_file_obj.close()

    def calculate_distance(self, curr_lat, curr_lon, no_of_rows):

        csv_new_rows = []

        R = 6373.0

        lat1 = radians(abs(curr_lat))
        lon1 = radians(abs(curr_lon))

        for row in self.csv_rows:
            if row[0] == 'id':
                continue

            lat2 = radians(abs(float(row[5])))
            lon2 = radians(abs(float(row[6])))

            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = (sin(dlat / 2)) ** 2 + cos(lat1) * cos(lat2) * (sin(dlon / 2)) ** 2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))

            distance = round((R * c), 2)

            row.append(distance)
            csv_new_rows.append(row)

        csv_new_rows.sort(key=lambda x: x[10])

        mapdata = '['

        for x in range(no_of_rows):
            print('')
            print('Location : ' + csv_new_rows[x][1] + ', ' + csv_new_rows[x][2] + ', ' + csv_new_rows[x][3] + ' - ' + csv_new_rows[x][4])
            print('Distance : ' + str(csv_new_rows[x][10]))
            if x == 0:
                mapdata = mapdata + '{' + '"lat": ' + str(curr_lat) + ',' + '"lng": ' + str(curr_lon) + '}'

            mapdata = mapdata + ', {' + '"lat": ' + str(csv_new_rows[x][5]) + ',' + '"lng": ' + str(csv_new_rows[x][6]) + '}'

        mapdata = mapdata + ']'

        file = open('/Users/abhishek/Desktop/shivam/python-got-to-go/mapdata.txt', 'w')
        file.write('data = ' + "'" + mapdata + "'")
        file.close()
