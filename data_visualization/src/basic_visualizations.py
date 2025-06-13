"""
数据可视化工具集

本模块提供了基本的数据可视化功能，包括：
- 基础图表：折线图、散点图
- 曲线拟合：多项式拟合、样条插值
- 动态可视化：数据拟合过程动画

所有输出文件将保存在当前目录下的'output'文件夹中。

依赖库：
- numpy: 数值计算
- matplotlib: 基础绘图
- seaborn: 高级统计图表
- scipy: 科学计算与插值
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import interpolate
from scipy.optimize import curve_fit
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from typing import Callable, Tuple, List, Optional

# 创建输出目录
OUTPUT_DIR = './data_visualization/output'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 设置图表样式，使用seaborn风格使图表更美观
plt.style.use('seaborn-v0_8')

# 设置随机种子，确保结果可复现
np.random.seed(42)

def create_sample_line_plot() -> None:
    """
    创建并保存一个简单的折线图示例
    
    生成一个正弦波的折线图，并保存为'line_plot.png'
    """
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)
    plt.title('Sample Line Plot: Sine Wave', fontsize=14)
    plt.xlabel('X-axis', fontsize=12)
    plt.ylabel('Y-axis', fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, 'line_plot.png')
    plt.savefig(output_path)
    plt.close()
    return output_path

def create_sample_scatter_plot() -> None:
    """
    创建并保存一个散点图示例
    
    生成带有随机噪声的散点图，并保存为'scatter_plot.png'
    """
    np.random.seed(42)
    x = np.random.normal(0, 1, 100)
    y = 2 * x + np.random.normal(0, 0.5, 100)
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x, y=y, alpha=0.7, s=100)
    plt.title('Sample Scatter Plot', fontsize=14)
    plt.xlabel('X values', fontsize=12)
    plt.ylabel('Y values', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, 'scatter_plot.png')
    plt.savefig(output_path)
    plt.close()
    return output_path

def fit_polynomial(x: np.ndarray, y: np.ndarray, degree: int = 2) -> np.ndarray:
    """
    使用最小二乘法拟合多项式曲线
    
    参数:
        x: 输入数据的x坐标，一维numpy数组
        y: 输入数据的y坐标，一维numpy数组
        degree: 多项式的次数，默认为2（二次多项式）
        
    返回:
        numpy.ndarray: 拟合后的y值，与输入x同维度
        
    示例:
        >>> x = np.array([1, 2, 3, 4, 5])
        >>> y = np.array([1, 4, 9, 16, 25])
        >>> y_fit = fit_polynomial(x, y, degree=2)
    """
    coeffs = np.polyfit(x, y, degree)
    poly = np.poly1d(coeffs)
    return poly(x)

def fit_spline(x: np.ndarray, y: np.ndarray, num_points: int = 100) -> Tuple[np.ndarray, np.ndarray]:
    """
    使用三次样条插值拟合数据点
    
    参数:
        x: 输入数据的x坐标，一维numpy数组
        y: 输入数据的y坐标，一维numpy数组
        num_points: 生成的拟合曲线上的点数，默认为100
        
    返回:
        tuple: 包含两个numpy数组的元组 (x_fit, y_fit)
            - x_fit: 插值点的x坐标
            - y_fit: 插值点的y坐标
            
    注意:
        使用scipy的splrep和splev函数实现三次样条插值
    """
    tck = interpolate.splrep(x, y, s=0)
    x_fit = np.linspace(min(x), max(x), num_points)
    y_fit = interpolate.splev(x_fit, tck, der=0)
    return x_fit, y_fit

def create_animated_fit(x: np.ndarray, 
                      y: np.ndarray, 
                      fit_func: Callable, 
                      title: str = 'Animated Fit',
                      output_file: str = 'animated_fit.gif',
                      frames: int = 50) -> None:
    """
    创建数据拟合过程的动画
    
    参数:
        x: 输入数据的x坐标，一维numpy数组
        y: 输入数据的y坐标，一维numpy数组
        fit_func: 用于拟合数据的函数，接受x并返回预测的y值
        title: 图表标题，默认为'Animated Fit'
        output_file: 输出GIF文件名，默认为'animated_fit.gif'
        frames: 动画总帧数，默认为50
        
    返回:
        None: 将动画保存为GIF文件
        
    注意:
        使用matplotlib.animation创建动画效果
        需要安装pillow库来保存GIF
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create line objects
    line_original, = ax.plot([], [], 'bo', alpha=0.5, label='Original Data')
    line_fit, = ax.plot([], [], 'r-', lw=2, label='Fitted Curve')
    
    # Set up the plot
    ax.set_xlim(min(x) - 0.5, max(x) + 0.5)
    ax.set_ylim(min(y) - 1, max(y) + 1)
    ax.set_title(title, fontsize=14)
    ax.set_xlabel('X values', fontsize=12)
    ax.set_ylabel('Y values', fontsize=12)
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.3)
    
    def init():
        line_original.set_data([], [])
        line_fit.set_data([], [])
        return line_original, line_fit
    
    def animate(i):
        # Show more data points as the animation progresses
        n_points = min(len(x), int(len(x) * (i + 1) / frames))
        x_show = x[:n_points]
        y_show = y[:n_points]
        
        # Update original data points
        line_original.set_data(x_show, y_show)
        
        # Update fitted curve if we have enough points
        if n_points > 3:
            try:
                y_fit = fit_func(x_show)
                line_fit.set_data(x_show, y_fit)
            except:
                pass
        
        return line_original, line_fit
    
    # Create animation
    ani = animation.FuncAnimation(fig, animate, init_func=init,
                                frames=frames, interval=50, blit=True)
    
    # 确保输出目录存在
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, output_file)
    
    # 保存GIF
    writer = PillowWriter(fps=20)
    ani.save(output_path, writer=writer, dpi=100)
    plt.close()
    print(f"Animation saved as {output_path}")
    return output_path

def demo_curve_fitting() -> None:
    """
    演示曲线拟合功能
    
    生成示例数据，并展示多项式拟合和样条插值的效果
    会生成两个文件：
    - polynomial_fit.gif: 多项式拟合过程动画
    - curve_fitting_comparison.png: 不同拟合方法对比图
    """
    # Create sample data with noise
    x = np.linspace(0, 10, 20)
    y = 2 * np.sin(x) + 0.5 * np.random.normal(size=len(x))
    
    # Polynomial fit
    y_poly = fit_polynomial(x, y, degree=3)
    
    # Spline fit
    x_spline, y_spline = fit_spline(x, y)
    
    # Create animated fit visualization
    create_animated_fit(x, y, 
                       lambda x: np.poly1d(np.polyfit(x, y, 3))(x),
                       title='Polynomial Fit Animation',
                       output_file='polynomial_fit.gif')
    
    # Create static comparison plot
    plt.figure(figsize=(12, 6))
    plt.scatter(x, y, color='blue', alpha=0.5, label='Original Data')
    plt.plot(x, y_poly, 'r-', lw=2, label='Polynomial Fit (deg=3)')
    plt.plot(x_spline, y_spline, 'g-', lw=2, label='Spline Fit')
    plt.title('Curve Fitting Comparison', fontsize=14)
    plt.xlabel('X values', fontsize=12)
    plt.ylabel('Y values', fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, 'curve_fitting_comparison.png')
    plt.savefig(output_path)
    plt.close()
    return output_path

def main():
    """
    主函数：执行所有可视化示例并保存结果到输出目录
    
    返回:
        dict: 包含生成文件路径的字典
    """
    print("正在创建示例可视化图表...")
    output_files = {}
    
    try:
        # 1. 创建基础图表
        print("\n1. 创建基础图表...")
        output_files['line_plot'] = create_sample_line_plot()
        output_files['scatter_plot'] = create_sample_scatter_plot()
        
        # 2. 演示曲线拟合
        print("\n2. 创建曲线拟合可视化...")
        output_files['polynomial_fit'] = os.path.join(OUTPUT_DIR, 'polynomial_fit.gif')
        output_files['curve_fitting_comparison'] = os.path.join(OUTPUT_DIR, 'curve_fitting_comparison.png')
        demo_curve_fitting()
        
        # 3. 输出生成的文件列表
        print("\n已生成以下可视化文件:")
        for desc, path in [
            ("- 正弦波折线图", output_files['line_plot']),
            ("- 带噪声的散点图", output_files['scatter_plot']),
            ("- 多项式拟合过程动画", output_files['polynomial_fit']),
            ("- 不同拟合方法对比图", output_files['curve_fitting_comparison'])
        ]:
            print(f"{desc}: {os.path.abspath(path)}")
            
        return output_files
        
    except Exception as e:
        print(f"\n错误: 生成可视化时出错 - {str(e)}")
        raise

if __name__ == "__main__":
    main()
