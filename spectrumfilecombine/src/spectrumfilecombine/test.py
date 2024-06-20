from pathlib import Path
from combine import FileBuffer
from combine import SpectrumCombiner
import pandas as pd
job_number = "57202"
date = "0531H"

combiner = SpectrumCombiner(job_number, date)
combiner.process_files()