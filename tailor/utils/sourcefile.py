from tailor.types.location import Location


def num_lines_in_file(filepath):
    with open(filepath) as file:
        return len(file.readlines())


def file_too_long(filepath, max_length):
    return 0 < max_length < num_lines_in_file(filepath)


def construct_too_long(ctx, max_length):
    return 0 < max_length < (ctx.stop.line - ctx.start.line)


def lines_too_long(filepath, max_length):
    long_lines = []
    if 0 < max_length:
        with open(filepath) as file:
            long_lines = [Location(lineno + 1, len(line.rstrip('\r\n')))
                          for lineno, line in enumerate(file)
                          if max_length < len(line.rstrip('\r\n'))]
    return long_lines


def name_too_long(ctx, max_length):
    return 0 < max_length < len(ctx.getText())