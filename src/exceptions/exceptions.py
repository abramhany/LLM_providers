class LLMError(Exception):
    """Base exception for LLM-related failures."""


class Authentication_Error(LLMError):
    """The provider rejected authentication."""


class InvalidRequest_Error(LLMError):
    """The provider rejected the request as invalid."""


class RateLimit_Error(LLMError):
    """The provider rate limit was reached."""


class Connection_Error(LLMError):
    """A network or timeout error occurred."""


class Provider_Error(LLMError):
    """The provider returned an unexpected server-side error."""



class BadRequest_Error(LLMError):
    """return user request was malform or missing some requierd parameters"""