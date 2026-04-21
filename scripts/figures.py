"""
Meta分析图表生成器 — 发表级森林图/漏斗图

用户视角：输入效应量数据 → 自动生成Nature/NEJM级图表
"""

def forest_plot_config():
    return {
        "type": "forest_plot",
        "style": "medical",
        "width": 800,
        "height": 600,
        "null_line": True,
        "ci_lines": True,
        "weights": True,
        "font": "Arial",
        "dpi": 300,
    }

def funnel_plot_config():
    return {
        "type": "funnel_plot",
        "style": "medical",
        "width": 600,
        "height": 600,
        "contour": True,
        "p_value": 0.05,
    }
