from typing import Union

import pytz
import datetime as dt

from .config import app

def get_current_datetime(
        as_string: bool = False, 
        format: str = '%Y-%m-%d %H:%M:%S'
    ) -> Union[dt.datetime, str]:
    """
    """
    tz = pytz.timezone(app.TZ)
    current_time = dt.datetime.now(tz)

    return current_time.strftime(format) if as_string \
        else current_time
