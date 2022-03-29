from csv import writer
from csv import reader
import translator

#the function below is dedicated to the translation of JECAM crops groups to french. In a second time, I will have to apply the function to all languages, and also to crops inside a group. 

def add_groups_french(input_file, output_file, transform_row):
    """ Append a column in existing csv using csv.reader / csv.writer classes"""
    # Open the input_file in read mode and output_file in write mode
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w', newline='') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Pass the list / row in the transform function to add column text for this row
            transform_row(row, csv_reader.line_num)
            # Write the updated row / list to the output file
            csv_writer.writerow(row)

add_groups_french('../../data/csv/JECAM/JECAM_en.csv', '../../data/csv/JECAM/JECAM_ue.csv', lambda row, line_num: row.append(translator.translate(f"{row[2]}", "fr")))

#issue if this method : does not recognize when the word already has been translated