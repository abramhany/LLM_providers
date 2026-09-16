from enum import Enum

class LLMError(Enum):

    INVALID_REQUEST  = 'User request was invalid'
    UNSUPPORTED_PARAMETER = "The requested parameter is not supported by this model."
    RATE_LIMIT_EXCEEDED = "Rate limit exceeded. Please check your quota."
    EMPTY_RESPONSE = 'Provider returned empty content'
