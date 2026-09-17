# this line imports some custom exceptions for use in this lab
# raise/handle them just like Exception, ValueError, or any other type of exception
from exceptions import (
    MeasurementUnitException,
    MissingValueException,
    TextFormatException,
)


def compute_BMI(height: float, weight: float) -> float:
    body_mass_index = weight / (height**2)
    return (f'{body_mass_index:.2f}')


def parse_row(row: str) -> list:
    line = row.split(",")

    if len(line) != 5:
        raise TextFormatException

    for item in line:

        if item == "":
            raise MissingValueException

    line[0] = int(line[0])
    line[3] = float(line[3])
    line[4] = float(line[4])

    if line[4] > 3:
        raise MeasurementUnitException

    if range(len(line)) != int or float or str:

        raise ValueError


    return line


def main():
    file = open("data.csv")
    next(file)

    # 1. Open the new file to write your results
    outfile = open("bmi_output.csv", "w")
    outfile.write("Exam ID,BMI\n")  # Write CSV header

    for row in file:
        try:
            attributes = parse_row(row)
            bmi = compute_BMI(attributes[4], attributes[3])

            # 2. Write each valid result to the new file
            outfile.write(f"{attributes[0]},{bmi}\n")

        except MissingValueException:
            print(f"ID: {row.split(',')[0]} Missing value")

        except TextFormatException:
            print(f"ID: {row.split(',')[0]} Format Error")

        except MeasurementUnitException:
            print(f"ID: {row.split(',')[0]} Measurement error")

    # 3. Close both files
    file.close()
    outfile.close()


main()
