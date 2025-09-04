import numpy as np
from scipy.stats import chi2

def calculate_cep(coordinates):
    """
    Calculates the Circular Error Probable (CEP) for a set of two-dimensional
    data points.

    CEP is a measure of the accuracy of a system, defined as the radius of a
    circle centered on the mean of the data that contains 50% of the data points.
    This calculation assumes the data follows a bivariate normal distribution.

    Args:
        coordinates (list of tuples or numpy.ndarray): A list of (x, y)
            coordinate pairs representing the data points.

    Returns:
        float: The calculated CEP value.
    """
    # Convert the list of tuples to a NumPy array for easier calculations.
    data = np.array(coordinates)

    # Calculate the standard deviation of the x and y coordinates.
    # We are using the sample standard deviation (ddof=1) since we are
    # typically working with a sample of data, not the entire population.
    std_x = np.std(data[:, 0], ddof=1)
    std_y = np.std(data[:, 1], ddof=1)

    # The standard deviation of the radial error (sigma_r) is the root
    # mean square of the individual axis standard deviations, assuming
    # the errors in x and y are uncorrelated.
    sigma_r = np.sqrt(std_x**2 + std_y**2)

    # CEP is the radius of the circle that contains 50% of the data.
    # For a circular normal distribution, the probability P of a point
    # falling within a radius R is given by:
    # P = 1 - exp(-R^2 / (2 * sigma^2))
    # We are solving for R when P=0.5.
    # 0.5 = 1 - exp(-CEP^2 / (2 * sigma_r^2))
    # exp(-CEP^2 / (2 * sigma_r^2)) = 0.5
    # -CEP^2 / (2 * sigma_r^2) = ln(0.5)
    # -CEP^2 = 2 * sigma_r^2 * ln(0.5)
    # CEP^2 = -2 * sigma_r^2 * ln(0.5)
    # CEP = sqrt(-2 * sigma_r^2 * ln(0.5))
    # Which simplifies to CEP ≈ 1.1774 * sigma_r

    cep_constant = np.sqrt(-2 * np.log(0.5))
    cep = cep_constant * sigma_r
    
    return cep

if __name__ == "__main__":
    # Example usage:
    # A set of data points (e.g., impact locations on a target)
    sample_data = [
        (1.2, 0.5),
        (-0.8, -1.0),
        (2.1, 1.8),
        (0.3, -2.5),
        (-1.5, 0.9),
        (0.0, 0.0),
        (-2.0, -1.5),
        (1.5, -0.5),
        (-0.1, 1.0),
        (0.8, 2.0)
    ]

    # Calculate the CEP for the sample data
    cep_value = calculate_cep(sample_data)

    print("Sample Data Points:")
    for point in sample_data:
        print(f"  ({point[0]:.2f}, {point[1]:.2f})")

    print("\n-------------------------------------------")
    print(f"Calculated Circular Error Probable (CEP): {cep_value:.3f}")
    print("-------------------------------------------")
    print("\nInterpretation:")
    print("This means that approximately 50% of the data points are expected to fall")
    print("within a circle with a radius of this value, centered at the average")
    print("location of the data points.")