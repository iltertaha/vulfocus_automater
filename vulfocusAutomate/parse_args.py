import argparse


def parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--image-file', help='File containing list of images')
    parser.add_argument('-t', '--template-file', help='File containing list of nuclei templates')
    parser.add_argument('-w', '--working-dir')
    parser.add_argument('-o', '--output-dir', default='./nuclei_results',\
        help='Path to the folder in which the nuclei results are stored. Default is nuclei_results.')
    parser.add_argument('-v', '--verbose', help='Print verbose output', action='store_true')

    args = parser.parse_args()

    assert args.image_file is not None, 'path to vulnerable images cannot be empty.'
    assert args.template_file is not None, 'path to nuclei templates cannot be empty.'
    assert args.working_dir is not None, 'working directory cannot be empty.'

    arguments = dict()
    arguments['image-file'] = args.image_file
    arguments['template-file'] = args.template_file
    arguments['working-dir'] = args.working_dir
    arguments['output-dir'] = args.output_dir
    arguments['verbose'] = args.verbose

    return arguments

    # print(arguments)

# parse()