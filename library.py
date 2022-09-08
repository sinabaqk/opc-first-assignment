from design import Design

class Library:

    def main():
        test_file = open('testdata.txt', 'r')
        lines = test_file.readlines()
        if len(lines) > 0:
            # remove the first line (data headers)
            lines.pop(0)
        designs = list()
        for line in lines:
            # remove newline char ('\n') from end of line, then split each line by tab ('\t')
            values = line.strip().split('\t')
            # create a Design instance
            design = Design(values[0], int(values[1]), int(values[2]), int(values[3]), int(values[4]), int(values[5]), values[6])
            designs.append(design)
        # sort designs by the density in descending order
        designs.sort(key=lambda d: d.density, reverse=True)
        # print designs with density data
        for design in designs:
            print('Name: {} - Density: {}'.format(design.name, design.density))

    if __name__ == "__main__":
        main()
