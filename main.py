# this line imports some custom exceptions for use in this lab
# raise/handle them just like Exception, ValueError, or any other type of exception
from exceptions import TextFormatException, MissingValueException, MeasurementUnitException


def compute_BMI(height: float, weight: float) -> float:
    
    body_mass_index =  weight / (height**2)
    return body_mass_index
    

def parse_row(row: str) -> list:
    
    line = row.split(",")


    if len(line) != 5:
        raise TextFormatException

    if line[3] == '':

        raise MissingValueException


    line[0] = int(line[0])
    line[3] = float(line[3])
    line[4] = float(line[4])

    if line[4] >= 3:
        raise MeasurementUnitException

    return line
    


def main():

    file = open('data.csv')
    next(file)

    for row in file:

        try:

            attributes = parse_row(row)
            bmi = compute_BMI(attributes[4],attributes[3])
            
        except MissingValueException:
            print(f"ID: {row.split(',')[0]} Missing value")

        except TextFormatException:
            print(f"ID: {row.split(',')[0]} Format Error")

        except MeasurementUnitException:
            print(f"ID: {row.split(',')[0]} Measurement error")



main()