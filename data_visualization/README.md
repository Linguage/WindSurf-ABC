# Python Data Visualization Project

This project provides a collection of Python scripts and notebooks for data visualization using popular libraries like Matplotlib, Seaborn, and Plotly.

## Project Structure

```
data_visualization/
├── data/               # Directory for storing data files
├── notebooks/          # Jupyter notebooks for interactive visualization
├── src/                # Python source files
│   └── basic_visualizations.py  # Example visualization scripts
├── requirements.txt    # Project dependencies
└── README.md           # This file
```

## Setup

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Examples

1. Run the basic visualization script:
   ```bash
   python src/basic_visualizations.py
   ```
   This will generate sample plots in the project directory.

2. For interactive visualization, launch Jupyter Lab:
   ```bash
   jupyter lab
   ```
   Then open the notebooks in the `notebooks/` directory.

## Dependencies

- Python 3.8+
- Core: pandas, numpy
- Visualization: matplotlib, seaborn, plotly
- Jupyter for interactive notebooks

## Adding Your Own Visualizations

1. Place your data files in the `data/` directory
2. Create new Python scripts in `src/` or Jupyter notebooks in `notebooks/`
3. Follow the examples in `basic_visualizations.py` to create your visualizations

## License

This project is open source and available under the MIT License.
