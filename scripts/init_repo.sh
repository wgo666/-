#!/bin/bash

# 初始化Git仓库
git init

# 创建项目目录结构
mkdir -p linux-calculator/src
mkdir -p linux-calculator/bin
mkdir -p linux-calculator/scripts
mkdir -p linux-calculator/tests
mkdir -p linux-calculator/.github/workflows

# 创建文件
touch linux-calculator/src/计算器.py
touch linux-calculator/bin/run-calculator.sh
touch linux-calculator/scripts/init_repo.sh
touch linux-calculator/tests/test_calculator.py
touch linux-calculator/.github/workflows/python-app.yml
touch linux-calculator/.gitignore
touch linux-calculator/LICENSE
touch linux-calculator/Makefile
touch linux-calculator/pyproject.toml
touch linux-calculator/Dockerfile
touch linux-calculator/README.md

echo "项目结构已创建！"