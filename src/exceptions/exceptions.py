class LLMErrorException(Exception):
    """Base exception for LLM-related failures."""


class Authentication_Error(LLMErrorException):
    """The provider rejected authentication."""


class InvalidRequest_Error(LLMErrorException):
    """The provider rejected the request as invalid."""


class RateLimit_Error(LLMErrorException):
    """The provider rate limit was reached."""


class Connection_Error(LLMErrorException):
    """A network or timeout error occurred."""


class Provider_Error(LLMErrorException):
    """The provider returned an unexpected server-side error."""



class BadRequest_Error(LLMErrorException):
    """return user request was malform or missing some requierd parameters"""