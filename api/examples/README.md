# API package

The basic structure for each REST resource.

## Function structure

- Get inputs
- Validate inputs
- If validation exception:
    - Log exception
    - Return error
- Perform logic, file or DB operations
- If error in logic/file/DB operations:
    - Log exception
    - Return error
- Return response
