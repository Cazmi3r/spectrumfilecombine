from pathlib import Path

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
        path_to_data = build_path_to_data(job_number, date_mmddx)
        self.buffer = list(path_to_data.glob('*.txt'))
        if not self.validate_buffer():
            raise RuntimeError("Data isn't Valid")
    def validate_buffer(self):
        """validates each file is the proper format"""
        header = generate_header()
        for file in self.buffer:
            with open(file) as f:
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
    def process_files(self, buffer):
        """combines all files into one file adding original file name to end"""
        pass
