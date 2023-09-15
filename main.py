import os
from pwr import Project, CodeLayer
from dotenv import load_dotenv
import argparse
load_dotenv()


class TeamsAppAgent(Project):

    def __init__(self, path, **kwargs):
        layers = [           
            CodeLayer(
                header='Cards - Layer 0',
                code_relative_path='cards',
                human_label='Cards',
                flag_label='cards'
            ),
            CodeLayer(
                header='API - Layer 1',
                code_relative_path='./',
                human_label='API',
                flag_label='api'
            )
        ]
        super().__init__(path, layers, **kwargs)


if __name__ == "__main__":

    # parse command line parameters 
    parser = argparse.ArgumentParser()
    parser.add_argument('--change', type=str)
    args = parser.parse_args()

    change = args.change

    if not change:
        raise Exception('Change is required; use --change <change>')

    kwargs = {
        'debug': {
            'write_file': True,
            'llm': False,
            'steps': True,
            'figma': {
                'page': 'Page 1'
            }
        },
        'llm': {
            
        }
    }

    path = os.path.join(os.path.dirname(__file__), '../azure-devops-app')

    agent = TeamsAppAgent(
        path=path
    )

    agent.forward(change, **kwargs)
