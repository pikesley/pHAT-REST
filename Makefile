run:
	foreman start

install:
	sudo pip install -r requirements.txt

lint:
	flake8 *py

clean:
	find . -name "*pyc" -delete

foreman: install
	rm -fr /tmp/inky-phat
	mkdir /tmp/inky-phat
	foreman export -a inky-phat -u pi systemd /tmp/inky-phat
	sudo rsync -av /tmp/inky-phat/ /etc/systemd/system/
	sudo systemctl daemon-reload
	sudo systemctl restart inky-phat.target
