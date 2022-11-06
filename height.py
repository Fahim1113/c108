import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")

ff.create_distplot([list(df["Height(Inches)"])], ["height distribution"], show_hist=False).show()
ff.create_distplot([list(df["Weight(Pounds)"])], ["weight distribution"], show_hist=False).show()