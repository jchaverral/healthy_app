from modules.data_loader import load_data
from modules.analysis import plot_distr_segment, plot_distr_segment2

df = load_data()
plot_distr_segment(df)
plot_distr_segment2(df)