# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import time

# Read recipe inputs
ncaatourneyCompactResults = dataiku.Dataset("NCAATourneyCompactResults")
ncaatourneyCompactResults_df = ncaatourneyCompactResults.get_dataframe()

time.sleep(600)

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

go_to_sleep_4_df = ncaatourneyCompactResults_df # For this sample code, simply copy input to output


# Write recipe outputs
go_to_sleep_4 = dataiku.Dataset("go_to_sleep_4")
go_to_sleep_4.write_with_schema(go_to_sleep_4_df)
