import os
from pwr import Project, CodeLayer
from pwr.extras.db import DBLayer
from pwr.extras.figma import FigmaLayer
from dotenv import load_dotenv
load_dotenv()


class Zen3TierProject(Project):

    def __init__(self, path, **kwargs):
        layers = [
            FigmaLayer(
                header='Figma - Layer 0'
            ),
            CodeLayer(
                header='Mobile - Layer 1',
                code_relative_path='client',
                human_label='Mobile',
                flag_label='mobile'
            ),
            CodeLayer(
                header='GraphQL - Layer 2',
                code_relative_path='server',
                human_label='Graphql',
                flag_label='graphql'
            ),
            DBLayer(
                header='Database - Layer 3'
            )
        ]
        super().__init__(path, layers, **kwargs)


if __name__ == "__main__":

    kwargs = {
        'debug': {
            'write_file': True,
            'llm': False,
            'steps': True,
            'figma': {
                'page': 'Page 1'
            }
        },
    }

    path = os.path.join(os.path.dirname(__file__), '../Zen-Champions')

    agent = Zen3TierProject(
        path=path
    )

    change = ""

    agent.forward(change, **kwargs)
