import pandas as pd
from pangeo_forge.recipe import NetCDFtoZarrSequentialRecipe
import os

dates = pd.date_range("2021-02", "2021-05", freq="M")
regions = range(1,5)

input_url_pattern = (
                "https://ige-meom-opendap.univ-grenoble-alpes.fr/"
                "thredds/fileServer/meomopendap/extract/SWOT-Adac/Surface/eNATL60/"
                "Region{region}-surface-hourly_{month}.nc"
                     )
input_urls = [
              input_url_pattern.format(region=os.path.join("%02d" % reg),
                                       month=day.strftime("%Y%m")
                                      )
              for reg in regions for day in dates
             ]

recipe = NetCDFtoZarrSequentialRecipe(
                    input_urls=input_urls,
                    sequence_dim="time_counter",
                    inputs_per_chunk=20
                    )
