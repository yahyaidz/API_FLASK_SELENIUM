from flask import Flask, request, jsonify
from conf import get_conf
from actions import ActionPerformer

app = Flask(__name__)

CONFIG = get_conf()

def execute_instructions():
    """
    Executes a series of actions specified in the request JSON.

    Returns:
        JSON response containing the result of the actions.
    """
    instructions = request.json
    actions = instructions.get('actions', [])

    if not actions:
        return jsonify({'error': 'No actions provided in the instructions'}), 400

    action_performer = ActionPerformer(CHROMEDRIVER_PATH=CONFIG['CHROMEDRIVER_PATH'])
    action_performer.start_driver()

    result = []
    for action in actions:
        action_type = action.get('type')
        if hasattr(action_performer, action_type):
            action_func = getattr(action_performer, action_type)
            params = {key: value for key, value in action.items() if key != 'type'}
            result.append(action_func(**params))
        else:
            result.append({'error': f'Action type {action_type} not supported'})

    action_performer.stop_driver()

    return jsonify({'result': result}), 200

@app.route('/execute_instructions', methods=['POST'])
def handle_execute_instructions():
    """
    Handles the POST request to execute instructions.

    Returns:
        JSON response with the result of the actions.
    """
    return execute_instructions()

if __name__ == '__main__':
    app.run(debug=True)
