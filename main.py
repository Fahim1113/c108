import random
import plotly.express as px
import plotly.figure_factory as ff

arr = []
count = []

for i in range(100):
  a = random.randint(1, 6)
  b = random.randint(1, 6)
  arr.append(a + b)
  count.append(i)

ff.create_distplot([arr], ["normal curve distribution for dice data"], show_hist=False).show()