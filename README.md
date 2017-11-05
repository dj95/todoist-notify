# todoist-notify

This is a hacky and fun project in order to display todoist tasks easily through
libnotify on my linux system.

![screenshot](./screenshot.png)

It is easily extendable. Feel free to create pull requests!


### Requirements

- Python 3.5
- [pytodoist](https://github.com/Garee/pytodoist)
- todoist account
- libnotify
- python-gobject
- *Optional:* systemd


### Installation

- Install all requirements
- Make sure you are able to write to `/opt`
- Run `./setup.sh`


### Usage

- Fill in the credentials in `~/.config/todoist-notify/config.json`
- Start and enable the systemd-user-service
- Run `todoist-client` in order to display the notifications


### TODO

- ncurses frontend
- reminder
- complete backend


### License

(c) 2017 - Daniel Jankowski


The logo is copyrighted by todoist and does not belong to me.


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:


The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.


THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
