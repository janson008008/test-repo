#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的Python脚本示例

这个脚本演示了基本的Python功能，包括：
1. 打印欢迎信息
2. 计算并显示斐波那契数列
3. 处理用户输入
"""

import time

def fibonacci(n):
    """
    计算斐波那契数列的前n项
    
    参数:
        n (int): 要计算的项数
    
    返回:
        list: 斐波那契数列的前n项
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def main():
    """
    主函数
    """
    print("=== 简单Python脚本示例 ===")
    print("欢迎使用这个简单的Python脚本！")
    print()
    
    # 打印当前时间
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"当前时间: {current_time}")
    print()
    
    # 计算并显示斐波那契数列
    print("斐波那契数列前10项:")
    fib_sequence = fibonacci(10)
    for i, num in enumerate(fib_sequence, 1):
        print(f"第{i}项: {num}")
    print()
    
    # 处理用户输入
    user_input = input("请输入你的名字: ")
    print(f"你好, {user_input}！")
    print()
    
    print("脚本执行完成！")

if __name__ == "__main__":
    main()
