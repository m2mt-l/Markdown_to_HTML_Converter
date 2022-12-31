import markdown
from argparse import ArgumentParser, Action, Namespace
from os.path import exists


class MarkDownAction(Action):
    def __call__(
        self,
        parser: ArgumentParser,
        namespace: Namespace,
        values: list,
        option_string: str,
    ):
        input_path, output_path = values

        if not exists(input_path):
            print(f"Input file {input_path} does not exist")
            return
        contents = ""

        with open(input_path) as f:
            contents = f.read()
        html = markdown.markdown(contents)
        # print(html)
        with open(output_path, "x") as f:
            f.write(html)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--markdown",
        type=str,
        nargs=2,
        action=MarkDownAction,
        metavar=("[input file]", "[output file]"),
        help="Convert a markdown file to a html file.",
    )

    args = parser.parse_args()
