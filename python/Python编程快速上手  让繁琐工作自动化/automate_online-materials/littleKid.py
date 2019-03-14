if name == 'Alice':      # noqa: F821 undefined name 'name'
    print('Hi, Alice.')
elif age < 12:           # noqa: F821 undefined name 'age'
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')
