# Montreal Gas Prices Analysis

This Python script analyzes the gas prices in Montreal over a period of four days. It reads data from Excel files, calculates the average gas price for each day, and fits a polynomial model to the data.

## Dependencies

The script requires the following Python libraries:
- numpy
- matplotlib
- pandas

## How to Run

1. Ensure that the required Python libraries are installed.
2. Update the file paths in the script to point to your Excel files.
3. Run the script in a Python environment.

## What the Script Does

1. Reads gas price data from Excel files for four different days.
2. Calculates the average gas price for each day.
3. Fits a 3rd order polynomial to the average gas price data.
4. Plots the average gas prices and the fitted polynomial.
5. Prints the polynomial's prediction for the gas price on the fourth day.

## Output

The script outputs a plot showing the average gas prices and the fitted polynomial. The title of the plot includes the Mean Squared Error (MSE) of the fitted polynomial. The script also prints the polynomial's prediction for the gas price on the fourth day.

## Note

This script assumes that the Excel files contain a column labeled 'Price' with the gas price data.

## License
This project is licensed under the terms of the MIT license. For more information, please refer to the LICENSE file.

## Contact
For any queries or suggestions, please open an issue on this repository. Happy coding!
