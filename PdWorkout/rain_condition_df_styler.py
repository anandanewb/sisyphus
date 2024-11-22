import numpy as np
import pandas as pd


weather_df = pd.DataFrame(np.random.rand(10,2)*5,
                          index=pd.date_range(start='2020-01-01', periods=10),
                          columns=['Tokyo', 'Beijing'])

def rain_condition(v):
    if v < 1.75:
        return 'Dry'
    elif v < 2.75:
        return 'Rain'
    return 'Thunderstorm'

def make_pretty(styler):
    styler.set_caption("Weather Conditions")
    styler.format(rain_condition)
    styler.format_index(lambda v: v.strftime('%A %d %B %Y'))
    styler.background_gradient(axis=None, vmin=1, vmax=5, cmap="YlOrRd")
    return styler

weather_df.style.pipe(make_pretty)