from api import app
from schematics.models import Model
from schematics.types import IntType, StringType
from schematics.exceptions import ModelConversionError, ModelValidationError


class Example(Model):
    """Validation for Example"""
    id = IntType(required=True)
    name = StringType(required=True, max_length=5)


@app.route('/examples/<int:example_id>', methods=['GET'])
def get_example(example_id):
    """Get one example's details"""

    # Flow
    # 1. Get inputs: Parsed by Flask from the URL
    # 2. Validate inputs
    # 3. If validation exception:
    #     3.1 Log exception
    #     3.2 Return error

    try:
        example = Example({
            'id': example_id,
            'name': '12345787'
        })

        example.validate()
    except ModelConversionError, mce:
        # ModelConversionError catches incorrect types
        app.logger.exception(mce.messages)
    except ModelValidationError, mve:
        # ModelValidationError catches validation errors
        app.logger.exception(mve.messages)

    # debug()
    # info()
    # warning()
    # error()
    # exception()
    # critical()

    # app.logger.debug('Testing the debug log statement')
    # app.logger.error('Test error statement')
    # app.logger.info('Test info statement')

    # Perform logic, file or DB operations

    # If error in logic/file/DB operations:
    #     Log exception
    #     Return error

    # Return response
    return "GET one example"
