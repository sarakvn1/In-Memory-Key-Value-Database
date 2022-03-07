def clean_inputs(new_input):
    new_line = new_input.replace("[ ", "[").replace(" ]", "]").replace(", ", ",").replace(" ,", ",")
    return new_line


def split_input(new_input):
    first_input = None
    second_input = None
    input_length = None
    cmd = None
    try:
        s_input = new_input.split(' ')
        input_length = len(s_input)
        cmd = s_input[0].replace('\n', '')
        first_input = s_input[1].replace('\n', '')
        second_input = s_input[2].replace('\n', '')

    except IndexError:
        pass

    return cmd, first_input, second_input, input_length
