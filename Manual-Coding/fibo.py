#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
斐波那契数列性质探索程序
Fibonacci Sequence Properties Exploration
"""

import math
import matplotlib.pyplot as plt
import numpy as np

def fibonacci_generator(n):
    """生成前n个斐波那契数"""
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def fibonacci_recursive(n):
    """递归计算第n个斐波那契数"""
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_golden_ratio(n):
    """使用黄金比例公式计算第n个斐波那契数"""
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return round((phi**n - psi**n) / math.sqrt(5))

def explore_golden_ratio_convergence():
    """探索黄金比例收敛性质"""
    print("=== 黄金比例收敛性质探索 ===")
    fib = fibonacci_generator(20)
    ratios = []
    
    for i in range(2, len(fib)):
        if fib[i-1] != 0:
            ratio = fib[i] / fib[i-1]
            ratios.append(ratio)
            print(f"F({i})/F({i-1}) = {fib[i]}/{fib[i-1]} = {ratio:.10f}")
    
    golden_ratio = (1 + math.sqrt(5)) / 2
    print(f"\n真实黄金比例 φ = {golden_ratio:.10f}")
    print(f"最后一个比值与黄金比例的差值: {abs(ratios[-1] - golden_ratio):.10e}")
    
    return ratios

def analyze_odd_even_pattern():
    """分析奇偶性质"""
    print("\n=== 奇偶性质分析 ===")
    fib = fibonacci_generator(20)
    
    pattern = []
    for i, num in enumerate(fib):
        parity = "偶" if num % 2 == 0 else "奇"
        pattern.append(parity)
        print(f"F({i}) = {num} ({parity})")
    
    print(f"\n奇偶模式: {' '.join(pattern[:15])}")
    print("观察: 每3个数字重复一次奇偶模式 (奇-奇-偶)")

def explore_divisibility_properties():
    """探索整除性质"""
    print("\n=== 整除性质探索 ===")
    fib = fibonacci_generator(25)
    
    # 探索能被3整除的斐波那契数
    divisible_by_3 = []
    for i, num in enumerate(fib):
        if num % 3 == 0:
            divisible_by_3.append(i)
    
    print(f"能被3整除的斐波那契数的位置: {divisible_by_3}")
    print("观察: 每4个位置重复一次 (F(0), F(4), F(8), F(12)...)")
    
    # 探索能被5整除的斐波那契数
    divisible_by_5 = []
    for i, num in enumerate(fib):
        if num % 5 == 0:
            divisible_by_5.append(i)
    
    print(f"能被5整除的斐波那契数的位置: {divisible_by_5}")
    print("观察: 每5个位置重复一次")

def explore_sum_properties():
    """探索和的性质"""
    print("\n=== 和的性质探索 ===")
    fib = fibonacci_generator(15)
    
    # 前n项和
    cumulative_sum = []
    for i in range(len(fib)):
        current_sum = sum(fib[:i+1])
        cumulative_sum.append(current_sum)
        print(f"前{i+1}项和: {current_sum}")
    
    print("\n验证公式: 前n项和 = F(n+2) - 1")
    for i in range(len(fib)-2):
        expected = fib[i+2] - 1
        actual = cumulative_sum[i]
        print(f"前{i+1}项和: {actual}, F({i+3})-1 = {expected}, 匹配: {actual == expected}")

def visualize_fibonacci_properties():
    """可视化斐波那契数列性质"""
    fib = fibonacci_generator(20)
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('斐波那契数列性质可视化', fontsize=16)
    
    # 1. 数列增长趋势
    ax1.plot(range(len(fib)), fib, 'bo-', linewidth=2, markersize=6)
    ax1.set_title('斐波那契数列增长趋势')
    ax1.set_xlabel('索引 n')
    ax1.set_ylabel('F(n)')
    ax1.grid(True, alpha=0.3)
    
    # 2. 黄金比例收敛
    ratios = []
    for i in range(2, len(fib)):
        if fib[i-1] != 0:
            ratios.append(fib[i] / fib[i-1])
    
    golden_ratio = (1 + math.sqrt(5)) / 2
    ax2.plot(range(2, len(ratios)+2), ratios, 'ro-', linewidth=2, markersize=6)
    ax2.axhline(y=golden_ratio, color='g', linestyle='--', linewidth=2, label=f'黄金比例 φ = {golden_ratio:.6f}')
    ax2.set_title('相邻项比值收敛到黄金比例')
    ax2.set_xlabel('索引 n')
    ax2.set_ylabel('F(n)/F(n-1)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # 3. 对数尺度下的线性增长
    ax3.semilogy(range(1, len(fib)), fib[1:], 'go-', linewidth=2, markersize=6)
    ax3.set_title('对数尺度下的指数增长')
    ax3.set_xlabel('索引 n')
    ax3.set_ylabel('log(F(n))')
    ax3.grid(True, alpha=0.3)
    
    # 4. 奇偶性质饼图
    odd_count = sum(1 for x in fib if x % 2 == 1)
    even_count = len(fib) - odd_count
    
    ax4.pie([odd_count, even_count], labels=['奇数', '偶数'], autopct='%1.1f%%', startangle=90)
    ax4.set_title('前20项奇偶数分布')
    
    plt.tight_layout()
    plt.show()

def fibonacci_spiral():
    """绘制斐波那契螺旋"""
    fib = fibonacci_generator(10)
    
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # 绘制正方形
    x, y = 0, 0
    for i, size in enumerate(fib[1:]):  # 从F(1)开始
        if i % 4 == 0:  # 右
            rect = plt.Rectangle((x, y), size, size, fill=False, edgecolor='blue', linewidth=2)
            x += size
        elif i % 4 == 1:  # 上
            rect = plt.Rectangle((x-size, y), size, size, fill=False, edgecolor='blue', linewidth=2)
            y += size
        elif i % 4 == 2:  # 左
            rect = plt.Rectangle((x-size, y-size), size, size, fill=False, edgecolor='blue', linewidth=2)
            x -= size
        else:  # 下
            rect = plt.Rectangle((x, y-size), size, size, fill=False, edgecolor='blue', linewidth=2)
            y -= size
        
        ax.add_patch(rect)
        
        # 添加数字标签
        center_x = rect.get_x() + rect.get_width()/2
        center_y = rect.get_y() + rect.get_height()/2
        ax.text(center_x, center_y, str(size), ha='center', va='center', fontsize=12, fontweight='bold')
    
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    ax.set_aspect('equal')
    ax.set_title('斐波那契螺旋与正方形')
    ax.grid(True, alpha=0.3)
    plt.show()

def main():
    """主函数"""
    print("斐波那契数列性质探索程序")
    print("=" * 50)
    
    # 生成基本数列
    print("前20个斐波那契数:")
    fib = fibonacci_generator(20)
    for i, num in enumerate(fib):
        print(f"F({i}) = {num}")
    
    # 探索各种性质
    explore_golden_ratio_convergence()
    analyze_odd_even_pattern()
    explore_divisibility_properties()
    explore_sum_properties()
    
    # 可视化
    print("\n正在生成可视化图表...")
    visualize_fibonacci_properties()
    fibonacci_spiral()
    
    # 性能比较
    print("\n=== 性能比较 ===")
    import time
    
    n = 30
    
    # 递归方法
    start_time = time.time()
    result_recursive = fibonacci_recursive(n)
    recursive_time = time.time() - start_time
    
    # 黄金比例方法
    start_time = time.time()
    result_golden = fibonacci_golden_ratio(n)
    golden_time = time.time() - start_time
    
    # 迭代方法
    start_time = time.time()
    result_iterative = fibonacci_generator(n+1)[n]
    iterative_time = time.time() - start_time
    
    print(f"计算F({n}):")
    print(f"递归方法: {result_recursive}, 用时: {recursive_time:.6f}秒")
    print(f"黄金比例方法: {result_golden}, 用时: {golden_time:.6f}秒")
    print(f"迭代方法: {result_iterative}, 用时: {iterative_time:.6f}秒")

if __name__ == "__main__":
    main()
