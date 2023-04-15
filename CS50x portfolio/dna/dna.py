import csv
import sys


def main():
    count = 0

    # TODO: Check for command-line usage
    if len(sys.argv)!= 3:
        print("Missing command line argument (need 3)")
        sys.exit(1)

    # TODO: Read DNA sequence file into a variable
    file = open(sys.argv[2])
    sequence= file.read()

    
    # TODO: Read database file into a variable
    with open(sys.argv[1],"r") as file:
        database = csv.DictReader(file)

        for row in database:
            for keys, values in row.items():
                if keys=="name":
                    continue

                # TODO: Find longest match of each STR in DNA sequence
                number = longest_match(sequence, keys)
                #print (row["name"],number, values)
                if int(number) == int(values):
                    count+= 1
                # TODO: Check database for matching profiles
                if count == (len(row)-1):
                    print(row["name"])
                    file.close()
                    sys.exit(0)
            count=0


    file.close()
    print("No match found")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()



#number = longest_match(sequence, keys)
            #for i in range(len(values)):
               # if number == values[i]:
                   # print(row["name"])
                    #file.close()
                    #sys.exit(0)
