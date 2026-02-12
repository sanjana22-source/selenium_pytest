from jsonschema import validate, ValidationError


class SchemaValidator:

    @staticmethod
    def validate_schema(response_json, schema):
        try:
            validate(instance=response_json, schema=schema)
        except ValidationError as e:
            raise AssertionError(f"Schema validation failed: {e.message}")