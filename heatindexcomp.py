from readdata import read_data

# Column names and column indices to read
columns = {'date': 0, 'time': 1, 'tempout': 2, 'humout': 5, 'heatindex': 13}

# Data types for each column (only if non-string)
types = {'tempout': float, 'humout': float, 'heatindex': float}

# Read data from file
data = read_data(columns, types=types)


# Compute the heat index
def compute_heatindex(t, rh_pct):
   a = -42.379
   b = 2.04901523
   c = 10.14333127
   d = -0.22475541
   e = -0.00683783
   f = -0.05481717
   g = 0.00122874
   h = 0.00085282
   i = -0.00000199

   rh = rh_pct / 100

   hi = a + (b * t) + (c * rh) + (d * t * rh) + (e * t**2) + (f * rh**2) + (g * t**2 * rh) + (h * t * rh**2) + (i * t**2 * rh**2)
   return hi

# Compute the heat index
heatindex = []
for temp, hum in zip(data['tempout'], data['humout']):
   heatindex.append(compute_heatindex(temp, hum))

# Output comparison of data
print('                ORIGINAL  COMPUTED')
print(' DATE    TIME  HEAT INDX HEAT INDX DIFFERENCE')
print('------- ------ --------- --------- ----------')
for date, time, hi_orig, hi_comp in zip(data['date'], data['time'], data['heatindex'], heatindex):
   print(f'{date} {time:>6} {hi_orig:9.6f} {hi_comp:9.6f} {hi_orig-hi_comp:10.6f}')


