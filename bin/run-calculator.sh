#!/bin/bash

# 运行计算器应用程序
# 确保脚本执行时的工作目录是项目根目录
PROJECT_ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)

# 检查Python是否安装
if ! command -v python3 &> /dev/null; then
    echo "错误：未找到Python3，请先安装Python3环境"
        exit 1
        fi

        # 检查主程序文件是否存在
        if [ ! -f "$PROJECT_ROOT/src/计算器.py" ]; then
            echo "错误：未找到计算器主程序文件 $PROJECT_ROOT/src/计算器.py"
                exit 1
                fi

                # 启动计算器
                echo "正在启动Linux计算器..."
                python3 "$PROJECT_ROOT/src/计算器.py"
                