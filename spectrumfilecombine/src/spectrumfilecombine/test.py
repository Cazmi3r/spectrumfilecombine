from pathlib import Path
from combine import FileBuffer
from combine import generate_header

base_path = Path(r"P:\Clients\HYLA\Jobs")
job_number = "57202"
date = "0531H"
final_path = base_path / job_number / "DataIn" / date
print(final_path)
files = list(final_path.glob('*.txt'))
print(len(files))

testBuffer = FileBuffer("57202", "0531H")
print(testBuffer.validate_buffer())
print(testBuffer.is_buffer_empty())
print(testBuffer.pop_file())