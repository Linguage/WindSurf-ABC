# 3. Windsurf 基本功能演示

## 3.1 代码搜索功能

### 3.1.1 基本搜索

Windsurf 提供了强大的代码搜索功能，可以通过以下方式使用：

1. **文件内搜索**
   - 快捷键：`Ctrl+F` (Windows/Linux) 或 `Cmd+F` (macOS)
   - 支持正则表达式和大小写敏感搜索

2. **全局搜索**
   - 快捷键：`Ctrl+Shift+F` (Windows/Linux) 或 `Cmd+Shift+F` (macOS)
   - 支持按文件类型、目录过滤
   - 支持保存搜索条件

### 3.1.2 智能代码导航

- **转到定义**：`F12` 或 `Ctrl+点击`
- **查找所有引用**：`Shift+F12`
- **查看实现**：`Ctrl+F12`
- **快速查看**：`Alt+F12` (预览定义而不离开当前文件)

### 3.1.3 符号搜索

- 搜索类、方法、变量等符号
- 使用 `@` 前缀搜索符号
- 使用 `#` 前缀搜索工作区符号

## 3.2 代码编辑功能

### 3.2.1 智能代码补全

Windsurf 提供智能的代码补全功能：
- 基本代码补全：`Ctrl+Space`
- 智能类型匹配补全
- 片段补全（输入 `for` 后按 `Tab` 生成 for 循环）

### 3.2.2 代码重构

- **重命名符号**：`F2`
- **提取方法**：`Ctrl+Shift+R`
- **提取变量**：`Ctrl+Alt+V`
- **内联变量**：`Ctrl+Alt+N`

### 3.2.3 代码格式化

- 格式化文档：`Shift+Alt+F`
- 格式化选中内容：`K F`
- 配置格式化选项：`Ctrl+,` 打开设置，搜索 "formatter"

## 3.3 终端集成

### 3.3.1 内置终端

- 打开/关闭终端：`Ctrl+``
- 创建新终端：`Ctrl+Shift+``
- 拆分终端：`Ctrl+\`

### 3.3.2 任务运行器

1. 配置任务：`.vscode/tasks.json`
2. 运行任务：`Ctrl+Shift+B`
3. 调试任务：`F5`

## 3.4 版本控制集成

### 3.4.1 基本 Git 操作

- 初始化仓库：`Git: Initialize Repository`
- 暂存更改：`+` 图标或 `Git: Stage Changes`
- 提交更改：`√` 图标或 `Git: Commit`
- 推送更改：`...` > `Push`

### 3.4.2 分支管理

- 创建新分支：`Git: Create Branch`
- 切换分支：底部状态栏点击分支名
- 合并分支：`Git: Merge Branch`

## 3.5 调试功能

### 3.5.1 启动调试

1. 设置断点：点击行号左侧
2. 启动调试：`F5`
3. 使用调试控制台：
   - 继续：`F5`
   - 单步跳过：`F10`
   - 单步进入：`F11`
   - 单步跳出：`Shift+F11`
   - 重启：`Ctrl+Shift+F5`
   - 停止：`Shift+F5`

### 3.5.2 调试配置

创建 `.vscode/launch.json` 文件配置调试环境：

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}
```

## 3.6 AI 驱动的功能

### 3.6.1 智能代码补全

Windsurf 的 AI 代码补全不仅仅是简单的文本匹配，而是基于上下文的智能建议：

```python
# 示例：AI 理解上下文并提供准确建议
def calculate_user_stats(users):
    total_users = len(users)
    # 当您输入 "active_" 时，AI 会建议 "active_users"
    active_users = [user for user in users if user.is_active]
    # AI 还会建议相关的统计计算
    return {
        'total': total_users,
        'active': len(active_users),
        'inactive': total_users - len(active_users)
    }
```

### 3.6.2 自然语言编程

使用自然语言描述您想要实现的功能：

```
# 示例对话
用户: "创建一个函数来验证电子邮件地址"
Windsurf: 生成以下代码...

import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
```

### 3.6.3 代码解释与文档生成

选中代码，让 Windsurf 为您解释或生成文档：

```python
def binary_search(arr, target):
    """
    使用二分查找算法在已排序数组中查找目标值
    
    Args:
        arr (list): 已排序的数组
        target: 要查找的目标值
    
    Returns:
        int: 目标值的索引，如果未找到返回 -1
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

## 3.7 基本编辑技巧

### 3.7.1 多行编辑

- 按住 `Alt` 键并点击多个位置创建多个光标
- 使用 `Ctrl+Alt+上/下箭头` 在上下行创建光标
- `Ctrl+D` 选择相同的单词进行批量编辑

### 3.7.2 代码片段

使用内置的代码片段快速生成常用代码：
- 输入 `for` + `Tab` 生成循环结构
- 输入 `if` + `Tab` 生成条件语句
- 输入 `def` + `Tab` 生成函数定义

### 3.7.3 快速修复

当代码出现问题时，Windsurf 会提供快速修复建议：
- 点击灯泡图标查看建议
- 使用 `Ctrl+.` 打开快速修复菜单

---

> 下一章：[代码搜索与导航](./4-代码搜索与导航.md)

## 练习

1. **搜索功能掌握**：练习使用文件内搜索和全局搜索功能
2. **代码导航实践**：练习使用"转到定义"和"查找引用"功能
3. **调试基础**：设置简单的断点并运行调试
4. **AI功能体验**：尝试使用AI代码补全和解释功能
5. **基础编辑**：练习多行编辑和代码片段使用
