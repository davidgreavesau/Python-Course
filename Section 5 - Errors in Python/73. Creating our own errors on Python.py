class RunTimeErrorWithCode(TypeError):
    # This is a doc string
    """
    Exception raised when a specific error code is needed.
    """
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code


err = RunTimeErrorWithCode('An error happened.', 500)
print(err.__doc__)