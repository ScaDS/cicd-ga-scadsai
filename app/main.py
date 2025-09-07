import importlib
import os
from collections.abc import Callable

import gradio as gr
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure


# Load availabe analysis functions dynamically from modules in the "analysis" directory
def load_analysis_funcs() -> dict[str, Callable[[pd.Series], float]]:
    """Load analysis functions from modules in the "analysis" directory.

    Returns:
        dict[str, Callable[[pd.Series], float]]: A dictionary mapping module names to their compute functions.

    """
    analysis_dir = os.path.join(os.path.dirname(__file__), "analysis")
    analysis_funcs = {}

    for filename in os.listdir(analysis_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            module = importlib.import_module(f"app.analysis.{module_name}")
            # Only add if `compute` function exists
            if hasattr(module, "compute"):
                analysis_funcs[module_name] = module.compute
    return analysis_funcs


# Plotting function to visualize the DataFrame
def plot_df(df: pd.DataFrame) -> Figure:
    """Plot the DataFrame.

    Args:
        df (pd.DataFrame): DataFrame to plot.

    Returns:
        Figure: A matplotlib Figure object containing the plot.

    """
    fig, ax = plt.subplots(figsize=(6, 4))
    df.plot(ax=ax)
    return fig


analysis_modules = load_analysis_funcs()
df = pd.read_csv("app/data/dwd_leipzig_temp.csv", sep=";", index_col=[0], parse_dates=True)

# UI
demo = gr.Interface(
    fn=lambda selected: (
        "\n".join(f"{name}: {analysis_modules[name](df['temperature'])}" for name in selected),
        plot_df(df),
    ),
    inputs=gr.CheckboxGroup(choices=list(analysis_modules.keys()), label="Select Analyses"),
    outputs=[gr.Textbox(label="Analysis Results"), gr.Plot(label="Temperature Data")],
    title="Data Analysis App",
    description="Analysis and Visualization of Temperature Data.",
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
