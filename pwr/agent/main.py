import os
from pwr import Project, CodeLayer
# from pwr.extras.db import DBLayer
# from pwr.extras.figma import FigmaLayer
from dotenv import load_dotenv
load_dotenv()


class TeamsAppProject(Project):

    def __init__(self, path, **kwargs):
        layers = [            
            CodeLayer(
                header='Cards - Layer 0',
                code_relative_path='app/cards',
                human_label='Cards',
                flag_label='cards'
            ),
            CodeLayer(
                header='API - Layer 1',
                code_relative_path='app',
                human_label='API',
                flag_label='api'
            )
        ]
        super().__init__(path, layers, **kwargs)


if __name__ == "__main__":

    kwargs = {
        'debug': {
            'write_file': True,
            'llm': False,
            'steps': True,
        },
    }

    path = os.path.join(os.path.dirname(__file__), '../../')

    agent = TeamsAppProject(
        path=path
    )

    change = ""

    agent.forward(change, **kwargs)
