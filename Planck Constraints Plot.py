# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load and process PLANCK data
csv_path = 'PLANCK Data.csv'
data = pd.read_csv(csv_path)

# Split the single column into multiple columns based on the delimiter ';'
columns_split = data.iloc[:, 0].str.split(';', expand=True)
columns_split.columns = [
    'ns95', 'r95', 'ns65', 'r65', 'nsBK95', 'rBK95', 'nsBK68', 'rBK68', 'nsBAO95', 'rBAO95', 'nsBAO68', 'rBAO68'
]

# Convert all values to numeric, ignoring non-numeric headers
columns_split = columns_split.apply(pd.to_numeric, errors='coerce')

# Plot Planck constraints
def plot_planck_constraints():
    plt.figure(figsize=(10, 6))
    plt.xlim(0.94, 1.0)
    plt.ylim(0, 0.2)

    # Fill regions for 68% confidence levels
    plt.fill_between(columns_split['ns65'], 0, columns_split['r65'], color='yellow', alpha=0.4, label='68% CL')
    plt.fill_between(columns_split['nsBK68'], 0, columns_split['rBK68'], color='red', alpha=0.4, label='68% CL BK14')
    plt.fill_between(columns_split['nsBAO68'], 0, columns_split['rBAO68'], color='blue', alpha=0.4, label='68% CL BAO')

    # Plot 95% confidence levels
    plt.plot(columns_split['ns95'], columns_split['r95'], label='95% CL', color='yellow', linestyle='--')
    plt.plot(columns_split['nsBK95'], columns_split['rBK95'], label='95% CL BK14', color='red', linestyle='--')
    plt.plot(columns_split['nsBAO95'], columns_split['rBAO95'], label='95% CL BAO', color='blue', linestyle='--')

    # Add labels, title, and legend
    plt.xlabel('$n_s$ (Spectral Index)', fontsize=14)
    plt.ylabel('$r$ (Tensor-to-Scalar Ratio)', fontsize=14)
    plt.title('Planck Constraints on $n_s$ and $r$', fontsize=16)
    plt.legend(fontsize=12)

    # Display grid and plot
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

# Run the plotting function
if __name__ == "__main__":
    plot_planck_constraints()
