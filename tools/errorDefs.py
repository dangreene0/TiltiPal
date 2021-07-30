class Error(Exception):
    """Base class for other exceptions"""
    pass

class NoCampaignError(Error):
    """No Previous Event Found"""
    pass

class NoPreviousFileError(Error):
    """No Previous Event Found"""
    pass