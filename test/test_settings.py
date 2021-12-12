from typing import List
import pytest
from src.settings import get_settings, get_streams_string


def test_settings_load():
    """Test whether setting file loads or not
    """
    settings = get_settings()

    assert settings != None


@pytest.mark.depends(on=['test_settings_load'])
def test_params():
    """Test whether interval param in settings
    """
    settings = get_settings()

    assert 'logger' in settings
    
    assert 'interval' in settings.get('logger', {})
    assert 'trading_pairs' in settings.get('logger', {})
    assert 'sma_interval' in settings.get('logger', {})

    logger_settings = settings.get('logger')

    assert logger_settings['interval'] == '1m'
    assert len(logger_settings['trading_pairs']) > 0
    assert type(logger_settings['sma_interval']) is int
    assert logger_settings['sma_interval'] > 0


@pytest.mark.depends(on=['test_settings_load'])
@pytest.mark.parametrize(
    'trading_pairs,interval,stream_string',
    [
        (
            ['BTCUSDT', 'ETHUSDT', 'BNBBTC'],
            '1m',
            'wss://stream.binance.com:9443/stream?streams=btcusdt@kline_1m/ethusdt@kline_1m/bnbbtc@kline_1m'
        ),
        (
            ['BTCUSDT', 'ETHUSDT'],
            '5m',
            'wss://stream.binance.com:9443/stream?streams=btcusdt@kline_5m/ethusdt@kline_5m'
        )
    ]
)
def test_streams_string(
    trading_pairs: List[str],
    interval: str,
    stream_string: str
):
    """Test whether streams websocket string forms right
    """

    assert get_streams_string(trading_pairs, interval) == stream_string