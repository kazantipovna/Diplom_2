codes = {
    200: ['"success":true'],
    400: ['"success":false', 'Ingredient ids must be provided'],
    401: ['"success":false', 'email or password are incorrect', 'You should be authorised'],
    403: ['"success":false', 'Email, password and name are required fields', 'User already exists', 'User with such email already exists'],
    500: ['Internal Server Error']
}