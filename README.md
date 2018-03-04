# Inky REST

_Extremely thin HTTP wrapper around the [Inky pHAT](https://thepihut.com/products/inky-phat)_

## API

### `/paper`

#### `PATCH`

Accepts an `application/json` payload, representing the desired state of the 212x104 pixel display of the pHAT:

    {
      "display": [
        [0, 0, 0, 0, 1, 1, 2, 1, 0, 1, 0, 1, 2, 2, 1, 0, 1, 1, 0, 1, 2, 1, 0, 1,
         0, 0, 1, 1, 1, 1, 0, 1, 0, 2, 0, 2, 0, 1, 2, 2, 0, 2, 1, 2, 2, <etc>]
        [0, 0, 1, 0, 0, 1, 2, 2, 1, 1, 1, 1, 2, 1, 0, 0, 1, 0, 2, 2, 2, 1, 2, 2,
         2, 1, 1, 0, 0, 0, 2, 2, 1, 1, 2, 2, 1, 0, 0, 1, 2, 2, 0, 0, 1, <etc>],
        <etc>
      ]
    }

where the values translate as:

* 0: white pixel
* 1: black pixel
* 2: red pixel

## Running it

    make install

then

    python webserver.py

ought to do it. You'll also need `foreman` to install the `systemd` startup scripts, probably

    gem install foreman

then

    make foreman
