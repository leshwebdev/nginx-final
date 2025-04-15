Weird scenario that's been bugging me so far (+open issues):

Inside the Ubuntu VM that's running the Flask UI Apps within a VENV:
- http://localhost:5004 -> "subpages" (/movies, /showtimes, /users) - render in HTML
- http://localhost -> "subpages" - return JSON.
- https://localhost:5004 -> "secure connection failed" <SSL_ERROR_RX_RECORD_TOO_LONG>.

(similar behavior observed when accessing the app from a different [physical] machine.)

I'm unsure how to simulate access to the app from a /24 CIDR, so I simulated by DENYing a /32 address on the same subnet (a physical computer that's otherwise able to access the app).

it's all a learning WIP :)
