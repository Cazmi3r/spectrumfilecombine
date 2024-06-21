from pathlib import Path 
import pandas as pd

def build_path_to_data(job_number, date_mmddx):
    """builds the path to the data from the job num and date"""
    base_path = Path(r"P:\Clients\HYLA\Jobs")
    path_to_data = base_path / job_number / "DataIn" / date_mmddx
    return path_to_data
def generate_header():
    """Generates the header used for validation"""
    return r"First Name|Last Name|Phone #|E-mail|Address|Address 2|City|State|Zip|Item #|invoice_id|Trade Date|Kit Type Required|Carrier"

class FileBuffer():
    """Buffer for managing files"""
    def __init__(self, job_number, date_mmddx) -> None:
        self.path_to_data = build_path_to_data(job_number, date_mmddx)
        self.buffer = list(self.path_to_data.glob('*.txt'))
        if not self.validate_buffer():
            raise RuntimeError("Data isn't Valid")
    def validate_buffer(self):
        """validates each file is the proper format"""
        header = generate_header()
        for file in self.buffer:
            with open(file, encoding="utf-8") as f:
                first_line = f.readline().strip('\n')
                if first_line != header:
                    return False
        return True
    def pop_file(self):
        """returns one file from the buffer then removes it"""
        return self.buffer.pop()
    def is_buffer_empty(self):
        """checks if buffer is empty and returns a boolean value"""
        if not self.buffer:
            return True
        return False
    def get_buffer_size(self):
        """returns size of buffer"""
        return len(self.buffer)

class SpectrumCombiner():
    """Combines all text files into one file"""
    def __init__(self, job_number, date_mmddx) -> None:
        self.buffer = FileBuffer(job_number, date_mmddx)
        self.path_to_data = self.buffer.path_to_data
        self.df_to_combine = []
        self.process_files()
    def process_files(self):
        """combines all files into one file"""  
        # add all files to be combined into a single list
        while not self.buffer.is_buffer_empty():
            file_to_add = self.buffer.pop_file()
            self.df_add_file(file_to_add)
        # Combine data and output file
        output_df = pd.concat(self.df_to_combine)
        output_df.to_csv(
            self.path_to_data / "SpectrumData.txt",
            index=None,
            sep="|"
        )
    def df_add_file(self, file):
        """adds a file to output df and appends file name to df"""
        to_add_df = pd.read_csv(file,sep='|')
        to_add_df['filename'] = file.stem
        self.df_to_combine.append(to_add_df)
