run:
	foreman start

install:
	sudo pip install -r requirements.txt

lint:
	flake8 *py 

clean:
	find . -name "*pyc" -delete

foreman: install
	sudo foreman export -a phat-rest -u pi systemd /etc/systemd/system
	sudo systemctl daemon-reload
	sudo systemctl restart hanoi.target
