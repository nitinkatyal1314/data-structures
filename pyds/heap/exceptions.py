from common.exceptions import DSBaseException


class DeleteOperationInvalidError(DSBaseException):

    def __init__(self):
        message = "Deleting from an empty Heap. Invalid Operation"
        super(DeleteOperationInvalidError, self).__init__(message)


class InvalidHeapTypeError(DSBaseException):

    def __init__(self, valid_heap_types: list):
        _types = map(lambda x: str(x["value"]) + " (" + x["type"] + ")", valid_heap_types)
        message = "Valid heap types are : %s" % (", ".join(_types))
        super(InvalidHeapTypeError, self).__init__(message)
