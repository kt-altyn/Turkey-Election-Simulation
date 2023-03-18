import csv
from math import modf

akp_old_percentage = 42.49
mhp_old_percentage = 11.13
chp_old_percentage = 22.67
iyi_old_percentage = 10.01
hdp_old_percentage = 11.62
sp_old_percentage = 1.35
deva_old_percentage = 0
gelecek_old_percentage = 0
other_old_percentage = 0.73

akp_total_seats = 0
mhp_total_seats = 0
chp_total_seats = 0
iyi_total_seats = 0
hdp_total_seats = 0
sp_total_seats = 0
deva_total_seats = 0
gelecek_total_seats = 0
other_total_seats = 0

# Take input from the user for each party
print("Print estimated percentages by parties... (e.g 12.95)")
akp_multiplier = float(input("% for AKP: "))
mhp_multiplier = float(input("% for MHP: "))
chp_multiplier = float(input("% for CHP: "))
iyi_multiplier = float(input("% for IYI: "))
hdp_multiplier = float(input("% for HDP: "))
sp_multiplier = float(input("% for SP: "))
deva_multiplier = float(input("% for DEVA: "))
gelecek_multiplier = float(input("% for GELECEK: "))
other_multiplier = 100 - akp_multiplier - mhp_multiplier - chp_multiplier - iyi_multiplier - hdp_multiplier - sp_multiplier - deva_multiplier - gelecek_multiplier

# Define the filename and path of the CSV file
filename = "trpoll.csv"
output_filename = "deputy_chairs.csv"

# Open the CSV file and read its contents
with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    
     # Create the output CSV file and write the header row
    with open(output_filename, 'w', newline='') as output_file:
        writer = csv.writer(output_file, delimiter=';')
        writer.writerow(['city', 'akp', 'mhp', 'chp', 'iyi', 'hdp', 'sp', 'deva', 'gelecek'])
        
        # Iterate over each row in the CSV file
        for row in reader:
            # Get the city name from the current row
            city = row['city']
            
            # Get the vote count for each party from the current row
            akp_votes = int(row['akp'])
            mhp_votes = int(row['mhp'])
            chp_votes = int(row['chp'])
            iyi_votes = int(row['iyi'])
            hdp_votes = int(row['hdp'])
            sp_votes = int(row['sp'])
            deva_votes = int(row['deva'])
            gelecek_votes = int(row['gelecek'])
            other_votes = int(row['other'])
            
            # Apply the multipliers to each party's vote count
            akp_votes *= akp_multiplier/akp_old_percentage
            mhp_votes *= mhp_multiplier/mhp_old_percentage
            chp_votes *= chp_multiplier/chp_old_percentage
            iyi_votes *= iyi_multiplier/iyi_old_percentage
            hdp_votes *= hdp_multiplier/hdp_old_percentage
            sp_votes *= sp_multiplier/sp_old_percentage
            deva_votes = 0.5 * akp_votes * deva_multiplier / (akp_multiplier - deva_multiplier - gelecek_multiplier)
            gelecek_votes = 0.5 * akp_votes * gelecek_multiplier / (akp_multiplier - deva_multiplier - gelecek_multiplier)
            other_votes = other_multiplier * (other_votes/other_old_percentage)
            
            # Calculate the total number of votes cast in the city
            total_votes = akp_votes + mhp_votes + chp_votes + iyi_votes + hdp_votes + sp_votes + deva_votes + gelecek_votes + other_votes
            
            # Calculate the percentage of votes cast for each party in the city
            akp_percentage = akp_votes / total_votes
            mhp_percentage = mhp_votes / total_votes
            chp_percentage = chp_votes / total_votes
            iyi_percentage = iyi_votes / total_votes
            hdp_percentage = hdp_votes / total_votes
            sp_percentage = sp_votes / total_votes
            deva_percentage = deva_votes / total_votes
            gelecek_percentage = gelecek_votes / total_votes
            other_percentage = other_votes / total_votes
            
            # Calculate the number of deputy chairs that each party will get in the city
            akp_deputy_chairs = int(akp_percentage * int(row['vekil']))
            mhp_deputy_chairs = int(mhp_percentage * int(row['vekil']))
            chp_deputy_chairs = int(chp_percentage * int(row['vekil']))
            iyi_deputy_chairs = int(iyi_percentage * int(row['vekil']))
            hdp_deputy_chairs = int(hdp_percentage * int(row['vekil']))
            sp_deputy_chairs = int(sp_percentage * int(row['vekil']))
            deva_deputy_chairs = int(deva_percentage * int(row['vekil']))
            gelecek_deputy_chairs = int(gelecek_percentage * int(row['vekil']))
            
            # Calculate the fractional remainders for each party
            akp_remainder, _ = modf(akp_percentage * int(row['vekil']))
            mhp_remainder, _ = modf(mhp_percentage * int(row['vekil']))
            chp_remainder, _ = modf(chp_percentage * int(row['vekil']))
            iyi_remainder, _ = modf(iyi_percentage * int(row['vekil']))
            hdp_remainder, _ = modf(hdp_percentage * int(row['vekil']))
            sp_remainder, _ = modf(sp_percentage * int(row['vekil']))  
            deva_remainder, _ = modf(deva_percentage * int(row['vekil']))
            gelecek_remainder, _ = modf(gelecek_percentage * int(row['vekil']))
            
            # Assign the remaining deputy chairs to the parties with the highest fractional remainders
            while (akp_deputy_chairs + mhp_deputy_chairs + chp_deputy_chairs + iyi_deputy_chairs + hdp_deputy_chairs + sp_deputy_chairs + deva_deputy_chairs + gelecek_deputy_chairs) < int(row['vekil']):
                max_remainder = max(akp_remainder, mhp_remainder, chp_remainder, iyi_remainder, hdp_remainder, sp_remainder, deva_remainder, gelecek_remainder)
                
                if max_remainder == akp_remainder and akp_deputy_chairs < int(row['vekil']):
                    akp_deputy_chairs += 1
                    akp_remainder = -1
                elif max_remainder == mhp_remainder and mhp_deputy_chairs < int(row['vekil']):
                    mhp_deputy_chairs += 1
                    mhp_remainder = -1
                elif max_remainder == chp_remainder and chp_deputy_chairs < int(row['vekil']):
                    chp_deputy_chairs += 1
                    chp_remainder = -1
                elif max_remainder == iyi_remainder and iyi_deputy_chairs < int(row['vekil']):
                    iyi_deputy_chairs += 1
                    iyi_remainder = -1
                elif max_remainder == hdp_remainder and hdp_deputy_chairs < int(row['vekil']):
                    hdp_deputy_chairs += 1
                    hdp_remainder = -1
                elif max_remainder == sp_remainder and sp_deputy_chairs < int(row['vekil']):
                    sp_deputy_chairs += 1
                    sp_remainder = -1
                elif max_remainder == deva_remainder and deva_deputy_chairs < int(row['vekil']):
                    deva_deputy_chairs += 1
                    deva_remainder = -1
                elif max_remainder == gelecek_remainder and gelecek_deputy_chairs < int(row['vekil']):
                    gelecek_deputy_chairs += 1
                    gelecek_remainder = -1
            # Add the number of deputy chairs for each party to the total number of seats
            akp_total_seats += akp_deputy_chairs
            mhp_total_seats += mhp_deputy_chairs
            chp_total_seats += chp_deputy_chairs
            iyi_total_seats += iyi_deputy_chairs
            hdp_total_seats += hdp_deputy_chairs
            sp_total_seats += sp_deputy_chairs
            deva_total_seats += deva_deputy_chairs
            gelecek_total_seats += gelecek_deputy_chairs
            
            # Write the number of deputy chairs for each party to the output CSV file
            writer.writerow([city, akp_deputy_chairs, mhp_deputy_chairs, chp_deputy_chairs, iyi_deputy_chairs, hdp_deputy_chairs, sp_deputy_chairs, deva_deputy_chairs, gelecek_deputy_chairs])
                        
            
            # Print out the updated percentages and number of deputy chairs for each party in the city
            print(f"{city}: AKP {akp_percentage:.2%}, {akp_deputy_chairs} seat;MHP {mhp_percentage:.2%}, {mhp_deputy_chairs} seat; CHP {chp_percentage:.2%}, {chp_deputy_chairs} seat; IYI {iyi_percentage:.2%}, {iyi_deputy_chairs} seat; HDP {hdp_percentage:.2%}, {hdp_deputy_chairs} seat; SP {sp_percentage:.2%}, {sp_deputy_chairs} seat; DEVA {deva_percentage: .2%}, {deva_deputy_chairs} seat; GELECEK {gelecek_percentage: .2%}, {gelecek_deputy_chairs} seat; OTHER {other_percentage: 0.2%}")
            #print(total_votes)

# Print out the total number of seats for each party
print(f"Total seats: AKP {akp_total_seats}, MHP {mhp_total_seats}, CHP {chp_total_seats}, IYI {iyi_total_seats}, HDP {hdp_total_seats}, SP {sp_total_seats}, DEVA {deva_total_seats}, GELECEK {gelecek_total_seats}")
