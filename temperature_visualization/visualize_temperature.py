import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def generate_sample_data():
    """生成示例温度数据"""
    np.random.seed(42)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    
    dates = pd.date_range(start_date, end_date, freq='D')
    base_temp = 15  # 基准温度
    
    # 生成带有季节性的温度数据
    seasonal = 10 * np.sin(2 * np.pi * np.arange(len(dates)) / 365)
    noise = np.random.normal(0, 2, len(dates))
    
    # 添加长期趋势（变暖）
    trend = np.linspace(0, 1, len(dates))
    
    temperatures = base_temp + seasonal + noise + trend
    
    return pd.DataFrame({
        'date': dates,
        'temperature': temperatures,
        '7d_avg': pd.Series(temperatures).rolling(window=7).mean()
    })

def plot_temperature_data(df):
    """绘制温度数据"""
    plt.figure(figsize=(12, 6))
    
    # 绘制每日温度
    plt.plot(df['date'], df['temperature'], 
             'o', markersize=3, alpha=0.5, label='Daily')
    
    # 绘制7日移动平均线
    plt.plot(df['date'], df['7d_avg'], 
             'r-', linewidth=2, label='7-day Moving Avg')
    
    # 添加趋势线
    z = np.polyfit(range(len(df)), df['temperature'], 1)
    p = np.poly1d(z)
    plt.plot(df['date'], p(range(len(df))), 'k--', 
             label=f'Trend: {z[0]*365:.2f}°C/year')
    
    # 设置图表样式
    plt.title('Temperature Trends (Last 12 Months)', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Temperature (°C)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    
    # 保存图表
    plt.savefig('temperature_trend.png')
    plt.show()

def main():
    print("Generating temperature data...")
    df = generate_sample_data()
    
    print("Plotting temperature trends...")
    plot_temperature_data(df)
    
    print("Done! Check 'temperature_trend.png' for the visualization.")
    
    # 显示一些统计信息
    print("\nTemperature Statistics:")
    print(f"Average temperature: {df['temperature'].mean():.2f}°C")
    print(f"Maximum temperature: {df['temperature'].max():.2f}°C")
    print(f"Minimum temperature: {df['temperature'].min():.2f}°C")

if __name__ == "__main__":
    main()
