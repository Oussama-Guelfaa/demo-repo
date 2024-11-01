def calculate_ema(data, period):
    """
    Calculate the Exponential Moving Average (EMA) for a given data series.
    
    :param data: List of data points (e.g., stock prices).
    :param period: The EMA period (e.g., 20 for 20-day EMA).
    :return: List containing the EMA values.
    """
    ema_values = []
    multiplier = 2 / (period + 1)
    
    # Calculate the initial SMA (Simple Moving Average) for the first EMA value
    sma = sum(data[:period]) / period
    ema_values.append(sma)
    
    # Calculate subsequent EMA values
    for price in data[period:]:
        ema = (price - ema_values[-1]) * multiplier + ema_values[-1]
        ema_values.append(ema)
    
    return ema_values

# Example usage
if __name__ == "__main__":
    prices = [100, 102, 101, 105, 108, 107, 110, 112, 115, 117, 120, 125]
    period = 5
    ema_values = calculate_ema(prices, period)
    print(f"Exponential Moving Average (EMA) for period {period}: {ema_values}")