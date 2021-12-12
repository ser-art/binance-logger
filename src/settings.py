"""Provide uils to work wirth settings file"""

import yaml
import os


def get_settings() -> dict:
    """Get settings file as dict object 

    Returns:
        dict: Settings dict object
    """
    try:
        settings_path = os.environ.get('SETTINGS_PATH', 'settings.yaml')
        with open(settings_path, 'r') as file:
            settings = yaml.safe_load(file)
    except Exception as e:
        settings = None

        print(e)

    return settings


def get_sma_interval():
    return get_settings()['logger']['sma_interval']


def get_streams_string(
    trading_pairs: str = get_settings()['logger']['trading_pairs'],
    interval: str = get_settings()['logger']['interval']
) -> str:
    """Get streams string for websocket connection

    Returns:
        str: Streams string
    """

    base_url = os.environ.get('BASE_URL')

    trading_pairs = [
        tp.lower() + f'@kline_{interval}' 
        for tp in trading_pairs
    ]

    streams_string = [
        base_url,
        'stream?streams=',
        '/'.join(trading_pairs)
    ]

    streams_string = ''.join(streams_string)

    return streams_string
    


