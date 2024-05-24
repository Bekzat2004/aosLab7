class BufferOverflowError(Exception):
    def __init__(self, message="Buffer overflow error! Input exceeds the allowed length."):
        self.message = message
        super().__init__(self.message)

def simulate_buffer_overflow(input_string):
    BUFFER_LIMIT = 10
    if len(input_string) > BUFFER_LIMIT:
        raise BufferOverflowError()
    else:
        return f"Input is within the buffer limit: {input_string}"

try:
    result = simulate_buffer_overflow("This is a test string that exceeds the limit")
    print(result)
except BufferOverflowError as e:
    print(e)
